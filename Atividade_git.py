v = [9, 5, 6, 1, 8, 7, 2, 4, 3]
n = len(v)
for i in range(n - 1):
    ok = True
    for j in range(n - 1 - i):
        if v[j] > v[j+1]:
            v[j], v[j+1] = v[j+1], v[j]
            ok = False
    if ok:
        break
print(v)
