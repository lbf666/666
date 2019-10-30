import paramiko


private = paramiko.RSAKey.from_private_key_file(filename='/Users/chaoliu/.ssh/id_rsa')
transport = paramiko.Transport(('192.168.161.10', 22))
transport.connect(username='root', pkey=private)
client = paramiko.SSHClient()
client._transport = transport

_, stdout, stderr = client.exec_command(command='cat /etc/shadow', timeout=1)
print(stdout.read().decode('utf-8'))
print(stderr.read().decode('utf-8'))

transport.close()
