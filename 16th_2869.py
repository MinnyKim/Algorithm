# 수학1
# 달팽이는 올라가고 싶다

# 굉장히 오랜만에 풀어보는 알고리즘입니다
# 달팽이는 하루에 a-b 만큼 올라간다
# 다만 정상 도착시에는 b만큼 미끄러지지 않는다
# 총 걸리는 일수를 n 이라고 한다면
# v >= an - b(n-1) 이 되는 최초의 값을 구하면 된다
# n에 대해서 정리하면 n >= (v-b)/(a-b)

a, b, v = map(int, input().strip().split())

if (v-b)%(a-b) == 0:
    n = (v-b)//(a-b)
else:
    n = (v-b)//(a-b) + 1
print(n)
