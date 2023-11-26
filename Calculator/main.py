a=0
while a!=1:    
    num1=int(input("Enter the 1st number: "))
    # print("If you want to find out the percentage, Then left the section of number 2 blank.")
    num2=int(input("Enter the 2st number: "))
    opera=input("Enter the operator: ")


    if opera=="+":
        print(f"The sum of {num1} and {num2} is {num1+num2}.")
    if opera=="-":
        print(f"The difference of {num1} and {num2} is {num1-num2}.")
    if opera=="*":
        print(f"The product of {num1} and {num2} is {num1*num2}.")
    if opera=="/":
        print(f"The quotient of {num1} and {num2} is {num1/num2}.")