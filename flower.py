import turtle
tur = turtle.Turtle()
for k in range(180):
    tur.speed(0)
    tur.color('#7B2869')
    tur.circle(190 - k, 90)
    tur.left(90)
    tur.color('#C85C8E')
    tur.circle(190 - k, 90)
    tur.left(18)