#include "service/applicationservice.h"
#include "func/inifile.h"

#include <dirent.h>
#include <sys/stat.h>
#include <unistd.h>
#include <stdio.h>
#include <string.h>
#include <dlfcn.h>


const std::string ApplicationService::ktitle_ = "application";


ApplicationService::ApplicationService()
{  
    char* error=0;
    //dlopen
    read_app_ini("./App");

    for (unsigned int i=0; i < app_list.size(); i++) {
        void *handle;
        APPFUN get_fun;
        APPFUN_INIT get_fun_init,get_fun_exit;

        std::string ini_file = std::string("./App/") + app_list[i] + std::string("/app.ini");
        if(!read_profile_int("Application", "HaveLib", 1,   ini_file.c_str())) {
            //no libapp.so
            continue;
        }

        std::string file = std::string("./App/") + app_list[i] + std::string("/libapp.so");

        handle = dlopen(file.c_str(),RTLD_LAZY);

        if (!handle) {
            printf("%s \n",dlerror());
            continue;
        }

        get_fun = (APPFUN) dlsym(handle, "app_main");

        error=dlerror();
        if(error) {
            printf("%s \n",error);   
            exit(1);
        }

        dl_list.push_back(handle);
        application_map_.insert(make_pair(app_list[i], get_fun));

        get_fun_init = (APPFUN_INIT) dlsym(handle, "app_init");

        error=dlerror();//清楚错误信息
        if (!error)  {
            //init the application
            get_fun_init();  
        }
        else {
            printf("%s \n",error);   
        }

    }

}

ApplicationService::~ApplicationService()
{
    //close share lib
    for (unsigned int i=0; i < dl_list.size(); i++) {

        APPFUN_INIT get_fun_exit = (APPFUN_INIT) dlsym(dl_list[i], "app_exit");

        if (dlerror() == NULL) //清楚错误信息
        {
            //exit the application
            get_fun_exit();  
        }

        dlclose(dl_list[i]);
    }
}

void ApplicationService::Start(Json::Value *send_root, Json::Value *recv_root)
{        
    std::string title;
    APPFUN app_main;

    title = (*recv_root)["app_name"].asString();

    app_main = application_map_[title];

    std::cout << "start_application:" << title << std::endl;

    if ( app_main ==  NULL)
        //unkown app
        return;

    app_main(send_root, recv_root);
}

int ApplicationService::read_app_ini(const char* dirname)
{
    DIR* dp;
    struct dirent* dirp;
    struct stat st;

    /* open dirent directory */
    if((dp = opendir(dirname)) == NULL)
    {
        perror("opendir");
        return -1;
    }

    /**
     * read all files in this dir
     **/
    while((dirp = readdir(dp)) != NULL)
    {
        char fullname[255];
        memset(fullname, 0, sizeof(fullname));

        /* ignore hidden files */
        if(dirp->d_name[0] == '.')
            continue;

        /* display file name with proper tab */
        //printf("%s\n", dirp->d_name);

        strncpy(fullname, dirname, sizeof(fullname));
        strncat(fullname, "/", sizeof(fullname));
        strncat(fullname, dirp->d_name, sizeof(fullname));
        /* get dirent status */
        if(stat(fullname, &st) == -1)
        {
            perror("stat");
            fputs(fullname, stderr);
            return -1;
        }


        /* if dirent is a directory, call itself */
        if(S_ISDIR(st.st_mode)) {
            const char *section = "Application";
            const char *key = "Name";
            char rec[100]={0};
            //     write_profile_string(section, key, "fuck!!!!!",file);

            if(read_profile_string(section, key, rec, 100,"",strncat(fullname, "/app.ini", sizeof(fullname))))
            {
                app_list.push_back(dirp->d_name);
                //application_map_.insert(make_pair(std::string(dirp->d_name), aa));
            }
            else {
                return -1;
                perror("no ini,make sure this dir is app dir");
            }
        }


    }

    closedir(dp);

    return 0;
}

