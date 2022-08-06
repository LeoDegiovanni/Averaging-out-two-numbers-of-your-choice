print("I'm going to average two of your numbers.")
x = input("Type a random number: ")
y = input("Type another random number, but make it less, or equal, than your first one: ") 

while x < y:
	print("Try again.")
	x = input("Type a random number: ")
	y = input("Type another random number, but make it less than your first one: ")

x = int(x)
y = int(y)

z = (x - y) / 2
w = int(z)

if z == w:
	v = x - z
	v = int(v)
	print(v)
else:
	u = float(z)
	v = x - z
	v = float(v)
	print(v)



