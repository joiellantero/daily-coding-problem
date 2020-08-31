// this solution involves using the division operator

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
  int l1[] = {1, 2, 3, 4, 5}, *l2, product = 1, temp = 0;

  // we allocate the memory to be used by the new array, i.e., l2
  l2 = (int*) calloc(sizeof(l1), sizeof(int));

  // we obtain the number of elements of l1 using the formula below
  int length = sizeof(l1)/sizeof(int);

  // we take the product of the array by multiplying each of the elements inside
  for (int i = 0; i < length; i++){
    product *= l1[i];
  }

  // we now divide the product by each of the elements inside l1 and append each quotient to l2
  for (int i = 0; i < length; i++){
    // set the value of the temporary variable (temp) to product through every iteration
    temp = product;

    // divide the temp (a.k.a product) by the current element of array l1
    temp /= l1[i];

    // add the temp (a.k.a product) to our new array
    l2[i] = temp;
  }

  // pass array l2 and length to the function display
  display(l2, length);

  // release the used memory space for the array l2
  free(l2);

  return 0;
}
