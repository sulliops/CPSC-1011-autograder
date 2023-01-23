int main(void) {

    char *str;

    str = "SIGBUS";

    *(str + 1) = 't';

    return 0;

}
