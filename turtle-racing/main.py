import turtle
import time
import random

WIDTH, HEIGHT = 500, 500

colors = ['red', 'green', 'blue', 'orange', 'yellow', 'black', 'purple', 'pink', 'brown', 'cyan']


def get_number_of_racer():
    racers = 0
    while True:
        racers = input('Enter the number of turtle to race...(2 -10): ')
        if racers.isdigit():
            racers = int(racers)
        else:
            print('Input is not a numeric...Try again')
            continue
        if racers >= 2 and racers <= 10:
            return racers
        else:
            print('The number you have enter is out of range...')

def init_turtle():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title('Turtle Racing')

def create_turtle(colors):
    turtles = []
    spacing = WIDTH // (len(colors)+1)
    for i, color in enumerate(colors):
        t = turtle.Turtle()
        t.speed(1)
        t.color(color)
        t.shape('turtle')
        t.left(90)
        t.penup()
        t.setpos(-WIDTH // 2 + (i + 1) * spacing,  -HEIGHT//2 + 20)
        t.pendown()
        turtles.append(t)

    return turtles

def race(colors):
    turtles = create_turtle(colors)
    while True:
        for i in turtles:
            t = turtles[random.randrange(0, len(turtles))]
            distance = random.randrange(1, 20)
            t.forward(distance)
            x, y = t.pos()

            if y >= HEIGHT//2 - 10:
                return colors[turtles.index(t)]


num = get_number_of_racer()
init_turtle()
random.shuffle(colors)
color_li = colors[:num]
winner = race(color_li)
print(' The winner is the turtle with the color :', winner)
time.sleep(10)
