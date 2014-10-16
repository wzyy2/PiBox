#include "service/servicebase.h"

ServiceBase::ServiceBase()
{
    mutex_ = PTHREAD_MUTEX_INITIALIZER;
    //pthread_mutex_init(&mutex,NULL);
    //pthread_mutex_lock(&mutex);
    //pthread_mutex_unlock(&mutex);
    //pthread_mutex_destroy(&mutex);
}

ServiceBase::~ServiceBase()
{

}

void ServiceBase::set_data(Json::Value *recv_root)
{
    recv_root_ = recv_root;
}

void ServiceBase::Start(Json::Value *send_root)
{
    std::cout << "Service_base::Start" << std::endl;
}
