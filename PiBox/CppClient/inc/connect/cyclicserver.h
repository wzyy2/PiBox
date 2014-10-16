#ifndef CYCLICSERVER_H
#define CYCLICSERVER_H

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

#include "connect/baseserver.h"

class CyclicServer : public BaseServer
{
public:
    CyclicServer();
    ~CyclicServer();


    virtual bool StartListen();

    virtual void Process();

private:

};

#endif // CYCLICSERVER_H
