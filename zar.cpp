#include "zar.h"
#include<bits/stdc++.h>

czar::czar()
{
    memset(freq, 0, sizeof(freq));
    srand(time(NULL));
}

void czar::vote()
{
    ++ freq[1 + rand()%6];
}

void czar::reset_freq()
{
    memset(this->freq, 0, sizeof(this->freq));
}


