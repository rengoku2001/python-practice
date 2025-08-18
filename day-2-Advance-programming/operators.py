#operators -
#Arithematic operators: + - * / // ** %
value1 = 58
value2 = 23
print(value1+value2)
print(value1-value2)
print(value1*value2)
print(value1/value2)
print(value1//value2) #integer division , it leaves decimal points 
print(value1**value2) #it is like power, value1's power is value2 , value2 is the power of value1
print(value1%value2) # "%" this sign is modular not percentage, it gives reminder of the division

#comparison operators: ==, != , > , < , >= , <=
#input can be any data type but output is always boolean
value1 = 60
value2 = 37
print("value1==value2 :" ,value1==value2) #value1 is equal to value2 : result is either true or false 
print("value1!=value2 :" ,value1!=value2) # "!=" means not equal to
print("value1>value2 :" ,value1>value2)
print("value1<value2 :" ,value1<value2)
print("value1>=value2 :" ,value1>=value2)
print("value1<=value2 :" ,value1<=value2)

#Logical operators : and , or , not
#Prediction : Rohit and virat will open the batting 
# Actual : Rohit and Shubhman gill opened the batting 
# Predition is wrong : "and" operator then all the values have to be True for the output to be True else its False
#In logical operators both the input have to be Boolean and the outcome is also a bool value  
print(True and True) #true and true means true , rest all are false
print(True and False)
print(False and True)
print(False and False)
a=5
b=6
c=5
print("my answer is :",a>=b and b>=c and c==a and c<b)
# F , T , T , T -->> even one false can make it complete false