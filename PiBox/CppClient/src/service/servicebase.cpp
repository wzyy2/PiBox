#include "service/servicebase.h"

ServiceBase::ServiceBase()
{
    // mutex_ = PTHREAD_MUTEX_INITIALIZER;
    pthread_mutex_init(&mutex_,NULL);
    //pthread_mutex_lock(&mutex);
    //pthread_mutex_unlock(&mutex);
    //pthread_mutex_destroy(&mutex);
}

ServiceBase::~ServiceBase()
{

}

void ServiceBase::Start(Json::Value *send_root, Json::Value *recv_root)
{
    std::cout << "Service_base::Start" << std::endl;
}
