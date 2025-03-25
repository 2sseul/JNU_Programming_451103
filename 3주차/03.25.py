# 짝수 홀수 판별

num = int(input("숫자를 입력하세요: "))

if(num % 2 == 0):
    print("짝수입니다")
else:
    print("홀수입니다")

# input 받은 수가 소수일 경우 처리

number = float(input("숫자를 입력하세요: "))

if(int(number) != number):
    print("소수입니다")
else:
    print("정수입니다")

# for문 
# for i in range(start.stop.step):

for i in range(0, 10):
    print(i)

# 1부터 100까지 짝수만 더해라
answer = 0
for i in range(1, 101):
    if(i % 2 == 0):
        answer += i
print(answer)

# 구구단 출력 2단부터 9단까지
for i in range(2, 10):
    for j in range(1, 10):
        print(i, " * ", j, " = ", i*j)

# 몇단 출력할지 물어보고 그 단 출력
num = int(input("몇 단을 출력할까요?: "))

for i in range(1, 10): 
    print(f"{num} * {i} = {num*i}")

# -------------------------
answer = ""
for i in range(1, 6):
    for j in range(0, i):
        answer += "*"
    print(answer)
    answer = ""
    
    # 개행하지 않고 문자열을 붙여 쓰려면 print("문자열", end="") 사용해야한다
for i in range(1, 6):
    for j in range(0, i):
        print("*", end="")
    print()

# n!
