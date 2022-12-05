import string
s=input('enter string')
p=string.punctuation
t=""
for i in s:
    if i not in p:
        t=t+i
print(t)
