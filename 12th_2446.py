# 실습 1
# 별찍기-9

n = int(input())
m = 2*n-1
for i in range(m, 0, -2):
    print(' '*((m-i)//2), end='')
    print('*'*i)
for i in range(3, m+2, 2):
    print(' ' *((m-i)//2), end='')
    print('*'*i)



# for i in range(2*n-1, 0, -2):
#     print('{:^{}}'.format(('*'*i), 2*n-1))
# for i in range(3, 2*n+1, 2):
#     print('{:^{}}'.format(('*'/*i), 2*n-1))

