def analysisCode(filepath, *args):
    code = {}
    with open(file=filepath, mode='r') as log:
        for lines in log.readlines():
            scode = lines.split()[8]
            if scode in args:
                if scode in code.keys():
                    code[scode] += 1
                else:
                    code.setdefault(scode, 1)
    return dict(sorted(code.items(), key=lambda x: x[1], reverse=True))
