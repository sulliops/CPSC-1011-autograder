#include <stdio.h>
#include <assert.h>

void start(FILE* in);
void rcomment(FILE* in); 
void skipM_comment(FILE* in);
void skipS_comment(FILE* in);

int main(int argc, char **argv) {
    
    assert(argc == 2);
    
    FILE *input = fopen(argv[1], "r");

    assert(input != NULL);

    start(input);

    fclose(input);

    return 0;

}

void start(FILE* in) {

    int current;

    while (!feof(in)) {

        current = fgetc(in);

        if (current == '/') {

            rcomment(in);

        } else {

            fputc(current, stdout);

        }

    }

}

void rcomment(FILE* in) {

    int current;

    while (!feof(in)) {

        current = fgetc(in);

        if (current == '/') {

            skipS_comment(in);

        } else if (current == '*') {

            skipM_comment(in);

        } else {

            fputc(current, stdout);

        }

    }

}

void skipM_comment(FILE* in) {

    int current = fgetc(in);
    int next;

    while (!feof(in)) {

        current = fgetc(in);

        if (current == '*') {

            next = fgetc(in);

            if (next == '/') {

                next = fgetc(in);
                break;

            }

        }

    }

}

void skipS_comment(FILE* in) {

    int current = fgetc(in);

    while (!feof(in) && current != '\n') {

        current = fgetc(in);

    }

}