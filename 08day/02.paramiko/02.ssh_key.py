import paramiko


ssh_connect = paramiko.SSHClient()
ssh_connect.set_missing_host_key_policy(paramiko.AutoAddPolicy())
pkey = paramiko.RSAKey.from_private_key_file('id_rsa')
ssh_connect.connect(
    hostname='39.100.110.135',
    port=22,
    username='root',
    pkey=pkey
)

stdin, stdout, stderr = ssh_connect.exec_command(command='ls -l /etc')
print(stdout.read().decode('utf-8'))

ssh_connect.close()
