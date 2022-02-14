x=int(input("enter n"))
y=0
a=int()
while x>0:
    rem=x%10
    y+=rem
    x=x//10
print(y)
