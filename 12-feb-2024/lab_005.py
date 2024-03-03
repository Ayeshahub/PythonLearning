#Continue

for num in range (0,11):
    if num % 2==0:
        print(f"found even number{num}")
        continue
    print(f"odd number{num}")


    for i in range (0,10):
        if i%3==0:
            print(i)
        else:
            print(i*2)
