import turtle

window = turtle.Screen()

background = ("What should the background color be?")
turtle.Screen().bgcolor(background)

t = turtle.Turtle()
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']

speed = input("How fast do you want the spiral to draw? 0 is fastest.\n")
while True:
    if speed.isdigit():
        speed = int(speed)
        break
    speed = input("Incorrect answer, how fast do you want the spiral to draw? 0 is fastest.\n")
t.speed(speed)

time = input("How long should the program run? 500 is recommended, covers most of the canvas.\n")
while True:
    if time.isdigit():
        time = int(time)
        break
    speed = input("Incorrect answer, how long should the spiral draw? 500 is recommended, covers most of the canvas\n")

curve = input("How much curve should the program have? 58 - 60, with 60 having no curve at all and 58 having most curve.")

for i in range(time):
    t.color(colors[i % 6])
    t.forward(i)
    t.left(curve)

window.exitonclick()