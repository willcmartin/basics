#include <stdio.h>
#include <stdbool.h>

int main(){
    int number;
    bool prime = true;

    printf("Number?\n");
    scanf("%d", &number);

    for (int i=2; i<=number/2; i++) {
        if (number%i == 0){
            prime = false;
            break;
        }
    }

    if (prime == true) {
        printf("Prime\n");
    } else {
        printf("Not a Prime\n");
    }

    return 0;
}
