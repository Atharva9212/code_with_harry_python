#create a calculator
print("you are using a calculator ")

#Input
print("Enter the operation to be performed ")
print("Select 1 for Addition \nSelect 2 for Subtraction \nSelect 3 for Multiply \nSelect 4 for Division ")
choice = int(input("\nEnter your choice : "))

if choice == 1:
    print("the sum: ",int(input("Enter the first number : "))+int(input("Enter the second number : ")))
elif choice == 2:
    print("the subtraction is: ", int(input("Enter the first number : ")) - int(input("Enter the second number : ")))
elif choice == 3:
    print("the multiplication is : ", int(input("Enter the first number : ")) * int(input("Enter the second number : ")))
elif choice == 4:
    print("the division: ", int(input("Enter the first number : ")) / int(input("Enter the second number : ")))


print("Thank you for using our service ")
