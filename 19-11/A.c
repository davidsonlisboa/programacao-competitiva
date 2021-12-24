/*Davidson Lisboa Della Piazza, 169786*/
/*CodeForces 181A	Series of Crimes*/

#include <stdio.h>
#include <stdlib.h>

int main(){
    int n, m, i, j, np, aux, pontox, pontoy;
    int arr[3];
    aux = 0;

    scanf("%d %d", &n, &m);
    char (*x)[m] = malloc(n * sizeof *x);
    for (i=0;i<n;i++){
        for (j=0;j<m;j++){
            scanf(" %c", &x[i][j]);
        }
    }

    for (i=0;i<n;i++){
        np = 0;
        for (j=0;j<m;j++){
                if(x[i][j]=='*'){
                    arr[aux] = j;
                    np++;
                    aux++;
            }
        }
        if(np==1){
            pontox = i;
            np = 0;
        }
    }

    if(arr[0]==arr[1]) pontoy = arr[2];
    else{
    if(arr[0]==arr[2])
        pontoy = arr[1];
    else
        pontoy = arr[0];
    }

    printf("%d %d", pontox+1, pontoy+1);
    free(x);
    return 0;
}
