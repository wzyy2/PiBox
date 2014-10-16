#ifndef _SERIAL_H_
#define _SERIAL_H_

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <termios.h>
#include <errno.h>
#include <string.h>
#include <time.h>


class Serial
{
public:
    Serial(char *dev);
    ~Serial();

    bool OpenDev(int oflag);  //O_RDWR|O_NDELAY
    bool CloseDev();

    ssize_t PutData(const void *buf, size_t n);
    ssize_t GetData(void *buf, size_t nbytes) ;
    unsigned short CalCrc(unsigned char *data, int data_len,unsigned short init_val_of_crc);
    void ConfigS();

    int set_parity(int databits, int stopbits, int parity);
    void set_speed(int speed);


private:
    int fd_;
    char *dev_name_;
};


//    dev = new Serial("/dev/ttyUSB0");
//    dev->OpenDev(O_RDWR);
//    dev->ConfigS(); //it's so important that we must face this.
//    dev->set_speed(115200);
//    dev->PutData("hello",5);


#endif
