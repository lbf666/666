import paramiko


client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
private = paramiko.RSAKey.from_private_key_file(filename='/Users/chaoliu/.ssh/id_rsa')
client.connect(
    hostname='192.168.161.10',
    port=22,
    username='root',
    pkey=private
)

_, stdout, stderr = client.exec_command(command='cat /etc/passwd', timeout=1)
print(stdout.read().decode('utf-8'))
print(stderr.read().decode('utf-8'))

client.close()

