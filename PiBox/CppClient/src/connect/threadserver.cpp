#include "connect/threadserver.h"


ThreadServer::ThreadServer()
{

}

ThreadServer::~ThreadServer()
{

}


bool ThreadServer::StartListen()
{
    //创建用于internet的流协议(TCP)socket,用server_socket_代表服务器socket
    server_socket_ = socket(PF_INET,SOCK_STREAM,0);
    if (server_socket_ < 0)
    {
        printf("Create Socket Failed!\n");
        exit(1);
    }

    bzero(&server_addr_,sizeof(server_addr_)); //把一段内存区的内容全部设置为0
    server_addr_.sin_family = sin_family_;
    server_addr_.sin_addr.s_addr = htons(sin_addr_);
    server_addr_.sin_port = htons(sin_port_);

    {
        int opt =1;
        setsockopt(server_socket_,SOL_SOCKET,SO_REUSEADDR,&opt,sizeof(opt));
    }

    //把socket和socket地址结构联系起来
    if (bind(server_socket_,(struct sockaddr*)&server_addr_,sizeof(server_addr_)))
    {
        printf("Server Bind Port : %d Failed!", sin_port_);
        exit(1);
    }

    //server_socket_用于监听
    if (listen(server_socket_, listen_queue_length_))
    {
        printf("Server Listen Failed!\n");
        exit(1);
    }

    printf("Server Start Listen!\n");

    return true;
}


void ThreadServer::Process()
{
   while (1) //服务器端要一直运行
    {
        //定义客户端的socket地址结构client_addr
        struct sockaddr_in client_addr;
        socklen_t length = sizeof(client_addr);
        //接受一个到server_socket_代表的socket的一个连接
        //如果没有连接请求,就等待到有连接请求--这是accept函数的特性
        //accept函数返回一个新的socket,这个socket(new_server_socket_)用于同连接到的客户的通信
        //new_server_socket_代表了服务器和客户端之间的一个通信通道
        //accept函数把连接到的客户端信息填写到客户端的socket地址结构client_addr中
        int new_server_socket_ = accept(server_socket_,(struct sockaddr*)&client_addr,&length);
        if ( new_server_socket_ < 0)
        {
            printf("Server Accept Failed!\n");
            break;
        }
        {
            int ret;
            pthread_t id;
            ret=pthread_create(&id,NULL, mhandle_, (void *)&new_server_socket_);
            if(ret!=0){
                printf ("Create pthread error!\n");
                exit (1);
            }

        }
        //关闭与客户端的连接
        //close(new_server_socket_);
    }
}