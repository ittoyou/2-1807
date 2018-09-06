#coding=utf-8
import sys
import pygame
pygame.init()
size = width,height = 640,480#设置窗口
screen = pygame.display.set_mode(size)#显示窗口
color = (0,0,0)
ball = pygame.image.load('./图片/ball.jpg')
ballrect = ball.get_rect()#获取矩形区域
speed = [5,5]#设置移动的X轴,Y轴距离
clock = pygame.time.Clock()
while True:
	clock.tick(60)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
	ballrect = ballrect.move(speed)
	if ballrect.left < 0 or ballrect.right > width:
		speed[0] = - speed[0]
	if ballrect.top < 0 or ballrect.bottom > height:
		speed[1] = -speed[1]
	screen.fill(color)#填充颜色
	screen.blit(ball,ballrect)#将图片画到窗口上
	pygame.display.flip()#更新全部显示
pygame.quit()
