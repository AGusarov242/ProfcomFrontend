'''k = list(input().split())
v = int(k[0])*(int(k[1]))
b = int(k[2])*(int(k[3]))
if v > b :
	print('M')
elif v == b :
	print('E')
else:
	print('P')'''

'''k = list(input().split())
d = ['!', '.', ':', ';', ',', '?']
c = 0
b = 0
r = 0 
u = 0
for i in range(len(k)):
	for j in range(len(k[i])):
		if k[i][j] != '-' and not k[i][j].isalpha() :
			b = b + 1
	print(b)
	if b != 0:
		c = c + 1
	b = 0
	if k[i] in d:
		c = c + 1;
print(len(k)-c)'''
'''k = list(input().split())
c = 0
b = 0
r = 0 
u = 0
for i in range(len(k)):
	if len(k[i]) < 2:
		if k[i].isalpha():
			u = u + 1
	for j in range(len(k[i])):
		if k[i][j] != '-':
			b = b + 1
		if k[i][j].isalpha():
			c = c + 1
		if k[i][j] != '-' and not k[i][j].isalpha():
			r = r + 1
	if b > 0 and c > 0 and r == 0:
		u = u + 1
	b = 0
	c = 0
	r = 0
print(u)'''

'''def isPalindrom(s, l, r):
	l1 = l
	r1 = r
	while l <= r:
		if s[l:l1] != s[r1:r]:
			return False
		l1 += 1
		r1 -= 1
	return True

s = input()
if isPalindrom(s, 0, len(s)):
	print('1')'''



'''a = str(input())
b = a[::-1]
k = int(len(a)/2)
print("yes" if a[0:k] == b[0:k] else "no")'''

'''def ispol(a):
	b = a[::-1]
	k = int(len(a)/2)
	if a[0:k] == b[0:k] :
		return True
	else:
		return False

k = input()
max = -1
pol = ''
for i in range(len(k)):
	for j in range(len(k)+1):
		if ispol(k[i:j]) and len(k[i:j])>max:
			max = len(k[i:j])
			pol = k[i:j]
print(max)
print(pol)'''

'''k = int(input())
v = int(input())
b = 0
j = 0
for i in range(v):
	c = int(input())
	if i != j:
		continue
	if c == 1:
		b = b + 1
		j = i + k
	if c == 0:
		j = j + 1
		continue
print(b)'''


#for i in len(k):
#if i <= len - 2 and i > =1 k[i]=='-' and k[i - 1].isalpha() and k[i + 1].isalpha() 

'''k = list(input().split())
c = 0
b = 0
r = 0 
u = 0
f = 0
for i in range(len(k)):
	if len(k[i]) < 3:
		for j in range(len(k[i])):
			if k[i][j].isalpha():
				f = f + 1
		if f == len(k[i]):
			u = u + 1
		f = 0
	else:
		for j in range(len(k[i])):
			if j <= (len(k[i])-2) and j >= 1 and k[i][j]=='-' and k[i][j-1].isalpha() and k[i][j+1].isalpha():
				b = b + 1
			if k[i][j].isalpha():
				c = c + 1
		if b+c == len(k[i]):
			u = u + 1
		b = 0
		c = 0'''

		'''if k[i][j] != '-' and not k[i][j].isalpha():
			r = r + 1
	}
	if b > 0 and c > 0 and r == 0:
		u = u + 1
	b = 0
	c = 0
	r = 0'''
#print(u)