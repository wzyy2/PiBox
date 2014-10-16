#include "connect/baseserver.h"



BaseServer::BaseServer(unsigned int port, int family, in_addr_t addr, int queue_length)
{
    server_socket_ = 0;
    sin_port_ = port;
    sin_family_ = family;
    sin_addr_ = addr;
    listen_queue_length_ = queue_length;
}

BaseServer::~BaseServer()
{
    StopListen();
}

void BaseServer::Configure(unsigned int port, int family, in_addr_t addr, int queue_length)
{
    sin_port_ = port;
    sin_family_ = family;
    sin_addr_ = addr;
    listen_queue_length_ = queue_length;
}

void BaseServer::setHandle(SERVER_HANDLE ghandle)
{
    mhandle_ = ghandle;
}

bool BaseServer::StopListen()
{
    if (server_socket_ > 0) {
        //关闭监听用的socket
        close(server_socket_);
        if (server_socket_)
            return false;
        else
            return true;
    }
    return true;
}

bool BaseServer::StartListen()
{
    return true;
}


void BaseServer::Process()
{
    while(1);
}