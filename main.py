# 구현 예제 4-2 답안

h = int(input())

count = 0
for i in range(h + 1):
  for j in range(60):
    for k in range(60):
      # 매 시각 안에 '3'이 포함되어 있다면 카운트 증가
      if '3' in str(i) + str(j) + str(k):
        count += 1

print(count)

for i in range(5):
  print(i)
  print(type(i))

# int형태를 문자열로 바꿔서 3을 카운트하는것이 인상적이다
