n, row = int(input()), input()
holder = 1
people = 0
i = 0
while i < len(row):
    if row[i] == 'S':
        holder += 1
        people += 1
        i += 1
    else:
        holder += 1
        people += 2
        i += 2
print(holder if holder < people else people)