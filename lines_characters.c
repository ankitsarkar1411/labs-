#include<stdio.h>
int main(){
 FILE *file;
 char ch;
 int lines=0,characters =0;
 file = fopen("trial.txt","r");
 if(file==NULL){
 printf("Could not open file");
 return 1;
 }
 while((ch=fgetc(file))!=EOF){
   characters++;
   if(ch=='\n'){
   lines++;
   }
   }
   fclose(file);
   printf("Number of lines :%d\n",lines);
   printf("Number of characters :%d\n",characters);
   return 0;
   }
 
