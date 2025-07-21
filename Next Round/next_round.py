n, k = map(int, input().split())
a = list(map(int, input().split()))
print(sum(i >= a[k-1] and i > 0 for i in a))
