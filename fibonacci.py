#fibonacci series
i=int(input("Enter the number:"))
x=0
y=1
z=0

while(z<=i):
    print(z)
    x=y
    y=z
    z=x+y
