# 要跟张老师要一行服务器的模板
# | grep是什么，查找匹配吗
# 查询命令都查出来了，现在需要写到脚本里，并对终端输出的信息做统计 15:48

op网ip	业务网ip	
操作系统：
    cat /etc/os-release //其他几个命令测试服务器都不支持
        PRETTY_NAME="Ubuntu 22.04.1 LTS"
        NAME="Ubuntu"
        VERSION_ID="22.04"
        VERSION="22.04.1 LTS (Jammy Jellyfish)"
        VERSION_CODENAME=jammy
        ID=ubuntu
        ID_LIKE=debian
        HOME_URL="https://www.ubuntu.com/"
        SUPPORT_URL="https://help.ubuntu.com/"
        BUG_REPORT_URL="https://bugs.launchpad.net/ubuntu/"
        PRIVACY_POLICY_URL="https://www.ubuntu.com/legal/terms-and-policies/privacy-policy"
        UBUNTU_CODENAME=jammy
    lsb_release -a  //测试服务器不支持(关键词是Description)
        No LSB modules are available.
        Distributor ID: Ubuntu
        Description:    Ubuntu 22.04.1 LTS
        Release:        22.04
        Codename:       jammy
    cat /etc/redhat-release    //这种方法只适合Redhat系的Linux：(关键词是Red Hat && release7.9)
        Red Hat Enterprise Linux Server release 7.9 (Maipo)
    cat /etc/issue  //测试服务器不支持
        Ubuntu 22.04.1 LTS \n \l

CPU型号：
    lscpu | grep "Model name"
        Model name:                      Intel(R) Core(TM) i5-9300H CPU @ 2.40GHz
CPU个数：
    lscpu | grep "CPU(s):" //关键词是CPU(s): 输出第二行没用
        CPU(s):                          1
        NUMA node0 CPU(s):               0
CPU主频：
    lscpu | grep "CPU MHz:"
        CPU MHz:                         2400.000
	
内存大小：
    free -h
                       total        used        free      shared  buff/cache   available
        Mem:           1.9Gi       976Mi        78Mi        13Mi       908Mi       816Mi
        Swap:          2.1Gi       0.0Ki       2.1Gi

！！nvme数量	
！！nvme单块大小
    nvme list  //没有nvme，不知道读上来是啥样的
        Node                  SN                   Model                                    Namespace Usage                      Format           FW Rev  
--------------------- -------------------- ---------------------------------------- --------- -------------------------- ---------------- --------

SSD数量	SSD单块大小	总硬盘大小	
    lsblk --list | grep 'disk'

网卡型号和数量：//服务器会有多个网卡，不同型号有多种，需要计数，我的天……
    lspci | grep Ethernet
    
内核版本：
    cat /proc/version
        Linux version 5.19.0-50-generic (buildd@lcy02-amd64-030) (x86_64-linux-gnu-gcc (Ubuntu 11.3.0-1ubuntu1~22.04.1) 11.3.0, 
        GNU ld (GNU Binutils for Ubuntu) 2.38) #50-Ubuntu SMP PREEMPT_DYNAMIC Mon Jul 10 18:24:29 UTC 2023	
    uname -a
        Linux ics-virtual-machine 5.19.0-50-generic #50-Ubuntu SMP PREEMPT_DYNAMIC Mon Jul 10 18:24:29 UTC 2023 x86_64 x86_64 x86_64 GNU/Linux

查看磁盘使用： //df 命令用于显示文件系统的磁盘空间使用情况，而 -h 选项会以更易读的方式显示数据大小。
    df -h
        Filesystem      Size  Used Avail Use% Mounted on
        tmpfs           197M  1.8M  195M   1% /run
        /dev/sda3        20G   17G  1.1G  95% /
        tmpfs           982M     0  982M   0% /dev/shm
        tmpfs           5.0M  4.0K  5.0M   1% /run/lock
        /dev/sda2       512M  6.1M  506M   2% /boot/efi
        tmpfs           197M   80K  197M   1% /run/user/127
        tmpfs           197M   72K  197M   1% /run/user/1000