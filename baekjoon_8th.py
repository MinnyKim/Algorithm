# 와 나 이정도면 주말 빼고 매일 알고리즘 푸는거같은데?
# 넘나 쀼듯하군요 후후 내일은 좀더 일찍 나와서 토익이랑 자소서도!

# 2884
# 45분 앞당긴 시간 만들기
# 그냥 일어나면 되는걸 뭘 또 알람 시간까지 바꾸니 정말..
# if h == 0:
#     if m <:
#         time = 60*24 + m
#         h = (time-45)//60
#         m = (time-45)%60
#         print(h, m)
# else:
#     time = 60*h + m
#     h = (time-45)//60
#     m = (time-45)%60
#     print(h, m)

# 위의 방법으로 풀때 너무 복잡한게 어렵게 해버렸군 흐음
# h, m = map(int, input().split())
# time = 60*h + m
# if time-45 < 0:
#     time = time + 60*24
# h = (time-45)//60
# m = (time-45)%60
# print(h, m)

# 2577
# a = int(input())
# b = int(input())
# c = int(input())
#
# d = a*b*c
# listD = list(str(d))
# # print(listD)
# for i in range(0, 10):
#     print(listD.count(f'{i}'))

# 3052
# 42로 나눈 distinct 나머지
list1 = []
for i in range(10):
    n = int(input())
    m = n%42
    list1.append(m)
list1 = set(list1)
print(len(list1))
