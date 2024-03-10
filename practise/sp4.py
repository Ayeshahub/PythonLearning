def print_right_triangle(rows):
    for i in range(1, rows + 1):
        print("*" * i)


# Input the number of rows for the triangle
rows = int(input("Enter the number of rows for the triangle: "))

# Call the function to print the right triangle
print_right_triangle(rows)



def print_left_triangle(rows):
    for i in range(1, rows + 1):
        print(" " * (rows - i) + "*" * i)

# Input the number of rows for the triangle
rows = int(input("Enter the number of rows for the triangle: "))

# Call the function to print the left triangle
print_left_triangle(rows)
