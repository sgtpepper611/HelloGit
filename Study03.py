i = 0
while i < 5:
    if i == 3:
        i += 1
        continue
    print(i)   # 0 1 2 4
    i += 1