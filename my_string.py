'''
Comment goes here
'''

"""
Comment goes here too
"""

name = 'Le Van Linh'
print(name)

newbie = "I'm newbie in Python"
print(newbie)

place = 'I live in "Warabi city"'
print(place)

bio = '''Hi there
I am from Vietnam
work as a software engineer
at System Integrator, Japan'''
print(bio)

linedown = "I'm Vietnamese\nI love IT"
print(linedown)

strA = "Hello"
strB = "World"
strC = strA + "\n" + strB
print(strC)
print(strA * 5)

str1 = "Le Van Linh"
str2 = "Van"
included = str2 in str1
print(included)

firstChar = str1[0]
print(firstChar)
print(type(firstChar))
print(str1[-1])
print(str1[len(str1) - 1])
print(str1[1:5])
print(str1[1:len(str1)])
print(str1[1:None])
print(str1[None:None])
print(str1[:])
print(str1[None:None:1])
print(str1[None:None:-1])
print(str1[None:None:2])

# Casting
cube = int("10") + 5
print(cube)

linh = str(10) + "5"
print(linh)

bk = "Bach Khoa Da Nang"
# In python phai lam cu chuoi the nay
# Vi no la mot hashtable object
bk = bk[None:7] + "0" + bk[8:None]
print(bk)
print(hash(bk))
