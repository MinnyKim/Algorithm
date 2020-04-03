# 문자열
# 단어 공부

import sys
s = list(sys.stdin.readline().rstrip().upper())

cnt_list = []
words_list = list(set(s))

for i in words_list:
    temp = s.count(i)
    cnt_list.append(temp)

max_val = max(cnt_list)
if cnt_list.count(max_val) > 1:
    print('?')
else:
    max_idx = cnt_list.index(max_val)
    print(words_list[max_idx])


# ㅅㅂ 존나게 어이없지만 이건 시간초과 나온거ㅎ
# 진짜 뒤지고 싶냐ㅎ

'''
import sys
s = list(sys.stdin.readline().upper())
cnt_list = []
for i in s:
    temp = s.count(i)
    cnt_list.append(temp)

max_val = max(cnt_list)
if max_val != cnt_list.count(max_val):
    print('?')
else:
    max_idx = cnt_list.index(max_val)
    print(s[max_idx])
'''


# length = len(s)
# for i in range(length):
#     cnt = 0
#     for j in s:
#         if s[i] == j:
#             cnt += 1
#     cnt_list.append(cnt)
#
# max_val = max(cnt_list)
# if max_val == cnt_list.count(max_val):
#     max_idx = cnt_list.index(max_val)
#     print(s[max_idx])
# else:
#     print('?')








# 내 생각엔 dictionary 때문에 시간이 초과되는거 가타
# 는 아니었어 count 함수를 문자열의 처음부터 끝까지 돌렸기 때문이야
'''
# 알파벳 별 빈도수 dictionary
dict_sum = {}
for i in s:
    dict_sum[i] = s.count(i)


# 빈도수만으로 구성된 list
values_list = list(dict_sum.values())
max_val = max(values_list)

# max 값 두개 이상인지 체크하기
if values_list.count(max_val) > 1:
    print('?')
else:
    max_key = max(dict_sum, key=dict_sum.get)
    print(max_key)
'''

# input 을 sys 로 바꿨는데도 시간 초과임 ㅎ


'''
# 최대값 삭제된 list 만들기 위해 복사
max_deleted_list = values_list[:]

# 최대값 모두 제거
while True:
    max_deleted_list.remove(max_val)
    if max_deleted_list.count(max_val) == 0:
        break

# 최대값이 여러개인지 확인 후 출력
if (len(values_list)-1) != len(max_deleted_list):
    print('?')
else:
    max_key = max(dict_sum, key=dict_sum.get)
    print(max_key)
'''

# 도대체 왜 두개 다 시간 초과냐 이말이야~~!!!~!!!!

'''
# list 내에서 max값 가진 인덱스만 뽑아서 list 만들기
max_idx = [i for i in range(len(values_list)) if values_list[i] == max_val]

# max 값이 여러개인지 체크 후 출력
if len(max_idx) > 1:
    print('?')
else:
    for alpha, cnt in dict_sum.items():
        if cnt == max_val:
            print(alpha)
'''