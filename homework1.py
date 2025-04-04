import turtle
def draw_bar(t, height):
    t.begin_fill()
    t.left(90)
    t.forward(height)
    if height >= 0:
        t.write(height, font=('Arial', 10, 'bold'))
    else:
        t.penup()
        t.forward(-18)
        t.pendown()
        t.write(height, font=('Arial', 10, 'bold'))
        t.penup()
        t.forward(18)
        t.pendown()
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(height)
    t.left(90)
    t.penup()
    t.forward(10)
    t.pendown()
    t.end_fill()

wn = turtle.Screen()

xs = [-48, 117, 200, -240, 160, 260, 220]
tess = turtle.Turtle()
tess.penup()
tess.goto(-170, 0)
tess.pendown()
for v in xs:
    if v >= 200:
        tess.color('black', 'red')
    elif 100 <= v < 200:
        tess.color('black', 'yellow')
    elif v < 100:
        tess.color('black', 'green')

    draw_bar(tess, v)

wn.mainloop()



