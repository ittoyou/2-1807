'''
import pygame
import sys
from pygame.locals import *


# pygame 初始化
pygame.init()


# 设置背景颜色和线条颜色
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)


# 设置鼠标拖动标志位
POS_moving = False


# 设置背景框大小
size = width, height = 600, 600
position = width // 2, height // 2


# 设置帧率，返回clock 类
clock = pygame.time.Clock()


screen = pygame.display.set_mode(size)
pygame.display.set_caption("llls make")


while True:
for event in pygame.event.get():
# 查找关闭窗口事件
if event.type == QUIT:
sys.exit()


# 查找鼠标按下事件
elif event.type == MOUSEBUTTONDOWN:
if event.button == 1:
# 值标志位为正
POS_moving = True


# 查找鼠标松开事件
elif event.type == MOUSEBUTTONUP:
if event.button == 1:
# 置标志位为假
POS_moving = False

# 填充背景色
screen.fill(WHITE)


# 画三个同心圆
pygame.draw.circle(screen, GREEN, position, 25, 1)
pygame.draw.circle(screen, BLUE, position, 75, 1)
pygame.draw.circle(screen, RED, position, 125, 1)

# 拖拽圆
if POS_moving:
position = pygame.mouse.get_pos()


# 刷新图
pygame.display.flip()


clock.tick(60)
'''
'''
#coding=utf-8
import pygame
from pygame.locals import *
from sys import exit
#thcolors 用于加载颜色进来
from pygame.color import THECOLORS
import time
pygame.init()
screen = pygame.display.set_mode((700, 480), 0, 32)
pygame.display.set_caption((r'python 画图工具').encode('utf-8')) 
start=time.clock ()
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
    end=time.clock ()
    if  int(end-start)==60:
        break
    screen.fill((255,255,255))
    #画矩形
    pygame.draw.rect(screen,[255,0,0],[400,280,300,200],1)
    pygame.draw.rect(screen,[255,0,0],[0,0,300,200],1)
    pygame.draw.rect(screen,[255,0,0],[0,280,300,200],1)
    pygame.draw.rect(screen,[255,0,0],[300,200,100,80],1)
    pygame.draw.rect(screen,[255,0,0],[400,0,300,200],1)
    #画多边形
    pygame.draw.polygon(screen,THECOLORS["red1"],[(100,100),(100,200),(300,100),(300,200)],1)
    #画圆
    pygame.draw.circle(screen,THECOLORS["red1"],[350,240],50,45)
    #画椭圆
    pygame.draw.ellipse(screen, THECOLORS["red1"], [250,200,200,80],0)
    #画弧线 
    pygame.draw.arc(screen, (0,255,0), (200, 200, 200, 100), 3.14159/3, 3.14159*2/3)
    x, y = pygame.mouse.get_pos()
    #画直线
    pygame.draw.line(screen, (0, 0, 255), (0, 0), (x, y))
    #画多条直线
    pygame.draw.lines(screen, (0,0,255), False,[(300,200),(300,500)],0) 
    #以下为根据鼠标画椭圆,矩形,圆
    pygame.draw.ellipse(screen, THECOLORS["blue"], [0,0,x,y],0)
    pygame.draw.rect(screen,[255,0,0],[100,100,x,y],0)
    pygame.draw.circle(screen,THECOLORS["red1"],[100,100],x,y)

   
    pygame.display.update()
'''
from turtle import *
import time
 
setup(600,800,0,0)
speed(0)
penup()
seth(90)
fd(340)
seth(0)
pendown()
 
speed(5)
begin_fill()
fillcolor('red')
circle(50,30)
 
for i in range(10):
    fd(1)
    left(10)
 
circle(40,40)
 
for i in range(6):
    fd(1)
    left(3)
 
circle(80,40)
 
for i in range(20):
    fd(0.5)
    left(5)
 
circle(80,45)
 
for i in range(10):
    fd(2)
    left(1)
     
circle(80,25)
 
for i in range(20):
    fd(1)
    left(4)
 
circle(50,50)
 
time.sleep(0.1)
 
circle(120,55)
 
speed(0)
 
seth(-90)
fd(70)
 
right(150)
fd(20)
 
left(140)
circle(140,90)
 
left(30)
circle(160,100)
 
left(130)
fd(25)
 
penup()
right(150)
circle(40,80)
pendown()
 
left(115)
fd(60)
 
penup()
left(180)
fd(60)
pendown()
 
end_fill()
 
right(120)
circle(-50,50)
circle(-20,90)
 
speed(1)
fd(75)
 
speed(0)
circle(90,110)
 
penup()
left(162)
fd(185)
left(170)
pendown()
circle(200,10)
circle(100,40)
circle(-52,115)
left(20)
circle(100,20)
circle(300,20)
speed(1)
fd(250)
 
penup()
speed(0)
left(180)
fd(250)
circle(-300,7)
right(80)
circle(200,5)
pendown()
 
left(60)
begin_fill()
fillcolor('green')
circle(-80,100)
right(90)
fd(10)
left(20)
circle(-63,127)
end_fill()
 
penup()
left(50)
fd(20)
left(180)
 
pendown()
circle(200,25)
 
penup()
right(150)
 
fd(180)
 
right(40)
pendown()
begin_fill()
fillcolor('green')
circle(-100,80)
right(150)
fd(10)
left(60)
circle(-80,98)
end_fill()
 
penup()
left(60)
fd(13)
left(180)
 
pendown()
speed(1)
circle(-200,23)
 
 
 
exitonclick()
