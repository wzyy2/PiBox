#include "service/statusservice.h"

const std::string StatusService::ktitle_ = "status";

static inline char *
skip_linebreak(const char *p)
{
    while (*p == '\n') p++;
    return (char *)p;
}

/* skip running/tasks */
static inline char *
skip_token(const char *p)
{
    while (isspace(*p)) p++;
    while (*p && !isspace(*p)) p++;
    return (char *)p;
}

StatusService::StatusService()
{

}

StatusService::~StatusService()
{
}


void StatusService::Start(Json::Value *send_root, Json::Value *recv_root)
{
    FILE *pf;
    char buffer[4096];
    char *p,*tmp;
    char *save_ptr=NULL;
    struct SystemInfo sys_info;


    if ((*recv_root)["cmd"] == std::string("shutdown"))
        system("sudo shutdown -h now");
    else if ((*recv_root)["cmd"] == std::string("reboot"))
        system("sudo reboot");

    /* uname -a ,Linux ubuntu 3.13.0-24-generic*/
    {
        pf = popen("uname -a", "r");
        fread(buffer, sizeof(buffer), 1, pf);

        p = buffer;
        tmp = strtok_r(p, " ", &save_ptr);

        for (int i=0; i<3; i++) {

            tmp = strtok_r(NULL, " ", &save_ptr);
            if (i == 0)
                sys_info.name = std::string(tmp);
            else if (i == 1)
                sys_info.kernel_version = std::string(tmp);

        }

        pclose(pf);
    }

    /* cat /proc/loadavg ,0.75 0.70 0.95 2/646 5691*/
    {
        pf = popen("cat /proc/loadavg", "r");
        fread(buffer, sizeof(buffer), 1, pf);

        p = buffer;
        tmp = strtok_r(p, " ", &save_ptr);

        for (int i=0; i<3; i++) {
            sys_info.load_avg[i] = strtod(tmp, NULL);
            tmp = strtok_r(NULL, " ", &save_ptr);
        }

        pclose(pf);
    }

    /* uptime,  05:20:25 up 50 min */
    {

        pf = popen("uptime", "r");
        fread(buffer, sizeof(buffer), 1, pf);
        p = buffer;
        while( *p != 'u')
            p++;
        tmp = p;
        while( *p != ',')
            p++;
        *p = '\0';
        sys_info.uptime = std::string(tmp);

        pclose(pf);
    }

    /* free -m */
    {
        std::stringstream  stream;
        std::string tmp;

        pf = popen("free -m", "r");
        fread(buffer, sizeof(buffer), 1, pf);
        stream << std::string(buffer);

        do {
            stream >> tmp;
        } while( tmp != std::string("Mem:"));

        stream >> tmp;
        sys_info.memory_info.total = strtol(tmp.c_str(), NULL, 10);
        stream >> tmp;
        sys_info.memory_info.used = strtol(tmp.c_str(), NULL, 10);
        stream >> tmp;
        sys_info.memory_info.free = strtol(tmp.c_str(), NULL, 10);
        stream >> tmp;
        sys_info.memory_info.shared = strtol(tmp.c_str(), NULL, 10);
        stream >> tmp;
        sys_info.memory_info.buffers = strtol(tmp.c_str(), NULL, 10);
        stream >> tmp;
        sys_info.memory_info.cached = strtol(tmp.c_str(), NULL, 10);

        pclose(pf);
    }

    /* df */
    {
        int i=0;
        char a;
        std::stringstream  stream;
        std::string tmp;
        struct FilesystemInfo f;

        pf = popen("df", "r");
        fread(buffer, sizeof(buffer), 1, pf);
        p = buffer;
        while ( *p++ != '\n' );
        stream << std::string(p);

        while ( stream >> tmp ) {
            i++;
            a = i % 6;

            if (a == 0) {
                f.mount_point = tmp;
                sys_info.filesystem_info.push_back(f);
            }
            else if (a == 1)
                f.filesystem = tmp;
            else if (a == 4)
                f.available = strtol(tmp.c_str(), NULL, 10);
            else if (a == 5)
                f.used = strtol(tmp.c_str(), NULL, 10);
        }

        pclose(pf);
    }

    /* /proc/stat*/
    {
        std::stringstream  stream;
        std::string tmp;
        char buffer[4096];
        long buf[4];

        pf = popen("cat /proc/stat", "r");
        fread(buffer, sizeof(buffer), 1, pf);
        stream << std::string(buffer);

        stream >> tmp;
        for(int i = 0; i < 4; i++) {
            stream >> tmp;
            buf[i] = strtol(tmp.c_str(), NULL, 10);
        }

        sys_info.cpu = 100 * (buf[0] + buf[1] + \
                buf[2]) / (buf[0] + buf[1] + buf[2] + buf[3]);

        pclose(pf);
    }

    (*send_root)["name"] = sys_info.name;
    (*send_root)["kernel_version"] = sys_info.kernel_version;
    (*send_root)["uptime"] = sys_info.uptime;
    (*send_root)["cpu"] = sys_info.cpu;
    {
        Json::Value jsonval;

        jsonval["0"] = sys_info.load_avg[0];
        jsonval["1"] = sys_info.load_avg[1];
        jsonval["2"] = sys_info.load_avg[2];

        (*send_root)["loadavg"] = jsonval;
    }

    {
        Json::Value jsonval;

        jsonval["total"] = (int) sys_info.memory_info.total;
        jsonval["used"] = (int) sys_info.memory_info.used;
        jsonval["free"] = (int) sys_info.memory_info.free;
        jsonval["shared"] = (int) sys_info.memory_info.shared;
        jsonval["buffers"] = (int) sys_info.memory_info.buffers;
        jsonval["cached"] = (int) sys_info.memory_info.cached;


        (*send_root)["memory_info"] = jsonval;
    }

    {
        Json::Value jsonarray;

        for (unsigned int i = 0; i < sys_info.filesystem_info.size(); i++) {
            Json::Value jsonval;
            jsonval["filesystem"] = sys_info.filesystem_info[i].filesystem;
            jsonval["mount_point"] = sys_info.filesystem_info[i].mount_point;
            jsonval["available"] = (int) sys_info.filesystem_info[i].available;
            jsonval["used"] = (int) sys_info.filesystem_info[i].used;
            jsonarray.append(jsonval);  // 插入数组成员
        }

        (*send_root)["filesystem_info"] = jsonarray;
    }


}
