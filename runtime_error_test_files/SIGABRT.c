// C program to demonstrate segmentation
// fault when array out of bound is accessed.
 
#include <stdio.h>
 
int main(void)
{
   int arr[2];
   
   arr[3] = 10;  // Accessing out of bound
   
   return (0);
}
 
// This code is contributed by sarajadhav12052009