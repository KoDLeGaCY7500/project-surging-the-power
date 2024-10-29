def power8(number):
    if number <=0:
        return False
    return(number&(number-1))==0

n=int(input("Enter number: "))

if power8(n):
    print("no is the power of 8")
else:
    print("no is not the power of 8(error code-69420)")