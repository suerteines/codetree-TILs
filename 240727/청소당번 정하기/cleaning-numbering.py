n = int(input())

cnt_1 = 0
cnt_2 = 0
cnt_3 = 0
for i in range (n):
    if i % 12 == 0:
        cnt_3 += 1
    elif i % 3 == 0:
        cnt_2 += 1
    elif i % 2 == 0:
        cnt_1 += 1

print(cnt_1, cnt_2, cnt_3)