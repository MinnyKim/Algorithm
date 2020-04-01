# 문자열
# 알파벳 찾기

s = list(input())
alpha_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
            'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
            'w', 'x', 'y', 'z']
for i in alpha_list:
    if i in s:
        print(s.index(i), end=' ')
    else:
        print(-1, end=' ')



# 이거는 import 해서 하는건데 백준에서는 런타임 에러남
from string import ascii_lowercase
# alpha_list = list(ascii_lowercase)
