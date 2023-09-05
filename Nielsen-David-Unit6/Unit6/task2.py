lst = []
done = False

while not done:
    val = input("Enter a number: ")
    if val == "":
        done = True
    else:
        lst.append(val)

print("length of list: ", len(lst))



myMax = lst[0]
for i in range(len(lst)):
    if lst[i] > myMax:
        myMax = lst[i]

print("The maximum number is: ", myMax)

print("The minimum number is: ", min(lst))

sum = 0
for i in range(len(lst)):
    sum += int(lst[i])

print("The sum of all values is: ", sum)

print("The average of all values is: ", sum/(len(lst)))