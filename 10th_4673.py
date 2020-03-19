# 함수
# 셀프 넘버
def d(n):
    m = n
    for i in str(n):
        m += int(i)
    return m

# 함수 d 적용한 10000이하 수 리스트
list_a = []
for i in range(10000):
    list_a.append(d(i))

# 1 ~ 10000 리스트
list_b = []
for i in range(10000):
    list_b.append(i)

# 집합으로 타입 변형 후 중복값제거, 차집합 가능
s1 = set(list_a)
s2 = set(list_b)

self_numbers = list(s2-s1)
self_numbers = sorted(self_numbers)

for i in self_numbers:
    print(i)
