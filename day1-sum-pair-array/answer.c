// applying the same concept in python but using c language.

#include <stdio.h>

int main(){
  int num[] = {10, 15, 3, 7};
  int length = sizeof(num)/sizeof(int);
  int k = 0, c = 0;
  printf("Enter value of k: ");
  scanf("%d", &k);

  for (int i = 0; i < length; i++ ){
    for (int j = 0; j < length; j++){
      if (k == (num[i] + num[j])){
        c = 1;
        break;
      }
    }
  }

  if (c == 1){
    printf("true\n");
    return 0;
  }
  printf("false\n");
  return 0;
}
