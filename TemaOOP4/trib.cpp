#include "trib.h"
#include<bits/stdc++.h>
using namespace std;

CTrib::CTrib()
{
    n = president = 0;
}

void CTrib::get_number_people()
{
    cout << "Read number of people: ";
    cin >> n;
}

void CTrib::run_election()
{
    for(int i = 1; i <= n; ++i)
        z1.vote();
}

void CTrib::find_president()
{
    for(int i = 1; i <= 6; ++i)
        if(z1.freq[i].second > n/2)
            president = i;
}

void CTrib::run_2nd_election()
{
    sort(z1.freq+1, z1.freq+7);
    int frt_president = z1.freq[6].second;
    int sec_president = z1.freq[5].second;
    for(int i = 1; i <= n; ++i)
        z1.vote_secRUN();

    if(z1.freq2[0] > z1.freq2[1])
        president = frt_president;
    else
        president = sec_president;
}

int CTrib::get_president()
{
    return president;
}
