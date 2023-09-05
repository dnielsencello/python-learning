def makenumberpyramid(num):
    out = str()
    for i in range(1, num + 1):
        if len(str(i)) < 2 and num >= 10:
            out += "     "
        for s in range(0, num - i):
            out += " "
        for j in range(i):
            if j < i - 1:
                out += str(i)
                out += str(" ")
            else:
                out += str(i)
        out += "\n"
    return out


num = eval(input("Enter the number of rows: "))
output = makenumberpyramid(num)
print(output)
