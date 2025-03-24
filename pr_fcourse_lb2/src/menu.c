#include <stdio.h>
#include <stdlib.h>

#include "index_first_negative.h"
#include "index_last_negative.h"
#include "multi_between_negative.h"
#include "multi_before_and_after_negative.h"

#define MAX 20

int main()
{
    int arr[MAX];
    int i = 0;
    int n;
    scanf("%d", &n);
    while (getchar() != '\n' && i < MAX){
        scanf("%d", &arr[i]);
        i++;
    }
    switch(n)
    {
        case 0: printf("%d\n", index_first_negative(arr, i));
                break;
        case 1: printf("%d\n", index_last_negative(arr, i));
                break;
        case 2: printf("%d\n" ,multi_between_negative(arr, i));
                break;
        case 3: printf("%d\n", multi_before_and_after_negative(arr, i));
                break;
        default: puts("Данные некорректны");
                 break;
    }
    return 0;
}