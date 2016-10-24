#include "zar.h"
#include "trib.h"
#include<bits/stdc++.h>

using namespace std;

int main()
{
    czar zar1;
    CTrib obj_trib(zar1);

    obj_trib.get_number_people();

    while(1)
    {
        obj_trib.run_election(zar1);

        int president = obj_trib.find_president(zar1);
        if(president)
        {
            cout<<"The new president is: "<< president;
            return 0;
        }
    }

    return 0;
}
