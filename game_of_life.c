
#include <stdio.h>
#include <stdlib.h>

// Устанавливает позицию курсора в терминале
void setCursorPos(int x, int y) {
    printf("\033[%d;%dH", y, x);
}

// Рисует поле с границами
void draw_board(int height, int width) {
    // Выделяем память для поля
    char **field = (char **)malloc(height * sizeof(char *));
    for (int i = 0; i < height; i++) {
        field[i] = (char *)malloc(width * sizeof(char));
    }

    // Заполняем поле
    for (int y = 0; y < height; y++) {
        for (int x = 0; x < width; x++) {
            if (y == 0 || y == height - 1) {
                // Верхняя и нижняя границы
                field[y][x] = '-';
            } else if (x == 0 || x == width - 1) {
                // Левая и правая границы
                field[y][x] = '|';
            } else {
                // Внутренняя часть поля
                field[y][x] = ' ';
            }
        }
    }

    // Выводим поле на экран
    for (int y = 0; y < height; y++) {
        for (int x = 0; x < width; x++) {
            printf("%c", field[y][x]);
        }
        printf("\n");
    }

    // Освобождаем память
    for (int i = 0; i < height; i++) {
        free(field[i]);
    }
    free(field);
}

void draw_life(int a, int b, int**matrix){
    for (int y = 0; y < b; y++) {
        for (int x = 0; x < a; x++) {
            printf("%d", matrix[y][x]); // Выводим числа
            
        }
        setCursorPos(2, y+3);
    }
}

int neighbour_sum(int** matrix, int i, int a, int x, int b){
    int sum = 0;

    int prev_row = (i == 0) ? b - 1 : i - 1; // Сосед сверху
    int next_row = (i == b - 1) ? 0 : i + 1; // Сосед снизу
    int prev_col = (x == 0) ? a - 1 : x - 1; // Сосед слева
    int next_col = (x == a - 1) ? 0 : x + 1; // Сосед справа

    sum += matrix[prev_row][prev_col]; // Верхний левый
    sum += matrix[prev_row][x];        // Верхний
    sum += matrix[prev_row][next_col]; // Верхний правый
    sum += matrix[i][prev_col];        // Левый
    sum += matrix[i][next_col];        // Правый
    sum += matrix[next_row][prev_col]; // Нижний левый
    sum += matrix[next_row][x];        // Нижний
    sum += matrix[next_row][next_col]; // Нижний правый

    return 0;
}

void change_life(int**matrix, int a, int b){
    int **matrix_b = (int **)calloc(b, sizeof(int *));
    for (int i = 0; i < b; i++) {
        matrix_b[i] = (int *)calloc(a, sizeof(int));
        for (int x = 0; x < b; x++) {
            matrix_b[i][x] = matrix[i][x];
        }
    }

    for (int i = 0; i < b; i++) {
        for (int x = 0; x < b; x++) {
            if (matrix_b[i][x]==0){
                if(neighbour_sum(matrix, i, a, x, b) == 3){
                    matrix[i][x] = 1;
                }
            }
            else{
                if(neighbour_sum(matrix, i, a, x, b) <2){
                    matrix[i][x] = 0;
                }
                else if(neighbour_sum(matrix, i, a, x, b) >3){
                    matrix[i][x] = 0;
                }

            }
        }
    }


    
    for (int i = 0; i < b; i++) {
        free(matrix_b[i]);
    }
    free(matrix_b);

}

int main() {

    int a = 80; // Ширина поля
    int b = 25; // Высота поля
    int sleep_val = 1000;

    int **matrix = (int **)calloc(b, sizeof(int *));
    for (int i = 0; i < b; i++) {
        matrix[i] = (int *)calloc(a, sizeof(int));

    }

    printf("\33[0d\33[2J");
    setCursorPos(0, 1);
    draw_board(b+2, a+2);
    while(1){    
        setCursorPos(2, 2);
        draw_life(a, b, matrix);
        change_life(matrix, a, b);
        // sleep(sleep_val);
        setCursorPos(1,30);
    }
    

    

    
    for (int i = 0; i < b; i++) {
        free(matrix[i]);
    }
    free(matrix);

    return 0;
}