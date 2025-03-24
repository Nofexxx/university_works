#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

#define SENT 10

char** input(size_t* size_text);
char** del_duplicate(char** text, size_t* text_size);
void calc_time(char** text, size_t* text_size);
void transform_time(int num);
char** del_frst_word(char** text, size_t* text_size);
void output(char** text, size_t text_size);
char** del_len_sent(char** text, size_t* text_size);
char** sort(char** text, size_t* text_size);


int main(){
    int n;
    char** text;
    size_t text_size;
    printf("Введите текст.\n");
    text = input(&text_size);

    if(text == NULL){
        printf("Недостаточно памяти!\n");
	    return 1;
    }

    text = del_duplicate(text, &text_size);
    printf("Выберите одно из действий:\n");
    printf("0. Выйти из приложения\n");
    printf("1. Удалить первое слово в каждом предожении\n");
    printf("2. Удалить предложения в котором длины всех слов равны\n");
    printf("3. Отстортировать предложения по количеству строчных букв в нём\n");
    printf("4. Подсчёт времени в тектсе\n");
    printf("5. Распечатать текст\n");

    while(2){
        n = getchar();
	    switch(n){
        case '0':
	            printf("Выхожу из приложения\n");
		        return 0;
	    case '1':
		        printf("Удаляю первое слово в каждом предложении:\n");
		        text = del_frst_word(text, &text_size);
		        output(text, text_size);
		        break;
	    case '2':
		        printf("Удаляю предложения длины слов которых равны:\n");
		        text = del_len_sent(text, &text_size);
		        output(text, text_size);
		        break;
	    case '3':
		        printf("Сортирую предложения по у меньшению количства строчных букв в нём:\n");
		        text = sort(text, &text_size);
		        output(text, text_size);
	            break;
	    case '4':
		        printf("Подсчитываю время в тексте:\n");
		        calc_time(text, &text_size);
		        break;
	    case '5':
		        printf("Распечатываю текст:\n");
	            output(text, text_size);
		        break;
        default:
			    printf("Такая операция неизвестна. Выберите одно из предложенных значений.\n");
			    break;
	    }
    }
    for(int j = 0; j < text_size; j++){
        free(text[j]);
        free(text);
    }
    return 0;
}

char** input(size_t* size_text){
    char** text;
    char* sentence;
    int i = 0;
    int size_sentence = 1;
    size_t text_size = 0;

    sentence = (char*)malloc(sizeof(char)); //выделение памяти под перый символ предложения
    text = (char**)malloc(sizeof(char*));   //выделени памяти под первок предложение
    sentence[i] = getchar();

    while (sentence[i] != '\n'){

        if(sentence[i] == '.'){
            text_size++;
	        text = (char**)realloc(text, text_size * sizeof(char*));
	        text[text_size - 1] = (char*)malloc((i + 2) * sizeof(char));
	        memcpy(text[text_size - 1], sentence, (i + 2) * sizeof(char));
	        text[text_size - 1][i + 1] = '\0';
	        i = 0;
            sentence[i] = getchar();
	        continue;
	    }
            i++;

	    if(i >= (size_sentence - 2)){    //условие для увелечении памяти
            size_sentence += SENT;
	        char* temp;
            temp = (char*)realloc(sentence, size_sentence * sizeof(char));

	        if(temp == NULL){
                for(int j = 0; j < text_size; j++){
                    free(text[j]);
		            text[j] = NULL;
		        }
	            free(text);
		        text = NULL;
		        return text;
	        }
	        sentence = temp;
	    }
	    sentence[i] = getchar();
    }
    free(sentence);
    *size_text = text_size;
    return text;
}

char** del_duplicate(char** text, size_t* text_size){       //удаляет дупликаты в тексте
    for(int a = 0; a < (*text_size - 1); a++){
        for(int b = a + 1; b < *text_size; b++){
            if(strcasecmp(text[a], text[b]) == 0){ //сравниваем повторяющееся предложения без учёта регистра
                free(text[b]);
		        memmove(&text[b], &text[b + 1], (*(text_size)-b - 1) * sizeof(char*));
		        *text_size -= 1;
		        b--;
	        }
	    }
    }
    text = realloc(text, *text_size * sizeof(char*));
    return text;
}

void transform_time(int num){   //переводит секунду в часы, минуты и секунды
    int all_sec = num;
    int sec_in_min = 60;
    int sec;
    int hour;
    int min = all_sec / sec_in_min;
    sec = all_sec % sec_in_min;
    if(min >= 60){
        hour = min/ sec_in_min;
        min = hour % sec_in_min;
        sec = min % 60;
    }
    printf("Hour: %d Min: %d Sec: %d \n", hour, min, sec);

}

void calc_time(char** text, size_t* text_size){     //ищет конструкции вида "числоsec" и переводит в число
    char* sentence;
    char* time_string = (char*)malloc(sizeof(char));
    int num = 0;
    int c = 0;
    for(int i = 0; i < *text_size; i++){
        sentence = text[i];
	    time_string = (char*)realloc(time_string, (strlen(text[i]) + 1) * sizeof(char));
        strcpy(time_string, text[i]);
	    for(int k = 0; k < strlen(text[i]); k++){
            if (isdigit(time_string[k])){
                if(time_string[k + 3] == 'c' || time_string[k + 4] == 'c'){
		            memmove(&time_string[c], &time_string[c + k], strlen(text[i]) * sizeof(char));
                    num += atoi(time_string);
		        }
	        }

        }
    }
    transform_time(num);
    free(time_string);
}

char** del_frst_word(char** text, size_t* text_size){     //удаляет первое слово в каждом предложении
    char* sentence;
    for(int i = 0; i < *text_size; i++){
        sentence = (char*)malloc((strlen(text[i]) + 1) * sizeof(char));
        sentence = text[i];
	    for(int j = 0, k = 0; j < strlen(text[i]); j++){
	        if(sentence[j] == ' ' || sentence[j] == '.'){
                memmove(&sentence[k], &sentence[j + 1], (strlen(text[i]) - j) * sizeof(char));
		        if(sentence[j] == '\0'){
		            free(text[i]);
                    memmove(&text[i], &text[i + 1], (*(text_size) - i - 1) * sizeof(char*));
                    *text_size -= 1;
                    i--;
                    continue;
        	    }
	        }
	    }
    }
    text = (char**)realloc(text, *text_size * sizeof(char*));
    return text;
}

void output(char** text, size_t text_size){
    for(int i = 0; i < text_size; i++)
        printf("%s", text[i]);
    printf("\n");
}

char** del_len_sent(char** text, size_t* text_size){    //удаляет все предложени в котром длины всех слов равны
    char *sep;
    char** word_arr = (char**)malloc(sizeof(char*));
    char* sentence;
//    int cnt_word = 0;
    for(int i = 0; i < *text_size; i++){
        int cnt = 1, cnt_word = 0;
        strcpy(sentence, text[i]);
        for(sep = strtok(sentence, " ,."); sep; sep = strtok(NULL, " ,.")){
            word_arr[cnt_word++] = sep;
        }
        for(int k = 1; k < cnt_word; k++){
            if(strlen(word_arr[0]) == strlen(word_arr[k])){
                cnt++;
                if(cnt == cnt_word){
                    free(text[i]);
                    memmove(&text[i], &text[i + 1], (*(text_size)- k) * sizeof(char*));
                    *text_size -= 1;
                    i--;
                }
            }
        }
    }
    free(word_arr);
    text = (char**)realloc(text, *text_size * sizeof(char*));
    return text;
}

int count_alph(char* sent){    //подсчитывает все строчные буквы в предложении
    int count = 0;
    char* copy = strdup(sent);
    for(int i = 0; i < strlen(copy); i++){
        if(islower(copy[i]))
	        count++;
    }
    free(copy);
    return count;
}

int comp(const void* a, const void* b){
    char** aa =(char**)a;
    char** bb = (char**)b;

    int len_sent1 = count_alph(*aa);
    int len_sent2 = count_alph(*bb);

    if(len_sent1 < len_sent2)
        return 1;
    if(len_sent1 > len_sent2)
        return -1;
    return 0;
}

char** sort(char** text, size_t* text_size){
    qsort(text, *text_size, sizeof(char*), comp);
    return text;
}