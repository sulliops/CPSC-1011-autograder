#include <stdio.h>
#include <string.h>

int main(int argc, char **argv) {

    if (argc > 1) {

        fprintf(stdout, "Testing only stdout with no input...\n");
        
        return 0;

    }
    
    fprintf(stdout, "Autograder test program...\n\n");

    fprintf(stdout, "Enter an input (1, 2, or 3): ");
    int input;
    fscanf(stdin, "%d", &input);

    while (input != 1 && input != 2 && input != 3) {

        fprintf(stderr, "Invalid input. Try again (1, 2, or 3): ");
        fscanf(stdin, "%d", &input);

    }

    if (input == 1) {

        fprintf(stdout, "\nYou chose input 1.\n");

    } else if (input == 2) {

        fprintf(stdout, "\nYou chose input 2.\n");

    } else if (input == 3) {

        fprintf(stdout, "\nYou chose input 3.\n");

    }

    fprintf(stdout, "All done!\n");

    return 0;

}