/*Davidson Lisboa Della Piazza, 169786*/
/*CodeForces 1312A	Two Regular Polygons*/

#include <stdio.h>

int main(){
    int x, y, i, n;
    scanf("%d", &n);
    for (i=0;i<n;i++){
        scanf("%d %d", &x, &y);
        if(x%y==0) printf("YES\n");
        else printf("NO\n");
    }
    return 0;
}
