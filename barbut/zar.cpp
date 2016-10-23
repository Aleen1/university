#include "zar.h"
#include<stdlib.h>
#include<time.h>

czar::czar()
{
    srand(time(NULL));
}

int czar::get_number()
{
    return rand()%6+1;
}
