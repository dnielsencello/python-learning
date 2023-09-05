# David Nielsen
# CS1400 - I01
# Unit 5 task 1

import turtle


class Face:
#initiate face
    def __init__(self):
        self.__smile = True
        self.__happy = True
        self.__darkEyes = True

#calls private methods to draw the face
    def draw_face(self):
        turtle.clear()
        self.__drawHead()
        self.__drawEyes()
        self.__drawMouth()

#draw the head
    def __drawHead(self):
        turtle.penup()
        turtle.goto(0, -50)
        turtle.pendown()
        turtle.fillcolor("yellow") if self.__happy else turtle.fillcolor("red")
        turtle.begin_fill()
        turtle.circle(100)
        turtle.end_fill()

#draw the eyes
    def __drawEyes(self):
        turtle.penup()
        turtle.fillcolor('black') if self.__darkEyes else turtle.fillcolor('blue')
        turtle.goto(-40, 50)
        turtle.pendown()
        turtle.begin_fill()
        turtle.circle(10)
        turtle.penup()
        turtle.goto(40, 50)
        turtle.pendown()
        turtle.circle(10)
        turtle.end_fill()

#draw the mouth
    def __drawMouth(self):
        turtle.pensize(5)
        turtle.penup()
        turtle.goto(-53, 0)
        turtle.setheading(-45) if self.__smile else turtle.setheading(225)
        turtle.pendown()
        turtle.circle(75, 90) if self.__smile else turtle.circle(75, -90)
        turtle.hideturtle()
        turtle.setheading(0)
        turtle.pensize(1)

# gets the value true or false
    def isSmile(self):
        return self.__smile

    def isHappy(self):
        return self.__happy

    def isDarkEyes(self):
        return self.__darkEyes

# changes the values true or false calls draw face
    def changeMouth(self):
        self.__smile = False if self.__smile else True
        self.draw_face()

    def changeEmotion(self):
        self.__happy = False if self.__happy else True
        self.draw_face()

    def changeEyes(self):
        self.__darkEyes = False if self.__darkEyes else True
        self.draw_face()


def main():
    face = Face()
    face.draw_face()

    done = False

    while not done:
        print("Change My Face")
        mouth = "frown" if face.isSmile() else "smile"
        emotion = "angry" if face.isHappy() else "happy"
        eyes = "blue" if face.isDarkEyes() else "black"
        print("1) Make me", mouth)
        print("2) Make me", emotion)
        print("3) Make my eyes", eyes)
        print("0) Quit")

        menu = eval(input("Enter a selection: "))

        if menu == 1:
            face.changeMouth()
        elif menu == 2:
            face.changeEmotion()
        elif menu == 3:
            face.changeEyes()
        else:
            break

    print("Thanks for Playing")

    turtle.hideturtle()
    turtle.done()


main()
