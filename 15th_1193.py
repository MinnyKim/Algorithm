# 수학1
# 분수찾기

# 1그룹 - 1/1 (1개)
# 2그룹 - 1/2, 2/1 (2개)
# 3그룹 - 3/1, 2/2, 1/3 (3개)
# 4그룹 - 1/4, 2/3, 3/2, 4/1 (4개)

# 공차 = 1
# n그룹 까지의 총 항 개수 = n(n+1)/2

# 홀수그룹은 분자가 n으로 시작해서 down 분모는 1로 시작해서 up
# 즉 분모가 그 그룹에서 순서를 나타냄

# 짝수그룹은 분자가 1로 시작해서 up 분모는 n으로 시작해서 down
# 분자가 그 그룹에서 순서를 나타냄

# 분자 + 분모 = n+1

x = int(input())

# 그룹 찾기
n = 0
while True:
    if x <= n*(n+1)/2:
        break
    n += 1

# 그룹 내에서 몇번째인지
seq = int(x-(n*(n-1)/2))

# 홀수그룹에서는 분모가 순서를 나타내고
if n % 2 != 0:
    print(f'{n-seq+1}/{seq}')
# 짝수그룹에서는 분자가 순서를 나타낸다
else:
    print(f'{seq}/{n-seq+1}')