#ifndef SERVICE_H
#define SERVICE_H

#include <stdio.h>        // for printf
#include <stdlib.h>        // for exit
#include <string.h>        // for bzero
#include <unistd.h>
#include <fcntl.h>
#include <errno.h>

#include <iostream>
#include <string>
#include <map>

#include "jsoncpp/json.h"

class ServiceBase;

class Service
{
public:
    Service(char *gbuf);
    ~Service();
    void Start();
    char *ifsend(int *send_len);

    static void RegisterService(std::string key, ServiceBase *value);

private:
    ServiceBase *target_service_;
    std::string json_;
    Json::Value *root_;
    Json::Value *send_root_;
    static  std::map<std::string, ServiceBase *> service_map_;

};



#endif // SERVICE_H
