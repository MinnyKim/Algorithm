# 평균
# 세준이의 기말고사 점수조작
n = int(input())
list1 = list(map(int, input().split()))
m = max(list1)

sum = 0
for i in range(0,n):
    list1[i] = list1[i]/m*100
    sum += list1[i]
mean = sum/n
print(mean)