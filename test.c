// calculate a area of a circle:

#include<stdio.h>
int main (){
    float pi, radius, area;
    pi = 3.14;

    printf("Enter the radius: ");
    scanf("%f", &radius);

    area = pi * radius * radius;
    printf("The area of a circle is %d\n", area);
    return 0;
}
