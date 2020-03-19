# 함수
# 정수 N개의 합
# def solve(a):
#     ans = 0
#     for i in a:
#         ans += i
#     return ans


# def solve(a):
#     ans = 0
#     n = len(a)
#     for i in range(0,n):
#         ans += a[i]
#     return ans

def solve(a):
    return sum(a)

print(solve([1,2,3]))