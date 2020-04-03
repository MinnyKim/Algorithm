# 문자열
# 그룹 단어 체커

n = int(input().rstrip())

# input 받은 단어 철자 하나하나씩 중첩리스트안에 넣기
words_list = []
for i in range(n):
    temp = list(input().rstrip())
    words_list.append(temp)
print(words_list)

# 각 단어의 unipue 철자있는 리스트 만들기
unique_word = []
for i in words_list:
    temp = list(set(i))
    unique_word.append(temp)
print(unique_word)

'''
# 연속되는 철자 제거한 리스트 만들기
for i in words_list:
    for j in range(0, len(i)-1):
        if i[j] == i[j+1]:
            i[j] = 0
print(words_list)

cnt = 0
for i in range(len(words_list)):
    if len(words_list[i])-words_list[i].count(0) == len(unique_word[i]):
        cnt += 1
print(cnt)
'''

# 구글링해서 해보기
result_temp = []
result_list = []
for i in words_list:
    result_temp.append(i[0])
    for j in range(1, len(i)):
        if i[j] != i[j-1]:
            result_temp.append(i[j])
    result_list.append(result_temp)
    result_temp= []
print(result_list)


cnt2 = 0
for i in range(len(words_list)):
    if len(result_list[i]) == len(unique_word[i]):
        cnt2+= 1
print(cnt2)