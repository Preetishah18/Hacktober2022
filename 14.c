#include<stdio.h>
#include<conio.h>

int main(){
//write a program to find the factorial of number
int num,factorial =1;
printf("Enter the number to find the factorial\n");
scanf("%d",&num);
for (int i = 1; i <= num; i++)
{
    factorial= factorial*i;
}
printf("The factorial of %d is %d ",num,factorial);
return 0;
}