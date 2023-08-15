#!/usr/bin/expect -f

# 定义三台机器的IP地址列表
set machines {"192.168.1.1" "192.168.1.2" "192.168.1.3"}

# 循环遍历三台机器
foreach machine $machines {
    # 远程执行命令创建用户和设置密码
    for {set i 1} {$i <= 10} {incr i} {
        set username "test_$i"
        spawn ssh -o StrictHostKeyChecking=no root@$machine "useradd -m -d /sse/$username $username && echo '$username:test@1234' | chpasswd"
        expect "password:"
        send "YOUR_SSH_PASSWORD\r"
        expect eof
    }
}

