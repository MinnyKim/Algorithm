# 수학 1
# 설탕배달

n = int(input())

case_list = []
N_5 = n // 5

for i in range(N_5, -1, -1):
    n_5 = n-(i*5)
    if n_5%3 == 0:
        a = n_5//3
        b = i
        case_list.append(a+b)

if len(case_list) == 0:
    print(-1)
else:
    print(min(case_list))


