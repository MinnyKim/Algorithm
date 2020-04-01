# 실습1
# 평균 점수
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

score_list = [a,b,c,d,e]
for i in score_list:
    if i < 40:
        score_list[score_list.index(i)] = 40
avg = int(sum(score_list)/len(score_list))
print(avg)