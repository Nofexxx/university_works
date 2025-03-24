#include "index_first_negative.h"
#include "index_last_negative.h"
#include "multi_between_negative.h"

int multi_between_negative(int s[], int len)
{
    int i, k;
    int pr = 1;
    for(i = index_first_negative(s, len), k = index_last_negative(s, len); i < k; i++)
        pr *= s[i];
    return pr;
}