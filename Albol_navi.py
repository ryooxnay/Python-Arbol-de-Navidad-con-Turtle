# -*- coding: utf-8 -*-
"""
Created on Sun Dec 25 01:17:03 2022

@author: USER
"""
import turtle
from random import randint
def crear_recta(turtle, color, x, y, width, height):
    turtle.penup()
    turtle.color(color)
    turtle.fillcolor(color)
    turtle.goto(x,y)
    turtle.pendown()
    turtle.begin_fill()
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    turtle.left(90)
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    turtle.left(90)
    turtle.end_fill()
    turtle.setheading(0)


t = turtle.Turtle()
#Para cambiar el color de fondo en turtle
canvas = turtle.Screen()
canvas.bgcolor("black")

y= -100
crear_recta(t, "brown", -15, y-60, 30, 60)
width = 240
t.speed(10)
while  width > 10:
    width = width -10
    height = 10
    x = 0 - width/2
    crear_recta(t, "green", x, y, width, height)
    y = y + height
t.speed(1)
t.penup()
t.color("yellow")
t.goto(-20, y+10)
t.begin_fill()
t.pendown()
for i in range(5):
    t.forward(40)
    t.right(144)
t.end_fill()
tree_heigth = y + 40
t.hideturtle()
