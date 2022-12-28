import turtle
window = turtle.Screen()
turtle.Screen().bgcolor('black')
t = turtle.Turtle()
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
speed = input("How fast do you want the spiral to draw? 0 is fastest.\n")
while True:
    if speed.isdigit():
        speed = int(speed)
        break
    speed = input("Incorrect answer, how fast do you want the spiral to draw? 0 is fastest.\n")
time = input(
    "How long should the program run? 500 is recommended, covers most of the canvas.\n")
while True:
    if time.isdigit():
        time = int(time)
        break
    speed = input(
        "Incorrect answer, how long should the spiral draw? 500 is recommended, covers most of the canvas\n"
    )
t.speed(speed)
for i in range(time):
    t.color(colors[i % 6])
    t.forward(i)
    t.left(58)

window.exitonclick()