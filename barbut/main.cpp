#include "zar.h"
#include <iostream>
using namespace std;

int v[10][10], a[10], b[10][10], prev_x, prev_y, ans[4][4];

int main()
{
    czar z1;
    czar z2;
    for(int i=1;i<=9000;++i)
    {
        int x = z1.get_number();
        int y = z2.get_number();
        v[x][y]++;

        a[x]++;
        a[y]++;

        if(x == prev_x && y==prev_y)
            b[x][y]++;
        else
        {
            prev_x = x;
            prev_y = y;
        }
    }

    ans[3][0]=v[1][1];
    ans[3][1]=ans[3][2]=1;

    for(int i=1;i<=6;++i)
    {
        for(int j=1;j<=6;++j)
        {
            if(ans[1][0]<v[i][j])
            {
                ans[1][0]=v[i][j];
                ans[1][1]=i;
                ans[1][2]=j;
            }
            if(ans[2][0]<b[i][j])
            {
                ans[2][0]=v[i][j];
                ans[2][1]=i;
                ans[2][2]=j;
            }
            if(ans[3][0]>v[i][j])
            {
                ans[3][0]=v[i][j];
                ans[3][1]=i;
                ans[3][2]=j;
            }
        }
    }
    cout<<"Perechea cu cele mai multe aparitii este: "<<ans[1][1]<<' '<<ans[1][2]<<" cu "<<ans[1][0]<<" aparitii\n";
    cout<<"Perechea cu cele mai multe aparitii consecutive este: "<<ans[2][1]<<' '<<ans[2][2]<<" cu "<<ans[2][0]<<" aparitii\n";
    cout<<"Perechea cu cele mai putine aparitii este: "<<ans[3][1]<<' '<<ans[3][2]<<" cu "<<ans[3][0]<<" aparitii\n";
    cout<<"Frecventa fiecarei fete a unui zar este:\n";
    for(int i=1;i<=6;++i)
        cout<<"frecventa "<<i<<" este: "<< a[i]<<'\n';
    return 0;
}
