# David Nielsen
# CS1400 - I01
# Assigment 2 task 4



# User Inputs employment information: Name, Hours worked in a week, Hourly Pay, Federal and State Withholding
employeeName = input("Enter employee's name:")
hoursWorked = eval(input("Enter number of hours worked in a week:"))
hourlyPay = eval(input("Enter hourly pay rate:"))
fedWithhold = eval(input("Enter federal tax withholding rate (ex. 0.12):"))
stateWithhold = eval(input("Enter state tax withholding rate (ex. 0.06):"))



# Calculations for total pay, state and federal withholding, and net pay
totalPay = hoursWorked*hourlyPay
fedWithholding = totalPay*fedWithhold*100
stateWithholding = totalPay*stateWithhold*100
totalDeduction = stateWithholding+fedWithholding
netPay = totalPay - totalDeduction

# Concatenation of Calculations and Results

Out = employeeName.upper()
Out += " EMPLOYEE INFORMATION"
Out = format(Out, "^40")
Out += "\n"
Out += "\n"
Out += format("Pay", "^40")
Out += "\n"
Out += format("Hours Worked:  ", ">30")
Out += format(hoursWorked, ">10")
Out += "\n"
Out += format("Pay Rate: $", ">30")
Out += format(hourlyPay, ">10.2f")
Out += "\n"
Out += format("Gross Pay: $", ">30")
Out += format(totalPay, ">10.2f")
Out += "\n"
Out += "\n"
Out += format("Deductions", "^40")
Out += "\n"
Out += format("Federal Withholding " + str(fedWithhold) + "): $", ">30")
Out += format(fedWithholding, ">10.2f")
Out += "\n"
Out += format("State Withholding (" + str(fedWithhold) + "): $", ">30")
Out += format(stateWithholding, ">10.2f")
Out += "\n"
Out += format("Total Deduction: $", ">30")
Out += format(totalDeduction, ">10.2f")
Out += "\n"
Out += "\n"
Out += format("Net Pay $", ">30")
Out += format(netPay, ">10.2f")
print(Out)
