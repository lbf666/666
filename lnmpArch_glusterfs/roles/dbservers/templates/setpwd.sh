#!/usr/bin/env bash
#
# author by hlions
# date: 2019/11/12

/bin/systemctl start mysqld
sleep 5

INITP=$(grep 'temporary password' /var/log/mysqld.log | awk '{ print $NF }')
NEWP="(Hlions..1112)"

rpm -qa | grep expect &>/dev/null
if [ $? -ne 0 ];then
  yum -y install expect
fi

/usr/bin/expect <<-ROF
spawn mysql -uroot -p
expect "Enter password:" { send "${INITP}\r" }
expect "mysql>" { send "ALTER USER 'root'@'localhost' IDENTIFIED BY \"${NEWP}\";\r" }
expect "mysql>" { send "flush privileges;\r" }
expect "mysql>" { send "exit\r" }
expect eof
ROF

/bin/systemctl restart mysqld
