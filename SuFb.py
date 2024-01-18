a = 0
b = 1
c = 0

while c < 22:
	if c == 0:
		print(f"{a}" + ", ")
	elif c > 0:
		print(f"{c}" + ", ")
	c = a + b
	b = a
	a = c