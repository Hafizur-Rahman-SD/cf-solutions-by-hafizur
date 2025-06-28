liked_numbers = []
i = 1
while len(liked_numbers) < 1000:
    if i % 3 != 0 and i % 10 != 3: 
        liked_numbers.append(i)
    i += 1


t = int(input())
for _ in range(t):
    k = int(input())
    print(liked_numbers[k-1]) 