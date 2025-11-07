import sys

number = int(sys.argv[1])  # 명령행 인자 입력

for i in range(1, number + 1):  # 1부터 number까지 반복
    if number % i == 0:         # 나머지가 0이면 약수
        print(i, end=" ")

print()
