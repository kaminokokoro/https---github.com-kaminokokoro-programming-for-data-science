s = input()
count = []
for i in range(0, len(s)):
    count.append(0)
    for j in s:
        if s[i] == j:
            count[i] += 1

max = 0
for i in range(0, len(s)):
    if count[i] > max:
        max = i

print(s[max], count[max])
