import paramiko
import yagmail
import json


def exec_commands(command):
    transport = paramiko.Transport(('39.100.110.135', 22))
    transport.connect(username='root', pkey=paramiko.RSAKey.from_private_key_file('/Users/liuchao/.ssh/id_rsa'))
    client = paramiko.SSHClient()
    client._transport = transport
    client.exec_command(command=command)
    transport.close()


def gpfile(style):
    def get(rpath, lpath):
        sftp.get(remotepath=rpath, localpath=lpath)
        transport.close()
    def put(lpath, rpath):
        sftp.put(localpath=lpath, remotepath=rpath)
        transport.close()
    pkey = paramiko.RSAKey.from_private_key_file('/Users/liuchao/.ssh/id_rsa')
    transport = paramiko.Transport(('39.100.110.135', 22))
    transport.connect(username='root', pkey=pkey)
    sftp = paramiko.SFTPClient.from_transport(transport)
    if style == 'put':
        return put
    elif style == 'get':
        return get
    else:
        print('check your input! input true: get or put.')


# 上传脚本
put = gpfile('put')
put(lpath='./scripts/cmd_monitor.sh', rpath='/opt/cmd_monitor.sh')

# 执行脚本
exec_commands('bash /opt/cmd_monitor.sh')

# 拉取监控结果
get = gpfile('get')
get(rpath='/monitor/info.json', lpath='./cmd_info.json')

# 构建告警机制
sendmail = yagmail.SMTP(user='hlions@163.com', password='Liuchao0725', host='smtp.163.com')
def contents(device, rate):
    content = [
        "hi:",
        "this mail is warning!",
        "{} rate over 90, current value: {}".format(device, rate)
    ]
    return content

# 判断监控结果
with open(file='cmd_info.json', mode='r') as info:
    content = info.readlines()[-1]
    infos = json.loads(content)
    if infos['cpu'] > 85:
        content = contents('cpu', infos['cpu'])
        sendmail.send(to='bavduer@163.com', subject='cpu warning', contents=content)
    elif infos['memory'] > 10:
        content = contents('memory', infos['memory'])
        sendmail.send(to='bavduer@163.com', subject='memory warning', contents=content)
    elif infos['disk'] > 80:
        content = contents('disk', infos['disk'])
        sendmail.send(to='bavduer@163.com', subject='disk warning', contents=content)
