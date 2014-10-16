#ifndef CONNECTCLIENT_H
#define CONNECTCLIENT_H

#include <netinet/in.h>    // for sockaddr_in
#include <sys/types.h>    // for socket
#include <sys/socket.h>    // for socket
#include <arpa/inet.h>
#include <sys/stat.h>

#include <stdio.h>        // for printf
#include <stdlib.h>        // for exit
#include <string.h>        // for bzero
#include <unistd.h>
#include <fcntl.h>
#include <termios.h>
#include <errno.h>

#include <iostream>
#include <string>



class ConnectClient
{
public:
    ConnectClient();
    ~ConnectClient();



};

#endif // CONNECTCLIENT_H
