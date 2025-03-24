#include <stdio.h>
#include <stdlib.h>
#define MAX 20   //Максимальный размер массива

//Индекс первого отрицательного элемента
int index_first_negative(int s[], int len)
{
    int i;
    for(i = 0; i < len; i++)
        if(s[i] < 0)
            break;
    return i;
}

//Индекс последнего отрицательного элемента
int index_last_negative(int s[], int len)
{
    int i;
    for(i = (len - 1); i >= 0; i--)
        if(s[i] < 0)
            break;
    return i;
}

//Произведение элементов массива от 1-го отрицательного элемента(включая элемент) до последнего(не включая элемент)
int multi_between_negative(int s[], int len)
{
    int i, k;
    int pr = 1;
    for(i = index_first_negative(s, len), k = index_last_negative(s, len); i < k; i++)
        pr *= s[i];
    return pr;

}

//Произведение элементов массива до 1-го отрицательного элемента(не включая элемент) до последнего(включая элемент)
int multi_before_and_after_negative(int s[], int len)
{
    int i, k, a;
    int pr = 1;
    i = index_first_negative(s, len);
    k = index_last_negative(s, len);
    for(a = 0; a < i; a++)
        pr *= s[a];
    for(a = k; a < len; a++)
        pr *= s[a];
    return pr;
}

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