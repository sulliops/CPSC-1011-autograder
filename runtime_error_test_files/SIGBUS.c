int main(void) {

    char *str;

    str = "SIGILL";

    *(str + 1) = 't';

    return 0;

}