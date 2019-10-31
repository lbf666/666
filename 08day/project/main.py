import psutil
import yagmail
# https://pypi.org

sendmail = yagmail.SMTP(user='user01@163.com', password='******', host='smtp.163.com')
def contents(device, rate):
    content = [
        "hi:",
        "this mail is warning!",
        "{} rate over 90, current value: {}".format(device, rate)
    ]
    return content


cpu_rate = psutil.cpu_percent(interval=1)
if cpu_rate > 90:
    content = contents('cpu', cpu_rate)
    sendmail.send(to='user02@163.com', subject='cpu warning', contents=content)

memory_rate = psutil.virtual_memory().percent
if memory_rate > 75:
    pass

disk_rate = psutil.disk_usage("/").percent
if disk_rate > 80:
    pass



