import math

credit_principal = 'Credit principal: 1000'
final_output = 'The credit has been repaid!'
first_month = 'Month 1: paid out 250'
second_month = 'Month 2: paid out 250'
third_month = 'Month 3: paid out 500'

# write your code here
user_credit = int(input('Enter the credit principal:'))
user_wish = input("""
What do you want to calculate?
type "m" for count of months,
type "p" for monthly payment
""")
if user_wish == "m":
    user_payment = int(input('Enter monthly payment:'))
    users_months = math.ceil(user_credit / user_payment)
    if users_months == 1:
        print(f"It takes {users_months} month to repay the credit")
    else:
        print(f"It takes {users_months} months to repay the credit")

elif user_wish == "p":
    users_months = int(input("Enter count of months:"))
    payment = math.ceil(user_credit/users_months)
    lastpayment = user_credit - (users_months - 1) * payment
    if lastpayment != payment:
        print(f'Your monthly payment = {payment} with last month payment = {lastpayment}.')
    else:
        print(f'Your monthly payment = {payment}.')
