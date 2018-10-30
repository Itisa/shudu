
import random

def make_shudu():
	x = []
	y = []
	z = []
	for i in range(9):
		x.append([] * 9)
	for i in range(9):
		y.append([] * 9)
	for i in range(9):
		z.append([] * 9)
	o = -1
	while True:
		o += 1
		for i in range(9):
			if o == 8 and i == 8:
				for n in range(9):
					if not n+1 in x[8]:
						x[8].append(n+1)
						return x
			else:
				if {1,2,3,4,5,6,7,8,9}.issubset(set(x[o]).union(set(y[i])).union(set(z[int(o/3)*3+int(i/3)]))):				
					return make_shudu()									
			while True:
				num = random.randint(1,9)
				if num in x[o] or num in y[i] or num in z[int(o/3)*3+int(i/3)]:
					pass
				else:
					break
			x[o].append(num)
			y[i].append(num)
			z[int(o/3)*3+int(i/3)].append(num)

if __name__ == '__main__':	
	a = make_shudu()
	for i1 in a:
		print(i1)
	
			