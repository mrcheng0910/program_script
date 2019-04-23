# encoding:utf-8
from collections import Counter
fp = open('nohup.out','r')
j = 0
seq_loop_times = []
seq_lose_package = []
total = 0

time_count = Counter()
total_time_count = Counter()

for i in fp.readlines():

    if j == 0:  # 跳过第一行
        j = 1
        continue
    total += 1
    l = i.strip().split()
    loop_time = int(l[4])
    lose_package = int(l[5])
    total_time_count[int(l[1].split(':')[0])] += 1
    if lose_package > 0:
        # print i.strip()
        time_count[int(l[1].split(':')[0])]+=1
        seq_lose_package.append(i.strip())

fp.close()

print '总共探测次数:', total
print '总共丢包数量：', len(seq_lose_package)
print '百分比：', float(len(seq_lose_package))/total

for i,j in time_count.most_common():
    print i,j,float(j)/total_time_count[i]