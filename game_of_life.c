#include <ncurses.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

void draw_life(int a, int b, int **matrix);
int neighbour_sum(int **matrix, int current_row, int columns, int current_column, int rows);
void change_life(int **matrix, int a, int b);
void read_from_file(const char *filename, int **matrix);
void greeting(int **matrix);

int main() {
    int a = 80;
    int b = 25;
    int sleep_val = 512;

    int **matrix = (int **)calloc(b, sizeof(int *));
    for (int i = 0; i < b; i++) {
        matrix[i] = (int *)calloc(a, sizeof(int));
        for (int x = 0; x < a; x++) matrix[i][x] = 0;
    }

    greeting(matrix);
    // Инициализация ncurses
    initscr();
    // Включение неблокирующего режима
    nodelay(stdscr, TRUE);

    while (1) {
        draw_life(a, b, matrix);
        change_life(matrix, a, b);
        refresh();

        char ch = getch();
        if (ch == 'q' || ch == 'Q') break;
        if (ch == '+') sleep_val = (sleep_val > 100) ? sleep_val / 2 : 100;
        if (ch == '-') sleep_val *= 2;
        // Неблокирующая задержка
        napms(sleep_val);
    }

    endwin();
    return 0;
}

void draw_life(int a, int b, int **matrix) {
    for (int y = 0; y < b; y++) {
        for (int x = 0; x < a; x++) mvaddch(y, x, matrix[y][x] ? '@' : '.');
    }
}

int neighbour_sum(int **matrix, int current_row, int columns, int current_column, int rows) {
    int sum = 0;
    int prev_row = (current_row - 1 + rows) % rows;
    int next_row = (current_row + 1) % rows;
    int prev_col = (current_column - 1 + columns) % columns;
    int next_col = (current_column + 1) % columns;

    sum += matrix[prev_row][prev_col];
    sum += matrix[prev_row][current_column];
    sum += matrix[prev_row][next_col];
    sum += matrix[current_row][prev_col];
    sum += matrix[current_row][next_col];
    sum += matrix[next_row][prev_col];
    sum += matrix[next_row][current_column];
    sum += matrix[next_row][next_col];

    return sum;
}

void change_life(int **matrix, int a, int b) {
    int **matrix_b = (int **)calloc(b, sizeof(int *));
    for (int i = 0; i < b; i++) {
        matrix_b[i] = (int *)calloc(a, sizeof(int));
        for (int x = 0; x < a; x++) matrix_b[i][x] = matrix[i][x];
    }

    for (int i = 0; i < b; i++) {
        for (int x = 0; x < a; x++) {
            if (matrix_b[i][x] == 0) {
                if (neighbour_sum(matrix_b, i, a, x, b) == 3) matrix[i][x] = 1;
            } else {
                if (neighbour_sum(matrix_b, i, a, x, b) < 2)
                    matrix[i][x] = 0;
                else if (neighbour_sum(matrix_b, i, a, x, b) > 3)
                    matrix[i][x] = 0;
            }
        }
    }

    for (int i = 0; i < b; i++) free(matrix_b[i]);

    free(matrix_b);
}

void read_from_file(const char *filename, int **matrix) {
    FILE *file = fopen(filename, "r");
    if (file == NULL) {
        printf("Ошибка: не удалось открыть файл %s\n", filename);
        return;
    }

    int x, y;
    while (fscanf(file, "%d %d", &x, &y) == 2) {
        if (x >= 0 && x < 80 && y >= 0 && y < 25)
            // Устанавливаем клетку как живую
            matrix[y][x] = 1;
        else
            return;
    }

    fclose(file);
}

void greeting(int **matrix) {
    char str2[100];
    while (1) {
        int val;
        int coord_x;
        int coord_y;

        printf("Добро пожаловать в игру жизнь.\n");
        printf(" Изменение скорости + или -, выход из игры - q.\n");
        printf("Как хотите вводить начальное состояние:\n");
        printf("    1. Файл\n");
        printf("    2. Консоль\n");

        if (scanf("%d", &val)) {
            if (val == 1) {
                printf(" \nВведите название файла: ");
                if (scanf("%99s", str2)) {
                    read_from_file(str2, matrix);
                    return;
                }
            } else if (val == 2) {
                printf(" \nВведите координаты в консоль(введите некорректное значение для остановки): ");
                while (1) {
                    if (scanf("%d", &coord_x) && scanf("%d", &coord_y) && coord_x >= 0 && coord_x <= 80 &&
                        coord_y >= 0 && coord_y <= 25)
                        matrix[coord_y][coord_x] = 1;
                    else
                        return;
                }
            }
        } else
            while (getchar() != '\n');

        clear();
    }
}
