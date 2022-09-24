k=input('enter string : ')
l=['a','i','u','e','o']
m=''

for letter in k:
    if letter.lower() not in l:
        m= m+letter
print(m)