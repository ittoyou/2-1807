#coding=utf-8
import pygame
from mysprite import *
class PlaneGame(object):
	def __init__(self):
		pygame.init()
		pygame.font.init()
		self.screen = pygame.display.set_mode(SCREEN_RECT.size)
		self.clock = pygame.time.Clock()
		self.__create_sprites()
		pygame.time.set_timer(CREATE_ENEMY_EVENT,800)#pygame 定时每隔一秒执行一次
		pygame.time.set_timer(CREATE_BULLET_EVENT,300)#pygame 定时每隔一秒执行一次
		self.enemy1_down_group = pygame.sprite.Group()#敌机销毁精灵组
		self.count = 0
		self.score = 0#分数
	def start_game(self):
		"""开始游戏"""
		print("开始游戏...")
		while True:
			self.count+=1
			self.clock.tick(60)#设置新帧率
			self.__event_handler()#事件监听
			self.__check_collide()#碰撞检测
			self.__update_sprites()#更新精灵组
			pygame.display.update()#更新屏幕显示
	def __create_sprites(self):
		bg1 = BackGroundSprite()
		bg2 = BackGroundSprite(True)
		self.back_group = pygame.sprite.Group(bg1,bg2)#创建背景组
		self.enemy_group = pygame.sprite.Group()#创建敌机精灵组
		self.herosprite = HeroSprite()
		self.hero_group = pygame.sprite.Group(self.herosprite)#创建英雄精灵组
	def __event_handler(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				PlaneGame.__game_over()
			elif event.type == CREATE_ENEMY_EVENT:
				enemy = EnemySprite()
				self.enemy_group.add(enemy)
			elif event.type == CREATE_BULLET_EVENT:
				self.herosprite.fire()
			#获取用户按键
			keys_pressed = pygame.key.get_pressed()
			if keys_pressed[pygame.K_RIGHT]:
				self.herosprite.speed = 10
				self.herosprite.speed1 = 0 
			elif keys_pressed[pygame.K_LEFT]:
				self.herosprite.speed = -10
				self.herosprite.speed1 = 0
			elif keys_pressed[pygame.K_UP]:
				self.herosprite.speed1 = -10
				self.herosprite.speed = 0
			elif keys_pressed[pygame.K_DOWN]:
				self.herosprite.speed1 = 10
				self.herosprite.speed = 0
			else:
				self.herosprite.speed1 = 0
				self.herosprite.speed = 0		
	def __check_collide(self):
		'''碰撞检测'''
		#检测两个精灵组中的精灵是否碰撞在一起 子弹和敌机
		enemy_down = pygame.sprite.groupcollide(self.enemy_group,self.herosprite.bullet_group,True,True)
		enemy1_down_group.add(enemy_down)#加入到销毁组
		#检测一个精灵和一个精灵组 敌机和英雄
		enemies = pygame.sprite.spritecollide(self.herosprite, self.enemy_group,True)
		if len(enemies) > 0:
			self.herosprite.kill()
			plan_main.__game_over()
	def __update_sprites(self):
		self.back_group.update()
		self.back_group.draw(self.screen)
		self.enemy_group.update()
		self.enemy_group.draw(self.screen)
		self.hero_group.update()         
		self.hero_group.draw(self.screen)
		self.herosprite.bullet_group.update()
		self.herosprite.bullet_group.draw(self.screen)
		#绘制分数
		self.drawText(str(self.score),SCREEN_RECT.width - 30,50)
		#敌机销毁
		for enemy1_down in enemy1_down_group:
			self.screen.blit(enemy1_down_surface[enemy1_down.down_index],enemy1_down.rect)
			if self.count % 15 == 0:
				enemy1_down.down_index += 1
				if enemy1_down.down_index == 3:
					self.score +=5
					enemy1_down_group.remove(enemy1_down)
					print(self.score)
	@staticmethod
	def __game_over():
		'''游戏结束'''
		print('游戏结束')
		pygame.quit()
		exit()
	def drawText(self,text,posx,posy,textHeight=48,fontColor=(0,0,0),backgroudColor=(255,255,255)):
		fontObj = pygame.font.Font(None, textHeight)#通过字体文件获得字体对象
		textSurfaceObj = fontObj.render(text, True,fontColor,backgroudColor)# 配置要显示的文字
		textRectObj = textSurfaceObj.get_rect()#获得要显示的对象的rect
		textRectObj.center = (posx, posy)  # 设置显示对象的坐标
		self.screen.blit(textSurfaceObj, textRectObj)  # 绘制字
if __name__ == '__main__':
	#创建游戏对象
	game = PlaneGame()
	#开始游戏
	game.start_game()
