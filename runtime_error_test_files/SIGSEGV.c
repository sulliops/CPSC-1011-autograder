#include <stdio.h>
#include <stdlib.h>
#include <string.h>


int main() {

  int MAX_INPUT_SIZE = 200;
  volatile int running = 1;
  while(running) {

char input[MAX_INPUT_SIZE];
char *tokens[100];
const char* cmds[] = {"wait", "pwd", "cd", "exit"};
char *cmdargs[100];

printf("shell> ");
fgets(input, MAX_INPUT_SIZE, stdin);

//tokenize input string, put each token into an array
char *space;
space = strtok(input, " ");
tokens[0] = space;

int i = 1;
while (space != NULL) {
  space = strtok(NULL, " ");
  tokens[i] = space;
  ++i;
}

//copy tokens after first one into string
strcpy((char*)cmdargs, ("%s ",tokens[1]));
for (i = 2; tokens[i] != NULL; i++) {
  strcat((char*)cmdargs, " ");
  strcat((char*)cmdargs, tokens[i]);
}


//compare tokens[0] to list of internal commands
int isInternal = -1;
for (i = 0; i < 4; i++) {
  if (strcmp(tokens[0], cmds[i]) == 0) {
isInternal = i;
  }
}

char *wd[200];
switch(isInternal) {
case 0:
  //wait
  printf("WAIT \n");
  break;
case 1:
  //pwd
  printf("PWD \n");
  break;
case 2:
  //cd
  printf("CD \n");
  break;
case 3:
  //exit
  printf("EXIT \n");
  break;
case -1:
  //not internal command, continue
  break;
}


/*
for (i = 0; tokens[i] != NULL; i++) {
  printf("%s ", tokens[i]);
}
printf("\n");
*/
  }
}