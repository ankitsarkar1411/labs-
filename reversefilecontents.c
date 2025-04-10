#include <stdio.h>
#include <stdlib.h>

void reverseFileContents(const char *sourceFile, const char *destFile) {
    FILE *src = fopen(sourceFile, "rb");
    FILE *dest = fopen(destFile, "wb");
    if (src == NULL || dest == NULL) {
        perror("Error opening file");
        return;
    }

    fseek(src, 0, SEEK_END);
    long fileSize = ftell(src);
    fseek(src, 0, SEEK_SET);

    char *buffer = (char *)malloc(fileSize);
    fread(buffer, 1, fileSize, src);

    for (long i = fileSize - 1; i >= 0; i--) {
        fputc(buffer[i], dest);
    }

    printf("Size of file: %ld bytes\n", fileSize);

    free(buffer);
    fclose(src);
    fclose(dest);
}

int main() {
    reverseFileContents("trial.txt", "output.txt");
    return 0;
}

