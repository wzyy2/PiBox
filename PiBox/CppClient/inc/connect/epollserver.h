#ifndef EPOLLSERVER_H
#define EPOLLSERVER_H

#include <netinet/in.h>    // for sockaddr_in
#include <sys/types.h>    // for socket
#include <sys/socket.h>    // for socket

#ifdef linux
#include <sys/epoll.h>
#endif

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

class EpollServer : public BaseServer
{
public:
    EpollServer();
    ~EpollServer();

    virtual bool StartListen();

    virtual void Process();

private:

};

#endif // EPOLLSERVER_H
