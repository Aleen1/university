#ifndef TRIB_H
#define TRIB_H
#include "zar.h"

class CTrib
{
    private:
        czar z1;
        int n, president;
    public:
        CTrib();
        void get_number_people();
        void run_election();
        void run_2nd_election();
        void find_president();
        int get_president();
};

#endif // TRIB_H
