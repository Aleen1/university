#ifndef ZAR_H
#define ZAR_H
#include <bits/stdc++.h>
using namespace std;

class czar
{
    private:
        pair<int, int> freq[10];
        int freq2[2];
    public:
        czar();
        void vote();
        void vote_secRUN();
        friend class CTrib;
};


#endif // ZAR_H

