# 하 민주야 내일부터는 열심히 좀 하자 알겠지ㅜㅜ
# a,b 크기 비교
# a,b = map(int, input().split())
# if a > b:
#     print('>')
# elif a < b:
#     print('<')
# else:
#     print('==')

# 시험성적 입력받아 학점 주기
# score = int(input())
#
# if 90 <= score <= 100:
#     print('A')
# elif 80 <= score < 90:
#     print('B')
# elif 70 <= score < 80:
#     print('C')
# elif 60 <= score < 70:
#     print('D')
# else:
#     print('F')

# 윤년 출력
# year = int(input())
#
# if year%4 == 0 and year%100 !=0:
#     print('1')
# elif year%400 == 0:
#     print('1')
# else:
#     print('0')

# 상근날드
hamburger = []
drink = []

sang = int(input())
hamburger.append(sang)
jung = int(input())
hamburger.append(jung)
ha = int(input())
hamburger.append(ha)

coke = int(input())
drink.append(coke)
sprite = int(input())
drink.append(sprite)

minCom = hamburger[0] + drink[0]
for i in range(0, len(hamburger)):
    for j in range(0, len(drink)):
        if minCom > hamburger[i] + drink[j]:
            minCom = hamburger[i] + drink[j]
print(minCom-50)




