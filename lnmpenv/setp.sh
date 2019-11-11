#!/usr/bin/env bash
#
# author by hlions

PASSWORD=123456

systemctl start mariadb

sleep 2

mysqladmin -uroot password "123456"
if [ $? -ne 0 ];then
  /usr/bin/expect <<-ROF
  spawn mysqladmin -uroot -p password "123456"
  expect "*password*" { send "${PASSWORD}\r" }
  expect eof
ROF
fi
