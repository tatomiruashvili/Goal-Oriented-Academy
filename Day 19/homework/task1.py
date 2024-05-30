#Write a program that takes asks user for number (use input). If number is even, print that number is even. Else print that number is not even,
# also print next even number, for example if input is 15, print 16.
num1 = int(input("Please enter an int: "))

if num1 % 2 == 0:
    print("Number is even!")

else:
    print("Number is odd!")
    print("Next closest even number is" + " "  + str(num1 + 1))



#Create a while loop that asks the user to enter a password. Keep asking until they enter the correct password "Goa best". 
#Also print the count of incorrect passwords.
correct_password = "Best Goa"
incorrect_tries = 0

while True:
        num1 = input("Please enter your password: ")
        if num1 == correct_password:
            print("Access granted!")
            break
        else:
            incorrect_tries += 1
            print("Password is incorrect! Please try again: ")
            print("You have " + str(incorrect_tries) + " tries")
