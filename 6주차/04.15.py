alist = [] # 빈 리스트를 선언하면, "가비지값"이라고 함
print(alist)
alist.append(30)
print(alist)
print(alist[0])
alist[0] = 20
print(alist[0])
alist.append("홍길동")
print(alist)
alist.insert(1, "김길동")
print(alist)

# ------------
# 괄호넣기, 밑줄에 들어갈 코드 작성, 코드의 결과를 쓰라고 시험에 낼 것
# 아래문제처럼 낼 것 같음 ~

alist = []
alist.append(30)
print(alist[0])
alist.append("홍길동")
alist.append("홍길동")
alist.append("양길동")
alist.insert(1, "김길동")
alist.remove("김길동")
del(alist[1])
name = alist.pop()
print(alist)
print(name)

# --------------
# 시험에 내면 많이 틀린다함

alist = [1,2,3,4,5,6,7,8,9]
print(alist[2:5])
print(alist[4:])
print(alist[:6])
print(alist[:])

# ----------
# sorted도 확인할 것

# 수강생 5명의 점수를 입력받아 평균을 출력하는 프로그램
# 리스트 없이 구현

num = 5
result = 0
for i in range(1, num+1):
    score = int(input(f'{i}번째 학생의 점수를 입력하세요: '))
    result += score
print(f"수강생 {num}명의 평균은 {result/num}점 입니다.")

# 리스트 이용한 구현
students = []
for i in range(1, num+1):
    score = int(input(f'{i}번째 학생의 점수를 입력하세요: '))
    students.append(score)
result = sum(students)
print(f'수강생 {num}명의 평균은 {result/num}점 입니다.')

student = [int(x) for x in input().split()] # 리스트 컴프리헨션


# 결과 써라, 빈칸 채워라, 오류 고쳐라 ~ => 시험 이런식으로 낼거임