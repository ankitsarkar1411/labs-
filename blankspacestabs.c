#include <stdio.h>

void replaceSpacesAndTabs(const char *inputFile, const char *outputFile) {
    FILE *in = fopen(inputFile, "r");
    FILE *out = fopen(outputFile, "w");
    if (!in || !out) {
        printf("Error: Unable to open file.\n");
        return;
    }

    char c, prev = '\0';
    while ((c = fgetc(in)) != EOF) {
        if (c == ' ' || c == '\t') {
            if (prev != ' ') {
                fputc(' ', out);
            }
        } else {
            fputc(c, out);
        }
        prev = c;
    }

    fclose(in);
    fclose(out);
}

int main() {
    char inputFile[100], outputFile[100];
    printf("Enter the input file name: ");
    scanf("%s", inputFile);
    printf("Enter the output file name: ");
    scanf("%s", outputFile);

    replaceSpacesAndTabs(inputFile, outputFile);

    printf("Spaces and tabs replaced successfully.\n");
    return 0;
}
