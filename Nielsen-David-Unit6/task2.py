# David Nielsen
# CS1400 - I01
# Assignment 6 task 2

done = False
lst1 = []
while not done:

    numberToAdd = input('Please enter a number: ')
    if numberToAdd == '':
        done = True
    else:
        lst1.append(float(numberToAdd))

lengthList = len(lst1)
print('The number of values is ' + str(len(lst1)))

print('The minimum value in the list is ' + str(min(lst1)))

maxVal = float(lst1[0])
for i in range(len(lst1)):
    if maxVal < float(lst1[i]):
        maxVal = float(lst1[i])
print("The maximum value in the list is " + str(maxVal))

sum = 0

for i in lst1:
    sum += float(i)
print('The sum of the values in the list is ' + str(sum))
print('The average of the values in the list is ' + str(sum/lengthList))



