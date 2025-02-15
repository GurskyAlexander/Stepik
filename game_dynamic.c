#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
//#include <ncurses.h>

#define LEIGHT 80
#define WIDTH 25

void input_matrix(int **matrix);
void update_matrix(int **matrix_1, int **matrix_2);
int count_neighbors(int **matrix_1, int i, int j);
int gods_providence(int neighbors, int condition);
void swap_matrix(int **matrix_1, int **matrix_2);
int set_game_speed(char control, int *game_over, int time);
int is_apocalipsis(int **matrix_1, int **matrix_2);

int main(void) {
    int time = 100;
    int game_over = 1;

    int **matrix_1 = malloc(WIDTH * sizeof(int*));
    for (int i = 0; i < WIDTH; i++)
        matrix_1[i] = malloc(LEIGHT * sizeof(int));

    int **matrix_2 = malloc(WIDTH * sizeof(int*));
    for (int i = 0; i < WIDTH; i++)
        matrix_2[i] = malloc(LEIGHT * sizeof(int));

    input_matrix(matrix_1);
    // initscr();
    // nodelay(stdscr, true);                                     

    while (game_over) {
        printf("\033c");
        //char control = getchar();
        //time = set_game_speed(control, &game_over, time);
        usleep(time * 1000);
        //clear();
        update_matrix(matrix_1, matrix_2);
        if (is_apocalipsis(matrix_1, matrix_2))
            game_over = 0;
        swap_matrix(matrix_1, matrix_2);
    }
//  endwin();
    for (int i = 0; i < WIDTH; i++)
        free(matrix_1[i]);
    free(matrix_1);    

    for (int i = 0; i < WIDTH; i++)
        free(matrix_2[i]);
    free(matrix_2);

    printf("\033c");    
    printf("GAME OVER!!!\n");

    return 0;
}

int is_apocalipsis(int **matrix_1, int **matrix_2){
    int sum = 0;
    int count = 0;
    for (int i = 0; i < WIDTH; i++) {
        for (int j = 0; j < LEIGHT; j++) {
            sum += matrix_1[i][j];
            if (matrix_1[i][j] == matrix_2[i][j]) count++;
        }
        
    }
    return sum == 0 || count == 2000;    
}

void input_matrix(int **matrix) {
    for (int i=0; i < WIDTH; i++){
        for (int j = 0; j < LEIGHT; j++) {
            scanf("%d", &matrix[i][j]);
        }
    }
}

void update_matrix(int **matrix_1, int **matrix_2) {
    for (int i = 0; i < WIDTH; i++){
        for (int j = 0; j < LEIGHT; j++) {
            matrix_2[i][j] = gods_providence(count_neighbors(matrix_1, i, j), matrix_1[i][j]);
            if (matrix_2[i][j] == 1)
                printf("X");
            else    
                printf(" ");    
        }
        printf("\n");
    }
}

int set_game_speed(char control, int *game_over, int time) {
    switch (control) {
        case '1' : time = 1000; break;
        case '2' : time = 500; break;
        case '3' : time = 100; break;
        case 'q' : *game_over = 0; break;
    }
    return time;        
}

int count_neighbors(int **matrix_1, int i, int j) {
    int sum = 0;

    int i_minus = i - 1, j_minus = j - 1, i_plus = i + 1, j_plus = j + 1;

    if (i_minus < 0) i_minus = WIDTH - 1;
    if (j_minus < 0) j_minus = LEIGHT - 1;
    if (i_plus > WIDTH - 1) i_plus = i_plus % WIDTH;
    if (j_plus > LEIGHT - 1) j_plus = j_plus % LEIGHT;

    sum += matrix_1[i_minus][j_minus];
    sum += matrix_1[i_minus][j];
    sum += matrix_1[i_minus][j_plus];
    sum += matrix_1[i][j_plus];
    sum += matrix_1[i_plus][j_plus];
    sum += matrix_1[i_plus][j];
    sum += matrix_1[i_plus][j_minus];
    sum += matrix_1[i][j_minus];

    return sum;
}

int gods_providence(int neighbors, int condition) {
    int dead_or_live;
    if ((neighbors == 2 || neighbors == 3) && condition == 1) 
        dead_or_live = 1;
    else if (neighbors == 3 && condition == 0) 
        dead_or_live = 1;
    else dead_or_live = 0;
    
    return dead_or_live;
}

void swap_matrix(int **matrix_1, int **matrix_2){
    for (int i = 0; i < WIDTH; i++){
        for (int j = 0; j < LEIGHT; j++) {
            matrix_2[i][j] = matrix_1[i][j];
        }
    }
}