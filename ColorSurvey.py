import turtle
choices = ["red", "green", "blue", "black", "yellow", "orange", "purple", "pink", "brown"]
favorites = [ [choices[0]], [choices[1]], [choices[2]], [choices[3]], [choices[4]], [choices[5]], [choices[6]], [choices[7]], [choices[8]] ]

while True:
    name = input("What is your name?\n")
    fav_color = input("What is your favorite color?\n")

    if fav_color == choices[0]:
        favorites[0].append(name)
    elif fav_color == choices[1]:
        favorites[1].append(name)
    elif fav_color == choices[2]:
        favorites[2].append(name)
    elif fav_color == choices[3]:
        favorites[3].append(name)
    elif fav_color == choices[4]:
        favorites[4].append(name)
    elif fav_color == choices[5]:
        favorites[5].append(name)
    elif fav_color == choices[6]:
        favorites[6].append(name)
    elif fav_color == choices[7]:
        favorites[7].append(name)
    elif fav_color == choices[8]:
        favorites[8].append(name)
    else:
        break

t = turtle.Turtle()
t.speed(0)
t.penup()
t.goto(-200, 100)
t.pensize(10)

down = 50

for category in favorites:

  t.color(category[0])
  
  for index in range(len(category)):
    
    t.left(90)
    t.forward(10)
    t.write(category[index])

    t.forward(10)
    t.write(index)

    t.right(180)
    t.forward(20)

    t.left(90)
    t.pendown()
    t.forward(50)
    t.penup()

  t.goto(-200, 100 - down)
  down += 50