#include "index_first_negative.h"

int index_first_negative(int s[], int len)
{
    int i;
    for(i = 0; i < len; i++)
        if(s[i] < 0)
            break;
    return i;
}