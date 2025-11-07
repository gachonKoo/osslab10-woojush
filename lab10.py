# lab10.py
import sys

def get_divisors(n: int):
    return [i for i in range(1, n+1) if n % i == 0]

def main():
    if len(sys.argv) >= 2:
        n = int(sys.argv[1])          # 자동채점용: argv로 받음
    else:
        n = int(sys.stdin.readline())  # 로컬 테스트용: 입력 한 줄
    print(*get_divisors(n))            # 약수만 공백으로 출력

if __name__ == "__main__":
    main()
