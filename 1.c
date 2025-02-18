
char *s21_strchr(char *str, int symbol);
char *s21_strstr(char *str_1, char *str_2);

char *s_21strch(char *str, int symbol){
    
    char c = (char)symbol; 
    if (c != '\0') {
        while (*str != '\0') {
            if (*str == c) {
                return str;
            }
            str++;
        }
    }
    return NULL;
}


char *str = "Stepik the best!";
int symbol = 'b';
s21_strch_test(str, symbol, "best!");
str = "Stepik the best!";
symbol = 'z';
s21_strch_test(str, symbol, NULL);
str3 = "";
symbol = 'a';
s21_strch_test(str, symbol, NULL);


void s21_strch_test(char *str, int symbol, char *expected_result) {
    char *result = s21_strch(str, symbol);

    
    if (result == NULL && expected_result == NULL) {
        printf("%s %c SUCCESS\n", str, symbol);
    } else if (result != NULL && expected_result != NULL && strcmp(result, expected_result) == 0) {
        printf("%s %c %s SUCCESS\n", str, symbol, result);
    } else {
        printf("%s %c %s %s FAIL\n",
               str, symbol, result ? result : "FAIL", expected_result ? expected_result : "FAIL");
    }
}


char *s21_strstr(char *str_1, char *str_2) {
    if (*str_2 == '\0') { 
        return str_1;
    }
    char *ptr_1 = str_1;
    char *ptr_2;
    while (*ptr_1 != '\0') {
        ptr_2 = str_2;
        while (*ptr_1 == *ptr_2 && *ptr_2 != '\0') {
            ptr_1++;
            ptr_2++;
        }
        if (*ptr_2 == '\0') {
            return ptr_1 - (ptr_2 - str_2);
        }
        ptr_1 = ptr_1 - (ptr_2 - str_2) + 1;
    }

    return NULL; 
}

 
char *str1 = "Stepik the best!";
char *str2 = "best";
s21_strstr_test(str1, str2, "best");
str1 = "Stepik the best!";
str2 = "planet";
test_s21_strstr(str1, str2, NULL);
str1 = "Stepik the best!";
str2 = ""; 
test_s21_strstr(str1, str2, "Stepik the best!");

void s21_strstr_test(char *str_1, char *str_2, const char *expected_result) {
    char *result = s21_strstr(str_1, str_2);
    if (result == NULL && expected_result == NULL) {
        printf("%s %s FAIL\n", str_1, str_2);
    } else if (result != NULL && expected_result != NULL && s21_strcmp(result, expected_result) == 0) {
        printf("%s %s %s SUCCESS\n", str_1, str_2, result);
    } else {
        printf("%s %s %s FAIL Expected: %s\n",
               str_1, str_2, result ? result : "FAIL", expected_result ? expected_result : "FAIL");
    }
}

