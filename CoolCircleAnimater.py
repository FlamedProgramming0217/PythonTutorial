
import turtle
window = turtle.Screen()
turtle.Screen().bgcolor('black')
t = turtle.Turtle()
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']

#Asks for the speed and denies the answer when the input is not a number
speed = input("How fast we going? 0 is fastest.\n")
while True:
    if speed.isdigit():
        speed = int(speed)
        break
    speed = input("Incorrect answer, how fast we going? 0 is fastest.\n")

#Asks for how long the program should run. The number is for the "for i in range".
time = input(
    "How long should the program run? 500 is recommended: about 18 seconds.\n")
while True:
    if time.isdigit():
        time = int(time)
        break
    speed = input(
        "Incorrect answer, how long should the program run? 500 is recommended; about 18 seconds.\n"
    )

#Asks for the size of the circle. The variable is put into how forward the turtle should go in each round of the "for i in range"
size = input(
    "How big should the animation circle be? 50 seems like a good number.\n")
while True:
    if size.isdigit():
        size = int(size)
        break
    size = input(
        "Incorrect answer, How big should the animation circle be? 50 seems like a good number.\n"
    )

#Assigns speed and draws the animation
t.speed(speed)
for i in range(time):
    t.color(colors[i % 6])
    t.forward(size)
    t.left(59)

window.exitonclick()