import paramiko


pkey = paramiko.RSAKey.from_private_key_file('id_rsa')
transport = paramiko.Transport(('39.100.110.135', 22))
transport.connect(username='root', pkey=pkey)
sftp = paramiko.SFTPClient.from_transport(transport)
# 向远程服务器上传文件
sftp.put(localpath='./exam.py', remotepath='/opt/exam_transport_sftp.py')
# 从远程服务器下载文件到本地
sftp.get(remotepath='/root/er.py', localpath='./er_transport_sftp.py')
transport.close()


def ftpserver(style):
    def get(rpath, lpath):
        sftp.get(remotepath=rpath, localpath=lpath)
        transport.close()
    def put(lpath, rpath):
        sftp.put(localpath=lpath, remotepath=rpath)
        transport.close()
    pkey = paramiko.RSAKey.from_private_key_file('id_rsa')
    transport = paramiko.Transport(('39.100.110.135', 22))
    transport.connect(username='root', pkey=pkey)
    sftp = paramiko.SFTPClient.from_transport(transport)
    if style == 'put':
        return put
    elif style == 'get':
        return get
    else:
        print('check your input! input true: get or put.')


putfile = ftpserver('put')
putfile(lpath='./id_rsa', rpath='/opt/cloud1906_id_rsa')

getfile = ftpserver('get')
getfile(rpath='/root/sftp_transport.txt', lpath='./hellosftp.txt')






