import paramiko


private = paramiko.RSAKey.from_private_key_file(filename='/Users/chaoliu/.ssh/id_rsa')
transport = paramiko.Transport(('192.168.161.10', 22))
transport.connect(username='root', pkey=private)

sftp = paramiko.SFTPClient.from_transport(transport)

sftp.get(remotepath='/opt/file_test.txt', localpath='./file001.txt')
sftp.put(localpath='./file001.txt', remotepath='/opt/module.txt')

transport.close()
