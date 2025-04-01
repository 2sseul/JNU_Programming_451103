# 입력 1: 정수
# 입력 2: -, +, *, /
# 입력 3: 정수

# num1 = int(input())

# calculate = (input())

# num2 = int(input())

# answer = -1

# if calculate == '-':
#     answer = num1 - num2
# elif calculate == '+':
#     answer = num1 + num2
# elif calculate == '*':
#     answer = num1 * num2
# elif calculate == '/':
#     answer = num1 / num2
# else:
#     print("올바른 입력이 아닙니다.")

# if answer != -1:
#     print(f'정답은 {answer}입니다.')

# 2. 계산기 만들기
# 입력 1 : 정수
# 입력 2 : +,-*,/
# 입력 3 : 정수
# 출력 예
# 5
# *
# 3
# 5*3=15
#  계속하시겠습니까?(y/n)

flag = 'y'
while flag == 'y':
    num1 = int(input("첫번째 숫자를 입력하세요 = "))

    operators = ["+", "-", "*", "/"]
    calculate = input("연산자를 입력하세요 = ")
    while calculate not in operators:
        calculate = input("올바른 연산자를 다시 입력하세요 = ")
    
    num2 = int(input("두번째 숫자를 입력하세요 =" ))

    if calculate == '+':
        print(num1 + num2)
    elif calculate == '-':
        print(num1 - num2)
    elif calculate == '*':
        print(num1 * num2)
    else:
        print(num1 / num2)
    
    flag = input('계속 하시겠습니까? (y/n) =')

    if flag == 'n':
        break
    else:
        continue

# 10진수를 입력받아 2진수를 출력하는 파이썬 코드
num = int(input("숫자를 입력하세요 = "))

transfer = ""

if num == 0:
    transfer = "0"

while num > 0:
    transfer = str(num % 2) + transfer
    num //= 2

print(transfer)
