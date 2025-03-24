#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_SIZE 1001
#define WORD_SIZE 31

int cmp(const void* a, const void* b){
    return (strcmp(*(char**)a, *(char**)b));
}

int main()
{
    char text[MAX_SIZE];
    char* word_arr[300];
    char* sep;
    char* key = (char*)malloc(WORD_SIZE *sizeof(char));
    char* item;
    int wsize = 0;

    fgets(text, MAX_SIZE, stdin);
    if(text[strlen(text) - 1] == '\n')
        text[strlen(text) - 1] = '\0';

    fgets(key, WORD_SIZE, stdin);
    if(key[strlen(key) - 1] == '\n')
        key[strlen(key) - 1] = '\0';

    for(sep = strtok(text, " ."); sep; sep = strtok(NULL, " .")){
        word_arr[wsize++] = sep;
    }
    qsort(word_arr, wsize, sizeof(char*), cmp);

    item = (char*)bsearch(&key, word_arr, wsize, sizeof(char*), cmp);
    if(item != NULL)
        printf("exists\n");
    else
        printf("doesn't exist\n");

    free(key);
    return 0;
}