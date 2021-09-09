

i = 1
count = 0
total = 0
while i <= 120:
    if 120 % i == 0:
        print(i)
        count += 1
        total += i
    i += 1
print(f"120의 약수는 총{count}개입니다.")
print(f"약수의 총 합은 {total}입니다.")
