#include <stdio.h>
#include <stdlib.h>
#include <termios.h>
#include <signal.h>
#include <unistd.h>
#include <time.h>
#include <string.h>

#define MAX_LENGTH 500
#define HEIGHT 20
#define WIDTH 85
#define BILLION 1000000000

enum {STOP = 0, UP, DOWN, RIGHT, LEFT};

const char wall = '#';
const char snake_el = '*';
const char apple = '@';

const int height = HEIGHT - 3;
const int width = WIDTH - 2;

unsigned char play_field[HEIGHT][WIDTH];
sig_atomic_t run = 1;
int apl_cnt = 0;
int dir = STOP;
int new_dir;

typedef struct Coord{
    int col;
    int row;
}Coord;

Coord snake[MAX_LENGTH];
int snake_size = 1;
int snake_buff = 4;
int score = 0;

void sighandler(int sig){
    run = 0;
    signal(sig, sighandler);
}

struct termios saved_settings;

void reset_terminal_settings(){ //Перевод терминала в канонический режим

    printf("\x1b[?25h");
    tcsetattr(STDIN_FILENO, TCSANOW, &saved_settings);
    system("clear");
}


void set_terminal_settings(){ //Перевод работы терминала в не канонический режим
    struct termios new;

    //Сохранием настройки терминала
    tcgetattr(STDIN_FILENO, &saved_settings);

    tcgetattr(STDIN_FILENO, &new);
    new.c_lflag &= ~(ICANON | ECHO);
    new.c_cc[VMIN] = 0;
    new.c_cc[VTIME] = 0;
    tcsetattr(STDIN_FILENO, TCSAFLUSH, &new);
    printf("\x1b[?25l");
    system("clear");
    atexit(reset_terminal_settings);
}


void init_field(){

    for(int i = 0; i < height; i++)
        for(int j = 0; j < width; play_field[i][j++] = ' ');

}

void create_field(){
    printf("\x1b[H"); //Передвигает курсор на (0;0)

    for(int i = width + 2; i; i--)
        putchar(wall);
    putchar('\n');

    for(int i = 0; i < height; i++){
        putchar(wall);
        for(int j = 0; j < width; j++)
            putchar(play_field[i][j]);

        putchar(wall);
        putchar('\n');
    }

    for(int i = 0; i < width + 2; i++)
        putchar(wall);
    putchar('\n');

    printf("Score: %d\n", score);
}

Coord get_random_pos(){
    Coord result;

    while(1){
        result.row = rand() % height;
        result.col = rand() % width;
        if(play_field[result.row][result.col] == ' ')
            break;
    }

    return result;
}

void input(){
    int input;

    if(read(STDIN_FILENO, &input, 3)){
        switch (input) {
            case 'w': case 'W': dir = UP; break;
            case 's': case 'S': dir = DOWN; break;
            case 'a': case 'A': dir = LEFT; break;
            case 'd': case 'D': dir = RIGHT; break;
            case 'b': case 'B': reset_terminal_settings(); system("clear"); exit(0); break;
        }
    }
}

void change_head(){
    switch(dir){
        case UP:
            snake[0].row--;
            break;
        case DOWN:
            snake[0].row++;
            break;
        case LEFT:
            snake[0].col--;
            break;
        case RIGHT:
            snake[0].col++;
    }
}

void logic(){
    if(snake[0].row < 0 || snake[0].col < 0
            || snake[0].row > height - 1 || snake[0].col > width - 1) {
        reset_terminal_settings();
        system("clear");
        printf("Game over! You hit the wall!\n");
        printf("Pleas press any button to leave\n");
        getchar();
        exit(0);
    }

    if(play_field[snake[0].row][snake[0].col] != ' '
        && play_field[snake[0].row][snake[0].col] != apple){
        reset_terminal_settings();
        system("clear");
        printf("Game over! You eat your self!\n");
        printf("Pleas press any button to leave\n");
        getchar();
        exit(0);
    }
}

void gen_food()
{
    Coord random_pos = get_random_pos();
    play_field[random_pos.row][random_pos.col] = apple;
}

void snake_move(){
    memmove(&snake[1], &snake[0], sizeof(Coord) * snake_size);
    change_head();
    logic();

    if(play_field[snake[0].row][snake[0].col] == apple){
        snake_size++;
        gen_food();
        score++;
    }

    play_field[snake[0].row][snake[0].col] = snake_el;
    if(snake_size < snake_buff)
        snake_size++;
    else
        putchar(play_field[snake[snake_size].row][snake[snake_size].col] = ' ');
}

void spawn_snake(){
    snake[0] = get_random_pos();
    play_field[snake[0].row][snake[0].col] = snake_el;
}

int main(){
    set_terminal_settings();
    signal(SIGINT, sighandler);

    init_field();
    spawn_snake();
    create_field();
    gen_food();

    while(run){
        if(dir != STOP){
            snake_move();
            create_field();
        }

        input();
        usleep(150000);
        input();
    }
    return 0;
}