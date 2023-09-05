# David Nielsen
# CS1400 - I01
# Unit 5 task 3 bobinator

class Bobinator:

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def getAge(self):
        return self.__age

    def getName(self):
        return self.__name

    def min(self, other):
        if int(self.__age) < int(other.getAge()):
            return self
        else:
            return other

#returns uppercase concatenation of names and adds ages
    def __add__(self, other):
        bob = ""
        if len(str(self.__name)) < len(str(other.getName())):
            bob += other.getName().upper() + self.__name.upper()
            newAge2 = int(other.getAge()) + self.__age

        else:
            bob += self.__name.upper() + other.getName().upper()
            newAge2 = int(other.getAge()) + self.__age
        return Bobinator(bob, newAge2)

# concatenates lowercase of names (starting with shorter) and substracts ages
    def __sub__(self, other):
        bob = ""
        if len(str(self.__name)) > len(str(other.getName())):
            bob += str(other.getName()).lower() + self.__name.lower()
            newAge2 = abs(int(other.getAge()) - self.__age)

        else:
            bob += self.__name.lower() + str(other.getName()).lower()
            newAge2 = abs(int(other.getAge()) - self.__age)
        return Bobinator(bob, newAge2)
# adds repeat of last letter a number of times (factor -1) and multiplies the ages
    def __mul__(self, factor):
        newName = self.__name
        newName += self.__name[-1]*(factor-1)
        newAge = self.__age*(factor)
        return Bobinator(newName, newAge)

# alternates letters of each name uppercase and lowercase, calculates average
    def __truediv__(self, other):

        bob = ''
        i = j = 0
        if len(self.__name) > len(other.getName()):
            s1 = self.__name
            s2 = other.getName()
        elif len(self.__name) < len(other.getName()):
            s2 = self.__name
            s1 = other.getName()
        else:
            s1 = self.__name
            s2 = other.getName()

        while i < len(s1) and j < len(s2):
            bob += s1[i].lower() + s2[j].lower()
            i += 1
            j += 1
        while i < len(s1):
            bob += s1[i]
            i += 1
        print(bob)
        bob2 = ''
        for i in range(len(bob)):
            if i % 2 == 0:
                bob2 += bob[i].upper()
            else:
                bob2 += bob[i]
        newAge = (self.__age + int(other.getAge()))/2
        return Bobinator(bob2, newAge)

# gets the middle of each name and concatenates them, calculates average age
    def __mod__(self, other):

        bob = ""
        bob += self.getMid() + other.getMid()
        bob2 = ""
        for i in range(len(bob)):
            if i == 0 or i == len(bob) - 1:
                bob2 += bob[i].upper()
            else:
                bob2 += bob[i].lower()
        newAge = (self.__age + int(other.getAge())) / 2

        return Bobinator(bob2, newAge)

# gets the middle of each name
    def getMid(self):
        edge = 1
        midBob = ""
        while len(self.__name) - 2 * edge >= edge + 1:
            edge += 1

        for i in range(edge - 1, len(self.__name) - edge + 1):
            midBob += self.__name[i]

        return midBob

# reverses name and age
    def backBobSlice(self):

        bob = self.__name[::-1]
        newAge = str(self.__age)[::-1]
        newAge = int(newAge)

        return Bobinator(bob, newAge)

# reverses name and age
    def backBobManual(self):
        bob = ''
        newAge = ""
        for i in range(len(self.__name)):
            bob += self.__name[-i-1]
        for i in range(len(str(self.__age))):
            newAge += str(self.__age)[-i-1]

        return Bobinator(bob, newAge)

    def __lt__(self, other):
        return self.__age < other.getAge()

    def __str__(self):
        return str(self.__name + '(' +str(self.__age) + ')')

    def __repr__(self):
        return self.__name
