# David Nielsen
# CS1400 - I01
# Unit 4 Task 1
# make the number pyramid
def makeNumberPyramid(rows):
    #initiate string variables
    stringVariable = ""
    bottomString = ""

    # determine the length of the bottom row
    for i in range(rows):
        if i != 0:
            bottomString += " "
        bottomString += str(rows)
    lengthOfBottomRow = len(bottomString)
    #create individual rows
    for i in range(1, rows + 1):
        # initiate individual string rows
        rowString = ""
        for j in range(0, i):
            if j != 0:
                rowString += " "
            rowString += str(i)
        #add each rowString to the stringVariable
        stringVariable += format(rowString, "^" + str(lengthOfBottomRow))
        stringVariable += "\n"
    return stringVariable

def main():
    rows = eval(input("Enter the number of rows: "))
    print(makeNumberPyramid(rows))

main()