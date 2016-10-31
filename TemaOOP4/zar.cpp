#include "zar.h"
#include<bits/stdc++.h>

czar::czar()
{
    memset(freq, 0, sizeof(freq));
    memset(freq2, 0, sizeof(freq2));
    for(int i = 1; i <= 6; ++i)
        freq[i].second = i;
    srand(time(NULL));
}

void czar::vote()
{
    ++ freq[1 + rand()%6].first;
}

void czar::vote_secRUN()
{
    ++ freq2[rand()%2];
}

