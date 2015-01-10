#ifndef SERVICEBASE_H
#define SERVICEBASE_H

#include <pthread.h>

#include <iostream>
#include <string>

#include "jsoncpp/json.h"

class ServiceBase
{
public:
    ServiceBase();
    virtual ~ServiceBase();

    void set_data(Json::Value *recv_root);
    virtual void Start(Json::Value *send_root);

    Json::Value *recv_root_;
    //used for service sync
    pthread_mutex_t mutex_;
};

#endif // SERVICEBASE_H
