#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

#define MAX_EXCUSES 100
#define MAX_EXCUSE_LENGTH 100

int random_number(int max) {
	    return (double)rand() / RAND_MAX * max;
}

int main() {
	    char rainbow[] = "\xF0\x9F\x8C\x88";
	        char excuses[MAX_EXCUSES][MAX_EXCUSE_LENGTH];
		    int excuse_count = 0;

		        FILE *fp = fopen("excuses.txt", "r");
			    if (fp == NULL) {
				            printf("Could not open file excuses.txt");
					            return 1;
						        }

			        char line[MAX_EXCUSE_LENGTH];
				    while (fgets(line, sizeof(line), fp) != NULL) {
					            strncpy(excuses[excuse_count++], line, strlen(line) - 1);
						        }
				        fclose(fp);

					    srand(time(NULL));
					        int random_excuse = random_number(excuse_count);
						    printf("%s   %s\n", rainbow, excuses[random_excuse]);

						        return 0;
}

