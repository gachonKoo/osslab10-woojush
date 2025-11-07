# lab10.py
import sys

n = int(sys.argv[1])            # 명령행 인자
n = abs(n)                      # 음수 들어와도 양의 약수로 처리

divisors = [i for i in range(1, n + 1) if n % i == 0]
print(" ".join(map(str, divisors)))   # 마지막에 공백 없이 한 줄 출력
