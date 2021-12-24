/*Davidson Lisboa Della Piazza, 169786*/
/*CodeForces 158A	Next Round*/

#include <stdio.h>
#include <stdlib.h>

int main() {
    int n, k, i, qtd;
    qtd = 0;
    int *v;
    scanf("%d %d", &n, &k);
    v = malloc(n * sizeof(int));
    for(i=0; i<n; i++){
        scanf("%d", &v[i]);
    }
    for(i=0; i<n; i++){
        if((v[i]>=v[k-1])&&(v[i]>0)){
            qtd++;
        }
    }

    printf("%d\n", qtd);
    return 0;
}