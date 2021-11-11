#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) 
{
    if(argv[1])
    {
        int i = 0;
         while(argc)
        {
            if(i != 0) printf("Nick is a(n) %s\n",argv[i]);
            i++;
            argc--;
        }
    } else {
        printf("Nick is still a twazzick\n");
    }
    return 0;
}
