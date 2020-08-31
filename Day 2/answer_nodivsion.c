// this solution does not involve using the division operator

#include <stdio.h>
#include <stdlib.h>

// this function is for displaying the result of the new array, i.e., l2
void display(int l2[], int length){
  for(int i = 0; i < length; i++){
    printf("%d ", l2[i]);
  }
  puts("");
  return;
}

int main(){
  // declaring the variables to be used in the program
  int l1[] = {1, 2, 3, 4, 5}, *l2;

  // we allocate the memory to be used by the new array, i.e., l2
  // by using calloc we automatically initialize l2's elements to be zero
  l2 = (int*) calloc(sizeof(l1), sizeof(int));

  // we obtain the number of elements of l1 using the formula below
  int length = sizeof(l1)/sizeof(int);

  // we now iterate through l1 using nested loops
  for (int i = 0; i < length; i++){
    int temp = 1;
    for (int j = 0; j < length; j++){
      // we exclude the current element i of l1 in computing the product
      if (j == i){
        continue;
      }
      else{
        temp *= l1[j];
      }
    }

    // add the product to our new array
    l2[i] = temp;
  }

  // pass array l2 and length to the function display
  display(l2, length);

  // release the used memory space for the array l2
  free(l2);
}
