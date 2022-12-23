n = 1260
count = 0
quotient = 0
coin_types = [500,100,50,10]

for coin in coin_types:
    quotient = n // coin
    count += quotient
    n %= coin
print(count)
