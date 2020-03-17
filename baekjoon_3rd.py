# 아우 머리가 왤케 아프니 A/B
# a,b = map(int, input().split())
# print(round(a/b,9))

# 사칙연산
# a,b = map(int, input().split())
# print(a+b)
# print(a-b)
# print(a*b)
# print(a//b)
# print(a%b)

# 뭐 구하는 값,,,
# a,b,c = map(int, input().split())
# print((a+b)%c)
# print((a%c+b%c)%c)
# print((a*b)%c)
# print((a%c*b%c)%c)

# 세자리수 x 세자리수
num1 = int(input())
num2 = int(input())

print(num1*(num2%10))
print(num1*((num2%100)//10))
print(num1*((num2%1000)//100))
print(num1*num2)
