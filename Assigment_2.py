
#Enter Full Names
print("Enter First and Last Name:")
fname = input("Enter First Name: ")
lname = input("Enter Last Name: ")
fullnames = fname + " " + lname

#Enter phone, email
print("Enter Customer's Phone Number: ")
phone = input("Enter Phone Number: ")
print("Enter Customer's Email Address:")
email = input("Enter Email Address: ")

#price of a used car
price = 10000
has_good_credit = True

if has_good_credit:
    down_payment = 0.1 * price
else:
    down_payment = 0.2 * price

print("Full Names:" + fullnames)
print("Phone: " + phone)
print("Email: " + email)
print("Down Payment:", down_payment)