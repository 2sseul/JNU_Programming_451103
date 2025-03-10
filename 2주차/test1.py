a = 1
b = 2
c = a+b
print(c)

for j in range(2, 10):
    print(f"{j}단 구구단")
    for i in range(1, 10):
        print(f"{j} x {i} = {j * i}")

print("Hello world")

aa = 0.1
bb = 0.2
cc = aa+bb
print(cc)
# 결과는 0.30000000000000004 출력
# why? 
# - 위 코드의 문제는 부동소수점 숫자가 이진수로 표현될 때 정확히 표현되지 않기 때문.
# - 소수점을 이진수로 바꿀 때는 정확하게 바뀌지 않는다는 것 (=완벽하게 처리할 수 없다)
