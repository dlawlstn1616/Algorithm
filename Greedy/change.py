# 가지고 있는 동전 중에서 큰 단위가 항상 작은 단위의 배수이므로 작은 단위의 동전들을 종합해 다른 해가 나올 수 없는 경우
n = 1260
count = 0

coin_types = [500, 100, 50, 10]

for coin in coin_types:
  count += n // coin
  n %= coin

print(count)
