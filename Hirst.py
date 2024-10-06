# import colorgram
# colors = colorgram.extract('hirst.jpeg', 30)
# colors_list=[]
# for color in colors:
#   colors_list.append(tuple(color.rgb))
# print(colors_list)
import random
from turtle import Turtle, Screen, colormode

colors_list = [(29, 107, 154), (127, 172, 197), (151, 81, 51), (243, 213, 90),
               (203, 139, 156), (152, 61, 85), (13, 33, 64), (151, 20, 45),
               (212, 76, 104), (201, 158, 24), (62, 19, 34), (140, 176, 157),
               (218, 88, 61), (54, 23, 17), (236, 164, 184), (11, 45, 31),
               (59, 117, 84), (132, 32, 25), (24, 169, 203), (236, 170, 158),
               (28, 60, 113), (15, 92, 67), (134, 216, 232), (75, 156, 133),
               (7, 88, 107)]

tim = Turtle()
tim.speed("fastest")
colormode(255)
start_x = -250
start_y = 250


def tim_coloring():
  tim.begin_fill()
  tim.circle(20)
  tim.end_fill()


for i in range(100):
  tim.color(random.choice(colors_list))
  tim.penup()
  tim.goto(start_x + (i % 10) * 50, start_y - (i // 10) * 50)
  tim.pendown()
  tim_coloring()

screen = Screen()
screen.exitonclick()
