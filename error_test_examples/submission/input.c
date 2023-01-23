#include <stdio.h>

int main()
{
    //comment 1
    int a = 0;
    int b = 5; 

    /*
    //comment 2
    //comment 2 cont
    */

   /* comment 3 **********/
    for(a = 0; a < 5; a++)
    {
        /*
        comment 4
        */
        printf("%d\n", b);
        b++;
        //comment 5 /* comment 5 cont */
    }
    //comment 6
    return 0;
}
