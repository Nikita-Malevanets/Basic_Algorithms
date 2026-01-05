import turtle


def pythagoras_tree(t, order, size):
    if order == 0:
        return

    t.forward(size)

    t.left(30)
    pythagoras_tree(t, order - 1, size * 0.7)

    t.right(60)
    pythagoras_tree(t, order - 1, size * 0.7)

    t.left(30)
    t.backward(size)


def draw_pythagoras_tree(order, size=120):
    window = turtle.Screen()
    window.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(0, -250)
    t.setheading(90)
    t.pendown()

    pythagoras_tree(t, order, size)

    window.mainloop()


order = int(input("Введи рівень рекурсії (наприклад 5–10): "))
draw_pythagoras_tree(order)
