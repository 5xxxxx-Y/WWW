f = open('10.txt', 'r')
fi = open('out2.txt', 'w')
while 1:
    a = f.readline().strip()
    if a:
        if len(a) == 16:  # 键盘流量的话len改为16
            out = ''
            for i in range(0, len(a), 2):
                if i+2 != len(a):
                    out += a[i]+a[i+1]+":"
                else:
                    out += a[i]+a[i+1]
            fi.write(out)
            fi.write('\n')
    else:
        break
fi.close()
