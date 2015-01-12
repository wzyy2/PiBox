#include <iostream>
#include <wiringPi.h>
#include "stdlib.h"
#include "stdio.h"
#include "jsoncpp/json.h"

#define MAX_PIN 17

struct PIN{
    int mode;
    int value;
    int read_value;
    int pwm_value;
    int pull_mode;
    bool if_change;
}pin_info[MAX_PIN];

//pwm status
int pwm_clock = -1;
int pwm_range = 1024;
int pwm_mode = 1;
bool if_change = false;

extern "C"
{

    int app_init()
    {
        int i = 0;  
        //std::cout << "fuck you!!!" << std::endl
        // 初始化wiringPi  
        wiringPiSetup();  

        // all to uncertain
        for( i = 0 ; i < MAX_PIN ; i++ ) {  
            pin_info[i].mode = -1;
            pin_info[i].value = -1;
            pin_info[i].pwm_value = -1;
            pin_info[i].read_value = digitalRead(i);
            pin_info[i].pull_mode = -1;
            pin_info[i].if_change = false;
        }

        // // 设置IO口全部为输出状态  
        // for( i = 0 ; i < 8 ; i++ ) {  
        //     pinMode(i, OUTPUT);  
        //     pin_info[i].mode = OUTPUT;
        //     pin_info[i].read_value = digitalRead(i);
        // }

        return 0;
    }

    int app_exit()
    {
        return 0;
    }

    int app_main(Json::Value *send_root, Json::Value *recv_root)
    {
        std::string action;
        int pin_num;

        action = (*recv_root)["action"].asString();
        std::cout << action <<std::endl;
        pin_num = (*recv_root)["pin_num"].asInt();
        //check pin_num
        if(pin_num < 0 || pin_num >= MAX_PIN)
            return 0;

        if(action == "read_info") {
            Json::Value jsonarray;

            for(int i = 0; i < MAX_PIN; i++) {
                Json::Value jsonval;
                jsonval["name"] = i;
                jsonval["mode"] = pin_info[i].mode;
                jsonval["value"] = pin_info[i].value;
                jsonval["pwm_value"] = pin_info[i].pwm_value;
                jsonval["pull_mode"] = pin_info[i].pull_mode;

                pin_info[i].read_value = digitalRead(i);
                jsonval["read_value"] = pin_info[i].read_value;

                jsonarray.append(jsonval);
            }
            (*send_root)["pwm_clock"] =   pwm_clock;
            (*send_root)["pwm_range"] =   pwm_range;
            (*send_root)["pwm_mode"] = pwm_mode;
            (*send_root)["pin_info"] = jsonarray;
        }
        
        else if(action == "mode") {
            int value;  
            value = (*recv_root)["value"].asInt();

            if(value >= 0 && value <=3) {
                pin_info[pin_num].mode = value;
                pin_info[pin_num].if_change = true;
            }
        }else if(action == "value") {   
            int value;  
            value = (*recv_root)["value"].asInt();

            if(value >= 0 && value <=1) {
                pin_info[pin_num].value = value;
                pin_info[pin_num].if_change = true;
            }
        }else if(action == "pwm_value") {
            int value;  
            value = (*recv_root)["value"].asInt();

            pin_info[pin_num].pwm_value = value;
            pin_info[pin_num].if_change = true;
        }else if(action == "pwm_clock") {
            int value;  
            value = (*recv_root)["value"].asInt();
            pwm_clock = value;
            if_change = true;
        }else if(action == "pwm_mode") {
            int value;  
            value = (*recv_root)["value"].asInt();

            if(value >= 0 && value <=1) {
                pwm_mode = value;
                if_change = true;
            }
        }else if(action == "pwm_range") {
            int value;  
            value = (*recv_root)["value"].asInt();

            if(value >= 0 && value <=1) {
                pwm_range = value;
                if_change = true;
            }
        }else if(action == "pull_mode") {
            int value;  
            value = (*recv_root)["value"].asInt();

            if(value >= 0 && value <=2) {
                pin_info[pin_num].pull_mode = value;
                pin_info[pin_num].if_change = true;
            }
        }


        for(int i = 0; i < MAX_PIN; i++) {
            if(pin_info[i].if_change) {
                pinMode(i, pin_info[i].mode);
                switch(pin_info[i].mode) {
                    case INPUT:
                        if(pin_info[i].pull_mode >= 0)
                            pullUpDnControl(i, pin_info[i].pull_mode );
                        break;
                    case OUTPUT: 
                        if(pin_info[i].value >= 0)
                            digitalWrite(i, pin_info[i].value);
                        break;
                    case PWM_OUTPUT:
                        if(pin_info[i].pwm_value >= 0)
                            pwmWrite(i, pin_info[i].pwm_value ); 
                        break;
                    case GPIO_CLOCK: 
                        break;
                }
                pin_info[i].if_change = false;
            }

        }
        //pwm_status
        if(if_change) {
            if(pwm_mode >= 0)
                pwmSetMode(pwm_mode);
            if(pwm_range >= 0)
                pwmSetRange(pwm_range);          
            if(pwm_clock >= 0)
                pwmSetClock(pwm_clock);
            if_change = false;
        }

        return 0;
    }

}
