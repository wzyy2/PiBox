#include "service.h"
#include "service/servicebase.h"
#include "jsoncpp/json.h"

std::map<std::string, ServiceBase *> Service::service_map_;

Service::Service(char *gbuf)
{
    Json::Reader reader;
    std::string title;

    root_ = new Json::Value;
    send_root_ = new Json::Value;

    if (reader.parse(gbuf, *root_))  // reader将Json字符串解析到root，root将包含Json里所有子元素
    {
        title = (*root_)["title"].asString();  // 访问节点，upload_id = "UP000000"
        //int code = root["code"].asInt();    // 访问节点，code = 100
        //send_root_->append(new_item1); // 插入数组成员
        //std::string buf = send_root_->toStyledString();  //带格式
    }

    target_service_ = service_map_[title];
    if ( target_service_ ==  NULL)
        throw std::string("unkown service");
    std::cout << "handle service:" << title << std::endl;
}

Service::~Service()
{
    //realse recv json_data
    delete root_;
    //realse send json_data
    delete send_root_;
}

void Service::Start()
{
    target_service_->Start(send_root_, root_);
}

char *Service::ifsend(int *send_len)
{
    Json::FastWriter writer;

    json_ =  writer.write(*send_root_);
    std::cout << writer.write(*send_root_);

    *send_len = json_.size();

    return (char *)json_.c_str();
}

void Service::RegisterService(std::string key, ServiceBase *value)
{
    service_map_.insert(make_pair(key, value));
}
