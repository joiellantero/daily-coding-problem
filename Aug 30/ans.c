#include <stdio.h>
#include <stdlib.h>

void display(int l2[], int length){
  for(int i = 0; i < length; i++){
    printf("%d ", l2[i]);
  }
  puts("");
  return;
}

int main(){
  int l1[] = {1, 2, 3, 4, 5}, *l2;
  l2 = (int*) calloc(sizeof(l1), sizeof(int));
  int length = sizeof(l1)/sizeof(int);
  for (int i = 0; i < length; i++){
    int temp = 1;
    for (int j = 0; j < length; j++){
      if (j == i){
        continue;
      }
      else{
        temp *= l1[j];
      }
    }
    l2[i] = temp;
  }
  display(l2, length);
  free(l2);
}
