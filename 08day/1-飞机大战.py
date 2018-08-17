#coding=utf-8
import pygame
from mysprite import *
pygame.init()

# 创建游戏主窗口
screen = pygame.display.set_mode((480,700))
# 1> 加载图像
bg = pygame.image.load("./images/background3.png")
hero = pygame.image.load('./images/hero1.png')

herorect = pygame.Rect(200,500,120,120)#创建一个

clock = pygame.time.Clock()#创建游戏时钟
enemy = EnemySprite()
enemy1 = EnemySprite()
enemy1.rect.x = 50
enemy1.speed = 2
enemy_group = pygame.sprite.Group(enemy,enemy1)

# 游戏循环
while True:

	# 设置屏幕刷新帧率
	clock.tick(60)

	# 事件监听
	for event in pygame.event.get():

		# 判断用户是否点击了关闭按钮
		if event.type == pygame.QUIT:
			print("退出游戏...")

			pygame.quit()

			# 直接退出系统
			exit()
	herorect.y-=1
	screen.blit(bg,(0,0))
	screen.blit(hero,herorect)
	if herorect.bottom <= 0:#控制飞机返航
		herorect.top = 700
	enemy_group.update()
	enemy_group.draw(screen)
	pygame.display.update()


