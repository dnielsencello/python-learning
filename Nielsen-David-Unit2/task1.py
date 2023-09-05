# David Nielsen
# CS1400 - I01
# Assignment 2 task 1

# Calculate the future value of an investment

# User indicates investment amount, no. of years
investmentAmount = eval(input('Enter the starting investment amount: $'))
# User indicates the monthly payment amount
paymentAmount = eval(input('Enter the monthly payment amount: $'))
# User indicates the monthly interest rate
monthlyInterestRate = eval(input('Enter the annual interest: '))/(100*12)
# User indicates the number of years
years = eval(input('Enter the number or years: '))
# Monthly calculation
numOfMonths = years*12
# Calculation of the future value of the investment
futureValue = round(investmentAmount*((1+monthlyInterestRate)**numOfMonths) + (paymentAmount*(((1+monthlyInterestRate)**numOfMonths)-1)/(monthlyInterestRate))*(1+monthlyInterestRate),2)

# Print Statement
print('Future value is: $' + str(futureValue))
