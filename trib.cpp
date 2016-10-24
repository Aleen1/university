#include "trib.h"
#include<bits/stdc++.h>
using namespace std;

CTrib::CTrib(czar z1)
{
    this->z1=z1;
    n=0;
}

void CTrib::reset(czar z1)
{
    this->z1.reset_freq();
}

void CTrib::get_number_people()
{
    cout<<"Read number of people: "; cin>>this->n;
}

void CTrib::run_election(czar z1)
{
    for(int i = 1; i <= n; ++i)
    {
        this->z1.vote();
    }
}

int CTrib::find_president(czar z1)
{
    for(int i = 1; i <= 6; ++i)
        if(this->z1.freq[i] > n/2)
            return i;
    return 0;
}
