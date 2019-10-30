def ipAnalysis(filepath):
    ips = {}
    with open(file=filepath, mode='r') as log:
        for lines in log.readlines():
            if not lines.split()[0] in ips.keys():
                ips.setdefault(lines.split()[0], 1)
            else:
                ips[lines.split()[0]] += 1
    return dict(sorted(ips.items(), key=lambda x: x[1], reverse=True))

