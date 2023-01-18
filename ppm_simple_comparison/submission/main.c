#include <stdio.h>

int main (void){
	
	int width, j, k = 0;  // k is used for the array

	fprintf(stderr, "Flag of Ireland\n\n");

	fprintf(stderr, "Width of flag: ");
	scanf("%d", &width);

	int height = width / 2;
	fprintf(stderr, "\n\nMaking the flag with width %d & height %d...\n", width, height);

	unsigned int flag[width * height * 3];

	fprintf(stdout, "P3\n");
	fprintf(stdout, "%d %d %d\n", width, height, 255);

	for (int i = 0; i < height; i++) {
		
		for (j = 0; j < width / 3; j++) {
			
			flag[k++] = 0;
			flag[k++] = 128;
			flag[k++] = 0;

		}

		for (; j < width * 2 / 3; j++) {
			
			flag[k++] = 255;
			flag[k++] = 255;
			flag[k++] = 255;

		}

		for (; j < width; j++) {

			flag[k++] = 255;
			flag[k++] = 165;
			flag[k++] = 0;

		}

	}

	for (int i = 0; i < height * width * 3; i += 3) {

		fprintf(stdout, "%d %d %d\n", flag[i], flag[i+1], flag[i+2]);

	}

	return 0;
	
}