#include <stdio.h>
#include "../include/reiser4/libreiser4.h"

int main(int argc, char **argv){

    const char      *lib_ver;
    lib_ver = (const char *)libreiser4_version();
    printf("%s\n", lib_ver);
    return 0;

}

