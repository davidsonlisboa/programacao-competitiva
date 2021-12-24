/*Davidson Lisboa Della Piazza, 169786*/
/*UVA 424	Integer Inquiry*/

#include <stdio.h>
#include <stdlib.h>

#define MAXDIGITS 100
#define PLUS 1
#define MINUS -1

typedef long long ll;
typedef struct {
    char digits[MAXDIGITS];
    int signbit;
    int lastdigit;
} bignum;

void add_bignum(bignum *, bignum *, bignum *);
void subtract_bignum(bignum *, bignum *, bignum *);
void lltobignum(ll, bignum *);
void zero_justify(bignum *);
int compare_bignum(bignum *, bignum *);
int max(int, int);
void printbignum(bignum *);


int main() {
    int i;
    bignum bigA, bigB, bigC;
    ll a,b,c;
    c = 0;
    lltobignum(c, &bigC);
    for(i=0; i<100; i++){
        scanf("%lld", &a);
        if(a==0){
            lltobignum(a, &bigA);
            add_bignum(&bigA, &bigB, &bigC);
            break;
        }
        scanf("%lld", &b);
        if(b==0){
            lltobignum(b, &bigB);
            add_bignum(&bigA, &bigB, &bigC);
            break;
        }
        lltobignum(a, &bigA);
        lltobignum(b, &bigB);
        add_bignum(&bigA, &bigB, &bigC);
    }
    printbignum(&bigC);
    return 0;
}

void printbignum(bignum *c){
    int i;
    if(c->signbit==MINUS) printf("-");
    
    for(i=c->lastdigit; i>=0; i--){
        printf("a");
        printf("%c", c->digits[i]);
    }
    printf("\n");
}

void lltobignum(ll s, bignum *n){
    int i;
    ll t;

    if (s>=0) n -> signbit = PLUS;
    else n -> signbit = MINUS;

    for (i=0; i < MAXDIGITS; i++) n->digits[i] = (char) 0;
    n->lastdigit = -1;

    t = (s >= 0) ? s : -s;
    while (t > 0){
        n -> lastdigit++;
        n->digits[n->lastdigit] = (char) (t%10);
        t = t / 10;
    }
    if (s==0) n->lastdigit = 0;
}

int compare_bignum(bignum *a, bignum *b){
    int i;

    if((a->signbit == MINUS) && (b->signbit == PLUS)) return (PLUS);
    if((a->signbit == MINUS) && (b->signbit == MINUS)) return (MINUS);
    if(a->lastdigit > b->lastdigit) return (MINUS * a->signbit);
    if(b->lastdigit > a->lastdigit) return (PLUS * a->signbit);

    for(i = a->lastdigit; i>=0; i--){
        if(a->digits[i] > b->digits[i]) return(MINUS * a->signbit);
        if(b->digits[i] > a->digits[i]) return(PLUS * a->signbit);
    }
    return(0);
}

void zero_justify(bignum *n){
    while((n->lastdigit > 0) && (n->digits[n->lastdigit] ==0))
        n->lastdigit--;
    if((n->lastdigit == 0) && (n->digits[0] == 0))
        n->signbit = PLUS; 
}

int max(int a, int b){
    if(a>b) return a;
    else return b;
}

void subtract_bignum(bignum *a, bignum *b, bignum *c){
    int borrow;
    int v;
    int i;
    ll s = 0;
    lltobignum(s, c);

    if((a->signbit == MINUS) || (b->signbit == MINUS)){
        b->signbit = -1 * b->signbit;
        add_bignum(a, b, c);
        b->signbit = -1 *b->signbit;
        return;
    }

    if(compare_bignum(a,b) == PLUS){
        subtract_bignum(b,a,c);
        c->signbit = MINUS;
        return;
    }
    c->lastdigit = max(a->lastdigit, b->lastdigit);
    borrow = 0;

    for(i=0; i<=(c->lastdigit); i++){
        v = (a->digits[i] - borrow - b->digits[i]);
        if(a->digits[i]>0) borrow = 0;
        if(v<0){
            v = v + 10;
            borrow = 1;
        }
        c->digits[i] = (char) v;
    }
    zero_justify(c);
}

void add_bignum(bignum *a, bignum *b, bignum *c){
    int i, carry;

    if(a->signbit == b->signbit) c->signbit = a->signbit;
    else{
        if(a->signbit == MINUS){
            a->signbit = PLUS;
            subtract_bignum(b,a,c);
            a->signbit = MINUS;
        } else{
            b->signbit = PLUS;
            subtract_bignum(a,b,c);
            b->signbit = MINUS;
        }
        return;
    }
    c->lastdigit = max(a->lastdigit, b->lastdigit)+1;
    carry = 0;

    for(i=0; i<=(c->lastdigit); i++){
        c->digits[i] = (char) (carry+a->digits[i]+b->digits[i]) %10;
        carry = (carry+a->digits[i] + b->digits[i])/10;
    }
    zero_justify(c);
}
