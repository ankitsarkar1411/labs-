#include <stdio.h>
#include <stdlib.h>

void mergeFiles(const char *file1, const char *file2, const char *resultFile) {
    FILE *f1 = fopen(file1, "r");
    FILE *f2 = fopen(file2, "r");
    FILE *result = fopen(resultFile, "w");
    
    if (f1 == NULL || f2 == NULL || result == NULL) {
        perror("Error opening file");
        exit(EXIT_FAILURE);
    }

    char line1[256], line2[256];
    while (fgets(line1, sizeof(line1), f1) != NULL) {
        fputs(line1, result);
        if (fgets(line2, sizeof(line2), f2) != NULL) {
            fputs(line2, result);
        }
    }

    while (fgets(line2, sizeof(line2), f2) != NULL) {
        fputs(line2, result);
    }

    fclose(f1);
    fclose(f2);
    fclose(result);
}

int main() {
    mergeFiles("trial.txt", "output.txt", "result.txt");
    return 0;
}

