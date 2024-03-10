num1=int(input("enter first number: "))
num2=int(input("enter second number: "))
num3=num1+num2
print("sum of two numbers is: ",num3)


num=int(input("enter  number: "))
if (num%2 )==0:
    print("even number")
else:
    print("odd number")


    def print_right_triangle(rows):
        for i in range(1, rows + 1):
            print("*" * i)


    # Input the number of rows for the triangle
    rows = int(input("Enter the number of rows for the triangle: "))

    # Call the function to print the right triangle
    print_right_triangle(rows)

