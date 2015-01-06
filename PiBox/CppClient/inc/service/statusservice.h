#ifndef STATUSSERVICE_H
#define STATUSSERVICE_H

#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#include <iostream>
#include <string>
#include <vector>
#include <sstream>
#include "service/servicebase.h"
#include "jsoncpp/json.h"



struct  FilesystemInfo
{
    std::string filesystem;
    std::string mount_point;
    long available;
    char used;
};

struct  MemoryInfo
{
    long total;
    long used;
    long free;
    long shared;
    long buffers;
    long cached;
};

struct  SystemInfo
{
    std::string name;
    std::string kernel_version;
    std::string uptime;

    double load_avg[3];
    double cpu;
    struct  MemoryInfo memory_info;
    std::vector<struct FilesystemInfo> filesystem_info;
};

class StatusService : public ServiceBase
{
public:
    StatusService();
    ~StatusService();

    const static std::string ktitle_;

    void Start(Json::Value *send_root, Json::Value *recv_root);


private:

};

#endif // STATUSSERVICE_H
