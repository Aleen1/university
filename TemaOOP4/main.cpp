#include "zar.h"
#include "trib.h"
#include<bits/stdc++.h>

using namespace std;

int president;

int main()
{
    CTrib obj_trib;

    obj_trib.get_number_people();
    obj_trib.run_election();

    obj_trib.find_president();

    president = obj_trib.get_president();

    if(president)
    {
        cout << "The new president is: " << president << " after first election run";
    }
    else
    {
        obj_trib.run_2nd_election();
        president = obj_trib.get_president();
        cout << "The new president is: " << president << " after second election run";
    }

    return 0;
}
