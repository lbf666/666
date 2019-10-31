# 请编写一个程序, 实现基本的终端功能
# root@localhost ~: ls -l /etc
# result = 0
# root@localhost ~: exit
# root@localhost ~: ls /wangbadan

import paramiko


def commands(cm='whoami'):
    pkey = paramiko.RSAKey.from_private_key_file('id_rsa')
    transport = paramiko.Transport(('39.100.110.135', 22))
    transport.connect(pkey=pkey, username='root')
    ssh_connect = paramiko.SSHClient()
    ssh_connect._transport = transport
    stdin, stdout, stderr = ssh_connect.exec_command(command=cm)
    out = stdout.read().decode('utf-8')
    err = stderr.read().decode('utf-8')
    transport.close()
    return out, err


while True:
    exec_command = input('root@localhost ~: ')
    if exec_command in ('exit', 'logout'):
        break
    sout, serr = commands(exec_command)
    if len(sout) != 0:
        print(sout)
    else:
        print(serr)









