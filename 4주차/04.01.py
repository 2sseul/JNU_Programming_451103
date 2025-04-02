import random

# up down 게임
guess_number = random.randint(1, 100) # 1~100 사이의 난수 발생

print("숫자를 맞혀보세요. (1~100)")

user_number = 0
while user_number != guess_number:
    try:
        user_number = int(input("숫자를 입력하세요: "))
    except ValueError:
        print("숫자를 입력해주세요.")
        continue

    if user_number < 1 | user_number > 100:
        print("숫자는 1~100 사이의 숫자를 입력해주세요.")
        continue
    if user_number < guess_number:
        number_gap = guess_number - user_number
        if number_gap > 70:
            print(f'숫자는 {user_number}보다 매우 큽니다.')
        elif number_gap > 50:
            print(f'숫자는 {user_number}보다 상당히 큽니다.')
        elif number_gap > 20:
            print(f'숫자는 {user_number}보다 다소 큽니다.')
        else:
            print(f'숫자는 {user_number}보다 조금 큽니다.')
        continue
    elif user_number > guess_number:
        number_gap = user_number - guess_number
        if number_gap > 70:
            print(f'숫자는 {user_number}보다 매우 작습니다.')
        elif number_gap > 50:
            print(f'숫자는 {user_number}보다 상당히 작습니다.')
        elif number_gap > 20:
            print(f'숫자는 {user_number}보다 다소 작습니다.')
        else:
            print(f'숫자는 {user_number}보다  조금 작습니다.')
        continue
    else:
        print(f"정답입니다. 입력한 숫자는 {user_number}입니다.")
        break

# 로또 번호 생성기

lottos = []
while len(lottos) != 6:
    tmp_number = random.randint(1, 45)
    if tmp_number in lottos:
        continue
    else: 
        lottos.append(tmp_number)
lottos.sort()
print(f'로또번호는 {lottos} 입니다.')