num1 = int(input("enter first number:"))
num2 = int(input("enter second number:"))
print("1.add")
print("2.substract")
print("3.multi")
choice =int(input("enter choice(1/2/3):"))
if choice == 1:
    print("result:",num1+num2)
elif choice ==2:
     print("result:",num1-num2)
elif choice ==3:
     print("result:",num1*num2)     
else:
     print("error")