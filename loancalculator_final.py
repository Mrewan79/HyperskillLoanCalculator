import argparse
import math
import sys

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("--payment")
    parser.add_argument("--principal")
    parser.add_argument("--periods")
    parser.add_argument("--interest")
    parser.add_argument("--type")
    
    args = parser.parse_args()

    arguments = [args.payment, args.principal, args.periods, args.interest, args.type]

    #fails if there is no interest argument
    if arguments[3] is not None: 
        i = float(arguments[3]) * 0.01 / 12
    else:
        print("Incorrect parameters.")
        sys.exit()

    if i < 0:
        print("Incorrect parameters. ")
        sys.exit()

    if arguments[0] is None:
        if arguments[4] == "annuity":
            p = float(arguments[1])
            n = int(arguments[2])
            calc_payment(p, n, i)
        elif arguments[4] == "diff" and arguments[3] is not None:
            p = float(arguments[1])
            if p < 0:
                print("Incorrect parameters.")
            else:
                n = int(arguments[2])
                if n < 0:
                    print("Incorrect parameters.")
                else:
                    calc_diff_payments(p, n, i)
        else:
            print("Incorrect parameters.")
    elif arguments[1] is None:
        a = float(arguments[0])
        n = float(arguments[2])
        calc_principal(a, n, i)
    elif arguments[2] is None:
        a = float(arguments[0])
        if a < 0:
            print("Incorrect parameters.")
        else:
            p = float(arguments[1])
            calc_periods(a, p, i)
    elif arguments[4] is None:
        print("Incorrect parameters.")

def calc_payment(p, n, i):
    payment = p * ((i * (1 + i) ** n) / ((1 + i) ** n - 1))
    print(f"Your monthly payment =  {math.ceil(payment)}!")

def calc_principal(a, n, i):
    principal = a / ((i * (1 + i) ** n) / ((1 + i) ** n - 1))
    print(f"Your loan principal = {round(principal)}!")

def calc_periods(a, p, i):
    periods = math.ceil(math.log((a / (a - i * p)), 1 + i))
    years = periods // 12
    months = periods % 12
    if years == 0:
        years_and_months = f"{months} months"
    elif months == 0:
        years_and_months = f"{years} years"
    else:
        years_and_months = f"{years} years and {months} months"
    print("It will take", years_and_months, "to repay this loan!")
    
    #Overpayment
    payment = a * periods
    overpayment = payment - p
    print(f"Overpayment: {overpayment:.2f}")

def calc_diff_payments(p, n, i):
    total_payment = 0
    for m in range(1, n + 1):
       dm = (p / n) + i * (p - (p * ( m - 1 )) / n)
       print(f'Month {m} : payment is {math.ceil(dm)}')
       total_payment += math.ceil(dm)
       
    overpayment = total_payment - p
    print(f'Overpayment = {overpayment}')

main()
