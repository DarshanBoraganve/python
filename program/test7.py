
s1="ScgdSMBcc"
lower=[]
upper=[]
for i in s1:
     if i.islower():
         lower.append(i)
     else:
         upper.append(i)
h=''.join(lower+upper)
print(h)