import paramiko


client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(
    hostname='192.168.161.10',
    port=22,
    username='root',
    password='1'
)

_, stdout, stderr = client.exec_command(command='ls adb', timeout=10)
print(stdout.read().decode('utf-8'))
print(stderr.read().decode('utf-8'))

client.close()

