import sys

def digit_sum(n: int) -> int:
    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    return s

def solve():
    data = sys.stdin.read().strip().split()
    t = int(data[0])
    idx = 1
    out = []

    for _ in range(t):
        x = int(data[idx])
        idx += 1

        cnt = 0
        for y in range(x, x + 100):
            if y - digit_sum(y) == x:
                cnt += 1

        out.append(str(cnt))

    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()