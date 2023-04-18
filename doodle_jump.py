from pygame import *
from random import *
#? Классы 
#TODO Класс GameSprite 
class GameSprite (sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed, player_speed_y, player_speed_x):
        #?вызываем конструктор класса (Sprite):
        sprite.Sprite.__init__(self)


        #*каждый спрайт должен хранить свойство image - изображение
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.speed_y = player_speed_y
        self.speed_x = player_speed_x

        #*каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    #?метод, отрисовывающий героя на окне
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
#TODO Создаём класс игрока
class Player(GameSprite):
    #*метод для управления спрайтом стрелками клавиатуры
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 1:
            self.rect.x -= self.speed_x
        if keys[K_RIGHT] and self.rect.x < 350:
            self.rect.x += self.speed_x
        '''if keys(K_SPACE) and self.rect.y > 1 and jump == True:
            self.rect.y -= self.speed_y - 5
        if collider == True:
            self.rect.y += self.speed'''
#TODO Создаём класс платформ
class Platforms(GameSprite):
    #* Метод движения платформ
    def update(self):
        self.rect.y += self.speed

        if self.rect.y > 800:
            self.rect.x = randint(1, 330)
            self.rect.y = 0

#TODO Создаём окно
window = display.set_mode((400, 800))
display.set_caption('Doodle Jump')
background = transform.scale(image.load("background.png"), (400, 800))

#* Сдесь находятся экземпляры классов и переменные
game = True
jump = False
fiawe = 1
nums = [130, 260, 390, 520, 650, 780]
doodle = Player('doodle.png', 175, 600, 50, 50, fiawe, 40, 3)
platforms = sprite.Group()
clock = time.Clock()
FPS = 60
for i in nums:
    platform = Platforms('platform.png', randint(1, 370), i, 70, 30, fiawe, None, None)
    platforms.add(platform)
#? Игровой цикл
while game:

    for e in event.get():
        if e.type == QUIT:
            game = False
    
    window.blit(background, (0, 0))
    doodle.reset()
    platforms.draw(window)

    doodle.update()
    platforms.update()

    display.update() 
    clock.tick(FPS)