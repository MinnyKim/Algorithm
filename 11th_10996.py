# 실습 1단계
# 별찍기 - 21
n = int(input())
firstLine = []
secondLine = []
if n == 1:
    print('*')
else:
    for i in range(0, n, 2):
        firstLine.append('*')
        secondLine.append(' ')
        if len(firstLine) == n:
            break
        firstLine.append(' ')
        secondLine.append('*')


    # for i in firstLine:
    #     print(i, end='')
    # for j in secondLine:
    #     print(j, end='')

    for i in range(n):
        print(*firstLine, sep="")
        print(*secondLine, sep="")

# print(",".join())


# print(firstLine)
# print(secondLine)
#
# first = str(firstLine)
# print(first, type(first))


# 자 n = 4 일때 우선 찍히는 한세트를 만들어보자
# testList = []
# for i in range(0, n, 2):
#     testList.append('*')
#     if len(testList) == n:
#         break
#     testList.append(' ')
#
# testList2 = []
# for i in range(0, n, 2):
#     testList2.append(' ')
#     if len(testList2) == n:
#         break
#     testList2.append('*')
#
# print(testList)
# print(testList2)