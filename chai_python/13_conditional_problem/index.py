# 1.
# user_age=int(input("Please enter the age: "))
# if user_age<13:
#     print("Child")
# elif user_age<20:
#     print("Teenager")
# elif user_age<60:
#     print('Adult')
# else:
#     print('Senior')


# 2.
# age=int(input("Please enter the age: "))
# day="Wednesday"
# price = 12 if age >=18 else 8
# if day=="Wednesday":
#     price-=2
# print("Ticket price for you is $",price)


# 3. 
# score=int(input("Please enter the scrore: "))
# if score>100:
#     print("Please verify the grade again")
#     exit()
# if score>=90:
#     print("A")
# elif score>=80:
#     print("B")
# elif score>=70:
#     print("C")
# elif score>=60:
#     print("D")
# else :
#     print("F")


# 4.
# weather="Sunny"
# if weather=="Sunny":
#     activity="Go for a walk"
# elif weather=="Rainy":
#     activity="read"

# 5.
password=input("Please enter the password: ")
pass_len=len(password)
if len(password)<6:
    print("Weak")
