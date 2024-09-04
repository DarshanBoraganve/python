s1='darshan'
ra=''
j=len(s1)-1
for i in range(0,j+1):
         if i%2==0:
               ra=ra+s1[j].upper()
         else:
               ra=ra+s1[i].lower()      
         j-=1
print(ra) 