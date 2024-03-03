# Factorial

num = int(input("enter a number"))
if num < 0:
    print("fact not exist")
elif num == 0:
    print("fact is 1")
else:
    fact = 1
    for i in range (1,num+1):
        fact = fact*i
        print("fact of " ,fact)