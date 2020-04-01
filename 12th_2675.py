# 문자열
# 문자열 반복
t = int(input())
s_list = []
for i in range(t):
    temp = input().split()
    s_list.append(temp)

for i in s_list:
    s = list(i[1])
    r = int(i[0])
    for j in s:
        print(j*r, end='')
    print('')