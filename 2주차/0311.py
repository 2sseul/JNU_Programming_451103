# 3월 11일 강의코드

num = int(input("정수를 입력하세요: "))
print("입력한 숫자: ", num)

a = int(input("a: "))
b = int(input("b: "))
print("a + b =", a+b)
print("a * b = ", a*b)
print("a / b = ", a/b)
print("a // b = ",a//b)
print("a % b =", a%b)
print("a ** b=", a**b)

# 문자열을 입력받아 그 문자를 출력
word = input("문자를 입력하세요: ")
print(word)

# 문자열을 3개 입력받아 그 문자를 출력
words = []
for i in range(0, 3):
    words.append(input(f"{i+1}번째 문자열을 입력하세요: "))
print(words)

# 문자열을 입력받아 마지막 3글자를 출력
sentence = input("문자열을 입력하세요: ")
print(sentence[-3:])
print(sentence[len(sentence)-3:len(sentence)])
