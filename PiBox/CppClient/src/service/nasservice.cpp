#include "service/nasservice.h"


const std::string NasService::ktitle_ = "nas";


NasService::NasService()
{
    pthread_mutex_init(&mutex_,NULL);
}

NasService::~NasService()
{
    pthread_mutex_destroy(&mutex_);
}

void NasService::Start(Json::Value *send_root, Json::Value *recv_root)
{        
    pthread_mutex_lock(&mutex_);

    {
        char ret;

        if ((*recv_root)["cmd"] == std::string("open"))
            ret = system("sh ./sh/aria2/start.sh") ;
        else if ((*recv_root)["cmd"] == std::string("close")) {
            ret = system("sh ./sh/aria2/stop.sh") ;
            ret = 0;
        }
            
        else if ((*recv_root)["cmd"] == std::string("time"))
            ;

        if(!ret)
            (*send_root)["cmd_ret"] = std::string("ok");
        else
            (*send_root)["cmd_ret"] = std::string("fail");
    }

    pthread_mutex_unlock(&mutex_);

}
