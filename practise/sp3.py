def fizzbuzz():
    number = int(input("enter a number:"))
    for i in range (1, 100):
        if i%3==0 and i%5==0:
            print("fizzbuzz")
        elif i%3==0:
            print("fizz")
        elif i%5==0:
            print("buzz")
        else:
            print(i)
fizzbuzz()


string=input("ente a name:")
reverse=string[::-1]
if string==reverse:
    print("is palindrome")
else:
    print("not a palindrome")