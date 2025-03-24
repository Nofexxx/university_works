#include <stdlib.h>
#include <stdio.h>
#include <string.h>


// Описание структуры MusicalComposition
typedef struct MusicalComposition
{
    char* name;
    char* author;
    int year;

    struct MusicalComposition* next;
    struct MusicalComposition* previous;
} MusicalComposition;

// Создание структуры MusicalComposition

MusicalComposition* createMusicalComposition(char* name, char* author,int year)
{
    MusicalComposition* newMusicalComposition = (MusicalComposition*)malloc(sizeof(MusicalComposition));
    newMusicalComposition->name = name;
    newMusicalComposition->author = author;
    newMusicalComposition->year = year;
    newMusicalComposition->previous = newMusicalComposition->next = NULL;
    return newMusicalComposition;
}

// Функции для работы со списком MusicalComposition

MusicalComposition* createMusicalCompositionList(char** array_names, char** array_authors, int* array_years, int n);

void push(MusicalComposition* head, MusicalComposition* element);

void removeEl(MusicalComposition* head, char* name_for_remove);

int count(MusicalComposition* head);

void print_names(MusicalComposition* head);


int main(){
    int length;
    scanf("%d\n", &length);

    char** names = (char**)malloc(sizeof(char*)*length);
    char** authors = (char**)malloc(sizeof(char*)*length);
    int* years = (int*)malloc(sizeof(int)*length);

    for (int i=0;i<length;i++)
    {
        char name[80];
        char author[80];

        fgets(name, 80, stdin);
        fgets(author, 80, stdin);
        fscanf(stdin, "%d\n", &years[i]);

        (*strstr(name,"\n"))=0;
        (*strstr(author,"\n"))=0;

        names[i] = (char*)malloc(sizeof(char*) * (strlen(name)+1));
        authors[i] = (char*)malloc(sizeof(char*) * (strlen(author)+1));

        strcpy(names[i], name);
        strcpy(authors[i], author);

    }
    MusicalComposition* head = createMusicalCompositionList(names, authors, years, length);
    char name_for_push[80];
    char author_for_push[80];
    int year_for_push;

    char name_for_remove[80];

    fgets(name_for_push, 80, stdin);
    fgets(author_for_push, 80, stdin);
    fscanf(stdin, "%d\n", &year_for_push);
    (*strstr(name_for_push,"\n"))=0;
    (*strstr(author_for_push,"\n"))=0;

    MusicalComposition* element_for_push = createMusicalComposition(name_for_push, author_for_push, year_for_push);

    fgets(name_for_remove, 80, stdin);
    (*strstr(name_for_remove,"\n"))=0;

    printf("%s %s %d\n", head->name, head->author, head->year);
    int k = count(head);

    printf("%d\n", k);
    push(head, element_for_push);

    k = count(head);
    printf("%d\n", k);

    removeEl(head, name_for_remove);
    print_names(head);

    k = count(head);
    printf("%d\n", k);

    for (int i=0;i<length;i++){
        free(names[i]);
        free(authors[i]);
    }
    free(names);
    free(authors);
    free(years);

    return 0;

}

MusicalComposition* createMusicalCompositionList(char** array_names, char** array_authors, int* array_years, int n)
{
    MusicalComposition* head = createMusicalComposition(array_names[0], array_authors[0], array_years[0]);
    MusicalComposition* buffer = head;

    for(int i = 1; i < n; i++)
    {
        buffer->next = createMusicalComposition(array_names[i], array_authors[i], array_years[i]);
        buffer->next->previous = buffer;
        buffer = buffer->next;
    }
    head->previous = buffer;

    return head;
}

void push(MusicalComposition* head, MusicalComposition* element)
{
    MusicalComposition* buffer = head->previous;
    buffer->next = element;
    element->next = NULL;
    element->previous = buffer;
    head->previous = element;
}

void removeEl(MusicalComposition* head, char* name_for_remove)
{
    if(!strcmp(head->name, name_for_remove)){
        if(head->next != NULL){
            MusicalComposition* buffer = head->previous;
            strncpy(head->name, buffer->name, 80);
            strncpy(head->author, buffer->author, 80);
            head->year = buffer->year;
            buffer->next->previous = NULL;
            head->previous = buffer->previous;
            free(buffer);
        }
        else
            free(head);

        return;
    }

    MusicalComposition* buffer = head->next;
    while(strcmp(name_for_remove, buffer->name) && buffer->next != NULL)
        buffer = buffer->next;

    if(head == NULL)
        return;

    buffer->previous->next = buffer->next;
    buffer->next->previous = buffer->previous;
    free(buffer);
}

int count(MusicalComposition* head){
    MusicalComposition* buffer = head;
    int cnt;

    for(cnt = 0; buffer != NULL; cnt++)
        buffer = buffer->next;

    return cnt;
}

void print_names(MusicalComposition* head){
    MusicalComposition* buffer = head;

    while(buffer != NULL)
    {
        printf("%s\n", buffer->name);
        buffer = buffer->next;
    }
}
