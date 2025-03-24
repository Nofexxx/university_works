#include "index_first_negative.h"
#include "index_last_negative.h"
#include "multi_before_and_after_negative.h"

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