import paramiko


pkey = paramiko.RSAKey.from_private_key_file('id_rsa')
transport = paramiko.Transport(('39.100.110.135', 22))
transport.connect(pkey=pkey, username='root')
ssh_connect = paramiko.SSHClient()
ssh_connect._transport = transport

stdin, stdout, stderr = ssh_connect.exec_command(command='ls -l /etc')
print(stdout.read().decode('utf-8'))

transport.close()
