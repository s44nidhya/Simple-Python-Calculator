


for i in range(0, 1000000000000):
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))

    op = input("Enter an operation to perform: ")



    if op=="+":
        print("The sum is:",a+b)
    if op=="-":
        print("The difference is:", a-b)
    if op=="*" or op=="x":
        print("The product is:",a*b)
    if op=="/":
        print("The quotient is: ",a/b)

    fur = str(input("Do you want to go further(Y/N): "))
    if fur =="Y":
        continue
    if fur=="N":
        print("Thanks for using my calculator<3")
        break


