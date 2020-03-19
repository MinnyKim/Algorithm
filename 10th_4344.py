# 평균은 넘겠지
c = int(input())
case_list = []
for i in range(c):
    case = list(map(int, input().split()))
    case_list.append(case)

# 평균 리스트 만들기
mean_list = []
for i in range(0, len(case_list)):
    sum = 0
    for j in range(1, len(case_list[i])):
        sum += case_list[i][j]
    mean = sum/case_list[i][0]
    mean_list.append(mean)
    del case_list[i][0]


# 평균 넘는 비율 구하기
for i in range(0, len(case_list)):
    cnt = 0
    for j in case_list[i]:
        if j > mean_list[i]:
            cnt += 1
    rate = cnt/len(case_list[i])*100
    print(f"{'%.3f'%rate}%")