# 수학1
# ACM 호텔

# h = 층 수, w = 방 수, n = n번째 손님

# 방 배정 순서는 101, 201, 301... h01
#               102, 202, 302... h02
#               .......
#               1..w, 2..w, 3..w ..... h..w

# h는 그냥 100곱하면 됨!
# 호수 = h*100 + w

# n//h + 1 = 호수
# n%h = 층수
'''
t = int(input())

listT = []
for i in range(t):
    h,w,n = map(int, input().strip().split())
    temp_list = [h,w,n]
    listT.append(temp_list)
# print(listT)


for i in listT:
    if i[2]%i[0] == 0:
        n_ho = i[2]//i[0]
        n_th = i[0]
    else:
        n_ho = i[2]//i[0]+1
        n_th = i[2]%i[0]
    print(n_th*100 + n_ho)
    # n_ho = i[2]//i[0] + 1
    # n_th = i[2]%i[0]
    # print(n_th*100 + n_ho)

'''

# 한 개 배열만 인풋받아서 풀어보기

h,w,n = map(int, input().strip().split())
# if n == 1:
#     n_ho = 1
#     n_th = 1
if n%h == 0:
    n_ho = n//h
    n_th = h
else:
    n_ho = n//h+1
    n_th = n%h
print(n_th*100 + n_ho)

'''
    if i[0]*i[1] == i[2]:
        n_ho = i[1]
        n_th = i[0]
    else:
        if i[2]%i[0] != 0:
            n_th = i[2]%i[0]
            n_ho = i[2]//i[0]+1
        else:
            n_th = i[2]//i[0]
            n_ho = i[0]
    print(n_th*100 + n_ho)
'''