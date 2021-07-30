# input N
# loop N and input t, x, y
# check all abs(x+y)<=t and if t is odd x+y is odd, and vice versa
# if so print "YES" else "NO" then return


def traveling():
    N = int(input())
    dt = dx = dy = 0
    for _ in range(N):
        t, x, y = map(int, input().split())
        dt = t - dt
        dx = x - dx
        dy = y - dy
        if abs(dx + dy) > dt or t % 2 != (x + y) % 2:
            return "No"
    return "Yes"


if __name__ == "__main__":
    ans = traveling()
    print(ans)
