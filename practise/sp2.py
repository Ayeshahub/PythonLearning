def print_multiplication_table():
    table=int(input("enter a table: "))
    for i in range (1, 10):
        result=table*i
        print(f"{table}*{i} = {result}")
print_multiplication_table()



def fizzbuzz():
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
