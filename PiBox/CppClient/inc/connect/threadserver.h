#ifndef THREADSERVER_H
#define THREADSERVER_H

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
#include <pthread.h>

#include <iostream>
#include <string>

#include "connect/baseserver.h"

class ThreadServer : public BaseServer
{
public:
    ThreadServer();
    ~ThreadServer();

    virtual bool StartListen();

    virtual void Process();

private:

};

#endif // THREADSERVER_H
