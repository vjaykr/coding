#include <stdio.h>

int main()
{
    printf("Hello, World!\n");
    printf("this is my revision of c \nin programming\n");// this is a comment text
  
    int a = 20;
    int b = 30;
    
    printf("the value of c is %i",b-a);
    char data ="this is a character";
    printf("the value of c is %c",data);


    if(a>b){
        printf("a is greater than b");
    }

    else{
        printf("b is greator than a\n");
    }

    int code = scanf("%d",&a);

    switch (code)
    {
    case 1 :
        printf("monday");
        break;
    
    case 2 :
        printf("tuesday");
        break;
    
    }


    for (int i = 0; i < 10; i++)
    {
        printf("the value of i is %d\n",i);
    }

    
    int mynum[] = {2,3,5,6,8,345,56,7,788,9,2};
     printf("size of mynum is %lu\n",sizeof(mynum));

    for (int i = 0; i < 10; i++){
       U7Y6T5R4E3W2SQA  
        printf("the value of mynum[%d] is %d\n",i,mynum[i]);
    }

    FILE *file;
    file = fopen("output.txt", "w");

    if (file == NULL) {
        printf("Error opening file!\n");
        return 1;
    }

    fprintf(file, "Hello, World!\n");
    fprintf(file, "This is my revision of C in programming\n");

    fprintf(file, "The value of c is %i\n", b - a);
    fprintf(file, "The value of data is %c\n", data);

    if (a > b) {
        fprintf(file, "a is greater than b\n");
    } else {
        fprintf(file, "b is greater than a\n");
    }

    for (int i = 0; i < 10; i++) {
        fprintf(file, "The value of i is %d\n", i);
    }

    fprintf(file, "Size of mynum is %lu\n", sizeof(mynum));

    for (int i = 0; i < 10; i++) {
        fprintf(file, "The value of mynum[%d] is %d\n", i, mynum[i]);
    }

    fclose(file);


}

