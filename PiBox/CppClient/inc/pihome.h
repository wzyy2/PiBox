#ifndef PIHOME_H
#define PIHOME_H

#include <autogen.h>        // for printf

#ifdef DEBUG_BUILD
    #define DEBUG(x) fprintf(stderr, x)
#else
    #define DEBUG(x) do {} while (0)
#endif





#endif // PIHOME_H
