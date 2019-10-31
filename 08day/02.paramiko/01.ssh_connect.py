# paramiko: SSH; SFTP
# SSH: password, rsa_key, transport
import paramiko


ssh_connect = paramiko.SSHClient()
ssh_connect.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_connect.connect(
    hostname='39.100.110.135',
    port=22,
    username='username',
    password='******'
)

stdin, stdout, stderr = ssh_connect.exec_command(command='ls -l /etc')
print(stdout.read().decode('utf-8'))

ssh_connect.close()
