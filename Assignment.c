#include<stdio.h>

int main(){
    int array[5] = {55, 22, 3, 445, 52};

    int max_index = 0; 
    for (int i = 1; i < 5; i++){
        if (array[max_index] < array[i]){
            max_index = i;
        }
    }

    printf("The maximum value is: %d\n", array[max_index]);
    return 0;
}

