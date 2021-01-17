def test_parallel(n):
    return n+1

@parallel
def test_parallel2(n):
    return n+1

x = [1, 2, 3, 4, 5]
y = []
for i in x:
    y.append(test_parallel(i))
y

z = list(test_parallel2(x))
ans = [None]*len(z)
for j in range(len(z)):
    ans[j] = z[j][1]
ans
