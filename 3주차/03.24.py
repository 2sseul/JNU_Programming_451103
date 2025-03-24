a = 3
b = 5
c = a >= b
d = a ** b
print("a = ", a)
print("b = ", b)
print("c = ", c)
print("d = ", d)

# 1학기 학점 입력, 2학기 학점 입력, 봉사시간 입력 후
# 학점 평균이 3.0을 넘기고 봉사시간이 10시간 이상일 경우 장학금 True

grade1 = float(input("1학기 학점 입력: "))
grade2 = float(input("2학기 학점 입력: "))
time = float(input("봉사시간 입력: "))

average = (grade1 + grade2) / 2

result = (average >= 3.0) and (time >= 10)

print("장학금 대상 여부: ", result)

# ---------------------------------------------

# 조건문: 나이를 물어보고 20 <= 입장 <= 25, 20 > age 집으로 가, 입장불가
age = int(input("나이를 입력하세요: "))

if age >= 20 and age <= 25 :
    print("입장")
elif age < 20 :
    print("집으로 가!")
else :
    print("입장 불가")
