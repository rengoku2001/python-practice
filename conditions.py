day_of_week = input("Enter day of week : ").lower() #convert lowercase
print(day_of_week)

if day_of_week == "saturday" or day_of_week == "sunday" : #if condition is true
    print("i will learn python")
else:  #if condition is false
    print("i wont learn python")  

num1 = int(input("enter First number: ")) #string to integer Type casting 
num2 = int(input("enter Second number: "))   

choice = input("Enter the operation: (Options + , - , * , / , %) :")

if choice == "+" :
    sum_of_num = num1 + num2
    print("addition: ",sum_of_num)
elif choice == "-" :
    diff_of_num = num1 - num2
    print("subtraction: ",diff_of_num)
elif choice == "*" :
    product_of_num = num1 * num2
    print("multiplication: ",product_of_num)
elif choice == "/" :
    divide_of_num = num1 / num2
    print("division: ",divide_of_num)
else :
    print("invalid")