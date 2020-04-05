# 수학 1
# 손익분기점
a, b, c = map(int, input().split())
x = 0
if c > b:
    x = a//(c-b)
    print(x+1)
else:
    print(-1)



# if c < b:
#     print(-1)
# elif c == b:
#     print(-1)
# else:
#     while True:
#         x += 1
#         if c * x > a + b * x:
#             break
#     print(x)

# while True:
#     x += 1
#     if c * x > a + b * x:
#         print(x)
#         break
#     elif c == b:
#         print(-1)
#         break
#     elif c < b:
#         print(-1)
#         break

# while b != c:
#     x += 1
#     if c * x > a + b * x:
#         break
#         print(x)
# print(-1)


# 첫번째 방법
'''
a, b, c = map(int, input().split())
x = 0
while True:
    x += 1
    if c * x > a + b * x:
        print(x)
        break
    elif c == b:
        print(-1)
        break
'''
# 두번째 방법
'''
a, b, c = map(int, input().split())
x = 0
while True:
    x += 1
    if c * x > a + b * x:
        break
        print(x)
    if c == b:
        break
        print(-1)
'''