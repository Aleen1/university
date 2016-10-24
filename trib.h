#ifndef TRIB_H
#define TRIB_H
#include "zar.h"

class CTrib
{
    private:
        czar z1;
        int n;
    public:
        CTrib(czar z1);
        void reset(czar z1);
        void get_number_people();
        void run_election(czar z1);
        int find_president(czar z1);
};

#endif // TRIB_H
