## 행렬 m1 * m2

m1 = [[1,2,3],
      [4,5,6],
      [7,8,9]]
m2 = [1,0,1]
m3 = []

num = 0
for i in range(0, len(m2)):
    for j in range(0, len(m1[0])):
        num += (m1[i][j] * m2[j])
    m3.append(num)
    num = 0
print(m3)
