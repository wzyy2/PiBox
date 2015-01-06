#ifndef NASSERVICE_H
#define NASSERVICE_H

#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#include <iostream>
#include <string>
#include <vector>
#include <sstream>
#include "service/servicebase.h"
#include "jsoncpp/json.h"


class NasService : public ServiceBase
{
public:
    NasService();
    ~NasService();

    const static std::string ktitle_;

    void Start(Json::Value *send_root, Json::Value *recv_root);

    void HandleCmd();

private:
};

#endif // NASSERVICE_H
