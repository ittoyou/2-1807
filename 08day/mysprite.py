#coding=utf-8
import random
import pygame
SCREEN_RECT = pygame.Rect(0,0,480,700)
CREATE_ENEMY_EVENT = pygame.USEREVENT#敌机的定时器事件常量
CREATE_BULLET_EVENT = pygame.USEREVENT + 1# 英雄发射子弹事件
#爆炸销毁图片
bg1 = pygame.image.load('./images/enemy1_down3.png')
bg2 = pygame.image.load('./images/enemy1_down3.png')
bg3 = pygame.image.load('./images/enemy1_down3.png')
bg4 = pygame.image.load('./images/enemy1_down4.png')
#爆炸的精灵组
enemy1_down_group = pygame.sprite.Group()
#把爆炸图片放到列表中
enemy1_down_surface = []
enemy1_down_surface.append(bg1)
enemy1_down_surface.append(bg2)
enemy1_down_surface.append(bg3)
enemy1_down_surface.append(bg4)
class GameSprite(pygame.sprite.Sprite):
	def __init__(self,image,speed=1):
		super(GameSprite,self).__init__()
		self.image = pygame.image.load(image)
		self.rect = self.image.get_rect()
		self.speed = speed
	def update(self):
		self.rect.y+=self.speed
class EnemySprite(GameSprite):
	def __init__(self):
		#imagename = './images/enemy-2.gif'
		#super(EnemySprite,self).__init__(self.planeImageName)
		randomImageNum = random.randint(1,3)
		self.planeImageName = './images/enemy' + str(randomImageNum) +'.png'
		super(EnemySprite,self).__init__(self.planeImageName)

		#self.image = pygame.image.load(self.planeImageName).covert()
		self.speed = random.randint(1,20)
		max = SCREEN_RECT.width - self.rect.width
		self.rect.x = random.randint(0,max)
		self.rect.bottom = 0
		self.down_index = 0#敌机销毁图片索引
		# 添加爆炸效果
		self.bomb_image_list = []
		self.__get_bomb_image() # 加载爆炸图片
	def update(self):
		super(EnemySprite,self).update()
		if self.rect.top >= SCREEN_RECT.height:
			self.kill()
	# 加载爆炸图片
	def __get_bomb_image(self):
		for i in range(1,4):
			randomImageNum = random.randint(1,3)
			imagename = './images/enemy'+str(randomImageNum) + '.png'
			self.bomb_image_list.append(pygame.image.load(imagename))
class BackGroundSprite(GameSprite):
	def __init__(self,is_alt=False):
		self.imagename = './images/background3.png'
		super(BackGroundSprite,self).__init__(self.imagename,3)
		if is_alt:
			self.rect.y = -self.rect.height
	def update(self):
		super(BackGroundSprite,self).update()
		if self.rect.top >= SCREEN_RECT.height:
			self.rect.y = -self.rect.height
class HeroSprite(GameSprite):
	def __init__(self):
		self.imagename = './images/hero1.png'
		super(HeroSprite,self).__init__(self.imagename)
		self.speed = 0
		self.bullet_group = pygame.sprite.Group()#创建子弹精灵组
		# 设置初始位置
		self.rect.centerx = SCREEN_RECT.centerx
		self.rect.bottom = SCREEN_RECT.bottom - 120
	def update(self):
		#super(HeroSprite,self).update()
		self.rect.x += self.speed# 飞机水平移动
		self.rect.y += self.speed1
		# 判断屏幕边界
		if self.rect.left <= 0:
			self.rect.left = 0
		if self.rect.right >= SCREEN_RECT.right:
			self.rect.right = SCREEN_RECT.right
		if self.rect.top < 0:
			self.rect.top = 0
		if self.rect.bottom > SCREEN_RECT.height:
			self.rect.bottom = SCREEN_RECT.height
	def fire(self):	
		bullet = BulletSprite()
		bullet.rect.x = self.rect.centerx
		bullet.rect.bottom = self.rect.top 
		bullet1 = BulletSprite()
		bullet1.rect.x = self.rect.centerx-35
		bullet1.rect.bottom = self.rect.top+30 
		bullet2 = BulletSprite()
		bullet2.rect.x = self.rect.centerx+35
		bullet2.rect.bottom = self.rect.top+30 
		self.bullet_group.add(bullet1)
		self.bullet_group.add(bullet2)
		self.bullet_group.add(bullet)
#英雄的子弹类
class BulletSprite(GameSprite):
	def __init__(self):
		self.imagename = './images/bullet.png'
		super(BulletSprite,self).__init__(self.imagename,-10)
	def update(self):
		super(BulletSprite,self).update()
		# 判断是否超出屏幕，如果是，从精灵组删除
		if self.rect.bottom < 0:
			self.kill()
#敌机的子弹类
class EnemyBullet(GameSprite):
	def __init__(self):
		self.imagename = './images/bullet1.png'
		super(EnemyBullet,self).__init__(screen,self.imagename,x+20,y+30)
	def judge_jizhong(self,hero):
		if self.x > hero.x and self.x < hero.x + 50:
			if self.y > hero.y and self.y < hero.y + 20:
				print('英雄死亡')
				return True
		else:
			return False

	def move(self):
		self.y += 5

	def judge(self):
		if self.y > 700:
			return True
		else:
			return False

class Source(pygame.sprite.Sprite):
	def __init__(self):
		super(Source,self).__init__()
	def update(self):
		super(Source,self).update()
		if self.rect.bottom < 0:
			self.kill()
