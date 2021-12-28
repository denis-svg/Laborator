f = open("in.txt", "r")
lines = f.readlines()
n1 = lines[0].rstrip()
n2 = lines[1].rstrip()
f.close()
n1 = int(n1, 16)
n2 = int(n2, 16)


def gcd(x, y):
	while y:
		x, y = y, x % y
	return x


p = gcd(n1, n2)


if p > n1//p:
	print(p)
else:
	print(n1 // p)

if p > n2//p:
	print(p)
else:
	print(n2 // p)