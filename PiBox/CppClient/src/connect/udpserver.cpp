#include "connect/udpserver.h"



UdpServer::UdpServer(unsigned int port, int family, in_addr_t addr)
{
    server_socket_ = 0;
    sin_port_ = port;
    sin_family_ = family;
    sin_addr_ = addr;
}

UdpServer::~UdpServer()
{
    StopListen();
}

void UdpServer::Configure(unsigned int port, int family, in_addr_t addr)
{
    sin_port_ = port;
    sin_family_ = family;
    sin_addr_ = addr;
}

void UdpServer::setHandle(UDP_SERVER_HANDLE ghandle)
{
    mhandle_ = ghandle;
}

bool UdpServer::StopListen()
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


bool UdpServer::StartListen()
{
    server_socket_ = socket(AF_INET, SOCK_DGRAM, 0); 
    bzero(&server_addr_, sizeof(server_addr_)); 

    server_addr_.sin_family = sin_family_; 
    server_addr_.sin_addr.s_addr = htons(sin_addr_); 
    server_addr_.sin_port = htons(sin_port_); 

    if(bind(server_socket_, (struct sockaddr *)&server_addr_, sizeof(server_addr_)) == -1) 
    { 
        printf("Server Bind Port : %d Failed!", sin_port_);
        exit(1); 
    } 

    return true;
}


void UdpServer::Process()
{
    mhandle_((void *) &server_socket_);
}
