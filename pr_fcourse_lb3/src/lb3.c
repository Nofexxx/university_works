#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

#define BUF_INIT_SIZE 32
#define BUF_INC_SIZE 16

int main()
{
	size_t buf_sz = BUF_INIT_SIZE;
	char* buf = malloc(sizeof(char) * buf_sz);
	char* buf_pt;

	int c;
	int loop = 1, sent_loop;
	size_t uppercase_cnt;

	size_t snt_cnt_bef = 0, snt_cnt_aft = 0;
	while(loop)
	{
		buf_pt = buf;

		while( (c = getchar()) == ' ' || c == '\t') ;

		sent_loop = 1;
		uppercase_cnt = 0;
		while(sent_loop)
		{
			switch(c)
			{
				case '.': case ';': case '?': case '!':
					*buf_pt = c;
					++buf_pt;
					if(buf_pt >= buf + buf_sz){
						buf_sz += BUF_INC_SIZE;
						size_t buf_pt_diff = buf_pt - buf;
						buf = realloc(buf, sizeof(char) * buf_sz);
						buf_pt = buf + buf_pt_diff;
					}
					*buf_pt = '\0';
					sent_loop = 0;
					printf("%s\n", buf);
					if(c == '!'){
						loop = 0;
						--snt_cnt_bef;
						break;
					}
					++snt_cnt_aft;
					break;
				default:
					if(isupper(c)) ++uppercase_cnt;
					if(uppercase_cnt > 1){
						sent_loop = 0;
						while( (c = getchar()) != '.' && c != ';' && c != '?' && c != '!') ;
					}
					*buf_pt = c;
					++buf_pt;
					if(buf_pt >= buf + buf_sz){
						buf_sz += BUF_INC_SIZE;
						size_t buf_pt_diff = buf_pt - buf;
						buf = realloc(buf, sizeof(char) * buf_sz);
						buf_pt = buf + buf_pt_diff;
					}
					c = getchar();
					break;
			}
		}
		++snt_cnt_bef;
	}
	printf("Количество предложений до %u и количество предложений после %u\n", snt_cnt_bef, snt_cnt_aft);
	free(buf);
	return 0;
}