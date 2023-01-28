import math 
from turtle import *
import turtle
def hearta(k):
       return 15*math.sin(k)**3
def heartb(k):
       return 12*math.cos(k)-5*\
              math.cos(2*k)-2*\
              math.cos(3*k)-\
              math.cos(4*k)
speed(0)
bgcolor("black")

for i in range(500):
       goto(hearta(i)*20, heartb(i)*20)
       backward(50)
       for j in range(5):
              if i <= 100:
                     color("#a7fff4")
              elif i<100 and i <= 200:
                     color("#FFD6EC")
              elif i<200 and i <= 300:
                     color("#FFA1CF")
              elif i<300 and i <= 400:
                     color("#FF74B1")
              elif i<400 and i <= 500:
                     color("#FF1E1E")
       goto(0,0)

goto(0,0)
pencolor("#FFFFFF")
write("ROBOGIRL TINKER", align="center", font = ("Display", 45, "italic"))
done()