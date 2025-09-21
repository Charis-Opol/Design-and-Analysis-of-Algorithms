#include<stdio.h>

void main(){
    int array[] = {34, 665, 7, 65, 67, 1000};
    int n = sizeof(array)/sizeof(array[0]);
    int max_index = 0;

    for (int i = 0; i < n; i++)
    {
        if (array[max_index] < array[i]){
            max_index = i;
        }
    }

    printf("The maximum element is %d in position %d.\n", array[max_index], max_index);
    
}