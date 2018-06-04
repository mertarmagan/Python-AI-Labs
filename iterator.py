
x = 0
if x < 2:
    print([])
    exit(0)

prime_arr = [2]

for i in range(3, x + 1, 1):
    for j in range(0, prime_arr.__len__(), 1):
        if i % prime_arr[j] == 0:
            break

    if j == prime_arr.__len__() -1:
        prime_arr.append(i)

for i in prime_arr:
    print(i)

print("array.len:", prime_arr.__len__())
