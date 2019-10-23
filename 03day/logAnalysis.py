# access_log analysis

# awk '{ ips[$1]++ }END{ for(ip in ips){ print ip, ips[ip] } }' access_log

ips = {}
with open(file='access_log', mode='r') as log:
    for lines in log.readlines():
        # lines.split()[0] = ip
        if not lines.split()[0] in ips.keys():
            ips.setdefault(lines.split()[0], 1)
        else:
            ips[lines.split()[0]] += 1
print(ips)

ips_list = []
for items in ips.items():
    ips_list.append(items)
for i in range(len(ips_list)):
    for j in range(len(ips_list) - 1):
        if ips_list[j][1] < ips_list[j+1][1]:
            ips_list[j], ips_list[j+1] = ips_list[j+1], ips_list[j]
print(dict(ips_list))

