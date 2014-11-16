#include "pihome.h"
#include "device/serial.h"
#include "connect/threadserver.h"
#include "service.h"
#include "service/servicebase.h"
#include "service/statusservice.h"
#include "service/nasservice.h"
#include "service/applicationservice.h"

#include <string>
#include <map>
#include <iostream>

static void *process_thread(void *new_server_socket_);


int main(int argc, char **argv)
{
    ThreadServer *pi_server;

    {
        StatusService *status_service;
        status_service = new StatusService;
        Service::RegisterService(status_service->ktitle_, status_service);
    }

    {
        NasService *nas_service;

        nas_service = new NasService;
        Service::RegisterService(nas_service->ktitle_, nas_service);
    }

    {
        ApplicationService *application_service;

        application_service = new ApplicationService;
        Service::RegisterService(application_service->ktitle_, application_service);
    }

    pi_server = new ThreadServer();
    pi_server->Configure(3333, AF_INET, INADDR_ANY, 20);
    pi_server->setHandle(process_thread);
    pi_server->StartListen();
    pi_server->Process();

}


static void *process_thread(void *socket)
{
    char buffer[1024];
    char *send_buf;
    socklen_t length;
    int send_len;
    bzero(buffer, 1024);

    do {
        length = recv(*((int *)socket),buffer,1024,0);
        if(length > 0) {
            try {
                //handle it in service
                Service pi_service(buffer);
                pi_service.Start();
                //if we should send back
                send_buf = pi_service.ifsend(&send_len);
                //printf("recv1:%s", send_buf);
                if (send_len > 0)
                    send(*((int *)socket),send_buf,send_len,0);
            }
            catch (std::string& e) {
            }
        }
    } while(length);

    //关闭与客户端的连接
    close(*((int *)socket));

    return NULL;
}