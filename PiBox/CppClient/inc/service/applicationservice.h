#ifndef APPLICATIONSERVICE_H
#define APPLICATIONSERVICE_H

#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#include <map>
#include <iostream>
#include <string>
#include <vector>
#include <sstream>
#include "service/servicebase.h"
#include "jsoncpp/json.h"

typedef int (*APPFUN)(Json::Value *send_root, Json::Value *recv_root); 
typedef int (*APPFUN_INIT)(); 

class ApplicationService : public ServiceBase
{
public:
    ApplicationService();
    ~ApplicationService();

    const static std::string ktitle_;

    void Start(Json::Value *send_root, Json::Value *recv_root);

    int read_app_ini(const char* dirname);

    void HandleCmd();

private:
    std::map<std::string, APPFUN> application_map_;
    std::vector<std::string> app_list;
    std::vector<void *> dl_list;
};

#endif // APPLICATIONSERVICE_H
