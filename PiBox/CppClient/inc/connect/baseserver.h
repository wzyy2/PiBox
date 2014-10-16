#ifndef BASESERVER_H
#define BASESERVER_H

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




class BaseServer
{
public:
    typedef void *(*SERVER_HANDLE)(void *socket); 

    BaseServer(unsigned int port = 3333,
           int family = AF_INET, in_addr_t addr = INADDR_ANY, int queue_length = 20);
    ~BaseServer();

    void Configure(unsigned int port, int family, in_addr_t addr ,int queue_length);
    void setHandle(SERVER_HANDLE ghandle);

    bool StopListen();

    virtual bool StartListen();

    virtual void Process();
    
protected:
    struct sockaddr_in server_addr_; //代表服务器internet地址, 端口
    int server_socket_;

    int listen_queue_length_;
    int sin_family_;
    unsigned int sin_port_;
    in_addr_t sin_addr_;

    SERVER_HANDLE mhandle_;

};

#endif // BASESERVER_H
