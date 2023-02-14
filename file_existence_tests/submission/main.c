#include <stdio.h>

int main(void) {

	FILE *testTXT1 = fopen("test1.txt", "w+");
	fprintf(testTXT1, "test\n");
	fclose(testTXT1);

	FILE *testTXT2 = fopen("test2.txt", "w+");
	fprintf(testTXT2, "test\n");
	fclose(testTXT2);

	return 0;

}