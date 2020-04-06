# 수학1
# 벌집

# {1, 7, 19, 37, 61, ...}
# 공차 d = 6n
# 일반항 An = 2+3n(n-1)

# 1 : 1개
# 2 ~ 7 : 2개
# 8 ~ 19 : 3개
# 20 ~ 37 : 4개
# 38 ~ 61 : 5개

# 루프가 한번 돌때마다 += 1

n = int(input())
# while True:
#     a = 2 + 3*i*(i-1)
#     b = 2 + 3*i*(i+1)
#     if n in range(a,b):
#         print(i+1)
#         break
#     i += 1
if n == 1:
    print(1)
else:
    i = 0
    while True:
        a = 2 + 3*i*(i+1)
        if n < a:
            print(i+1)
            break
        i += 1