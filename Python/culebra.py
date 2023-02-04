import turtle

# Configuración de la ventana
wn = turtle.Screen()
wn.title("Triki")
wn.bgcolor("lightblue")
wn.setup(width=600, height=600)

# Dibujar la cuadrícula
pen = turtle.Turtle()
pen.speed(0)
pen.color("black")
pen.pensize(3)
pen.penup()
pen.goto(-200, 200)
pen.pendown()
for i in range(4):
    pen.forward(400)
    pen.left(90)
pen.penup()

# Creación de los marcadores X y O
x_marker = turtle.Turtle()
x_marker.speed(0)
x_marker.shape("turtle")
x_marker.color("red")
x_marker.shapesize(3,3)
x_marker.penup()
o_marker = turtle.Turtle()
o_marker.speed(0)
o_marker.shape("circle")
o_marker.color("blue")
o_marker.shapesize(3,3)
o_marker.penup()

# Creación de una lista de las posiciones de la cuadrícula
positions = [(-100, 100), (100, 100), (-100, -100), (100, -100), 
             (-100, 0), (100, 0), (0, 100), (0, -100), (0, 0)]

# Bucle principal del juego
turn = "X"
for i in range(9):
    if turn == "X":
        x_marker.goto(positions[i])
        x_marker.stamp()
        turn = "O"
    else:
        o_marker.goto(positions[i])
        o_marker.stamp()
        turn = "X"

# Mantener la ventana abierta
wn.mainloop()