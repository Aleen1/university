#include<stdio.h>
#include<stdlib.h>
#include "cmmdc.h"
#define N 1000
#define min(a,b) \
   ({ __typeof__ (a) _a = (a); \
       __typeof__ (b) _b = (b); \
     _a < _b ? _a : _b; })



int gcd(int a, int b)
{
    return b == 0 ? a : gcd(b, a % b);
}

void gcd_NP(int a[], int grad_a, int b[], int grad_b, int ans[])
{
    int i, n=min(grad_a, grad_b);
    for(i = 0; i<=n; ++i)
    {
       ans[i]=gcd(a[i], b[i]);
    }
}

void solve()
{
    int n, m, i, p1[N], p2[N], p3[N];

    scanf("%d", &n);
    scanf("%d", &m);

    for(i=0;i<=n;++i)
    scanf("%d", &p1[n-i]);

    for(i=0;i<=m;++i)
        scanf("%d", &p2[m-i]);

    gcd_NP(p1, n, p2, m, p3);

    for(i=min(n, m);i>=0;--i)
        printf("%d ", p3[i]);

}
