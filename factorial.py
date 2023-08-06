# factorial of any number through recursion using python
#Let's Started
def facto(k):
    if k<0 or k==0:
        return 1
    else:
        return(k * facto(k-1))
i=int(input("enter the number: "))
print("factorial of ",i,"is=",facto(i))
