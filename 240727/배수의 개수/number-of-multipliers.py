cnt_1 = 0
cnt_2 = 0

for i in range (10):
    num = int(input())
    if num % 3 == 0:
        cnt_1 += 1
    if num % 5 == 0:
        cnt_2 += 1

print(cnt_1, cnt_2)