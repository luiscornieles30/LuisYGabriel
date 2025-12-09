from pygame import *
# from my_app import *


#clase padre para otros sprites
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_x_speed, player_y_speed):
        GameSprite.__init__(self, player_image, player_x, player_y, size_x, size_y)
        self.x_speed = player_x_speed
        self.y_speed = player_y_speed

    def update(self):
        if packman.rect.x <= win_width-80 and packman.x_speed > 0 or packman.rect.x >= 0 and packman.x_speed < 0:
            self.rect.x += self.x_speed
        platforms_touched = sprite.spritecollide(self, barriers, False)
        if self.x_speed > 0:
            for p in platforms_touched:
                self.rect.right = min(self.rect.right, p.rect.left)
        elif self.x_speed < 0:
            for p in platforms_touched:
                self.rect.left = max(self.rect.left, p.rect.right)

        if packman.rect.y <= win_height-80 and packman.y_speed > 0 or packman.rect.y >= 0 and packman.y_speed < 0:
            self.rect.y += self.y_speed
        platforms_touched = sprite.spritecollide(self, barriers, False)
        if self.y_speed > 0:
            for p in platforms_touched:
                self.y_speed = 0
                if p.rect.top < self.rect.bottom:
                    self.rect.bottom = p.rect.top
        elif self.y_speed < 0:
            for p in platforms_touched:
                self.y_speed = 0
                self.rect.top = max(self.rect.top, p.rect.bottom)

    def fire(self):
        bullet = Bullet('bala.png', self.rect.right, self.rect.centery, 60, 35, 55)
        hero_bullets.add(bullet)


class Enemy(GameSprite):
    side = "left"
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        GameSprite.__init__(self, player_image, player_x, player_y, size_x, size_y)
        self.speed = player_speed

    def update(self):
        if self.rect.y <= 50:
            self.side = "abajo"
        if self.side == "abajo":
            self.rect.y += self.speed
        if self.rect.y >= 400:
            self.side = "arriba"
        if self.side == "arriba":
            self.rect.y -= self.speed

    def enemyfire(self):
        bullet = Bullet('bala.png', self.rect.left, self.rect.centery, 35, 40, -15)
        enemy_bullets.add(bullet)


class Bullet(GameSprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        GameSprite.__init__(self, player_image, player_x, player_y, size_x, size_y)
        self.speed = player_speed

    def update(self):
        self.rect.x += self.speed
        if self.rect.x > win_width + 10:
            self.kill()


win_width = 700
win_height = 500
display.set_caption("Halo 7")
window = display.set_mode((win_width, win_height))

icon = image.load('alfin.bmp')
display.set_icon(icon)

img = image.load('anillo.jpg')
window.blit(transform.scale(img, (win_width, win_height)), (0, 0))

barriers = sprite.Group()
enemy_bullets = sprite.Group()
hero_bullets = sprite.Group()
monsters = sprite.Group()

w1 = GameSprite('estructura.png', -100, 450, 850, 60)
barriers.add(w1)

packman = Player('spartan.png', 46, 370, 80, 80, 0, 0)
final_sprite = GameSprite('fin.png', win_width - 85, win_height - 100, 80, 80)

monster1 = Enemy('sangeilii.png', win_width - 80, 40, 80, 80, 5)
monster2 = Enemy('sangeilii.png', win_width - 80, 400, 80, 80, 5)
monster3 = Enemy('sangeilii.png', win_width - 80, 0, 80, 80, 5)
monster4 = Enemy('sangeilii.png', win_width - 80, 450, 80, 80, 5)

monsters.add(monster1)
monsters.add(monster2)
monsters.add(monster3)
monsters.add(monster4)

finish = False
pausa = False  

run = True
ultimo_disparo = 0
delay_para_disparar = 2000

while run:
    time.delay(50)

    for e in event.get():
        if e.type == QUIT:
            run = False

        elif e.type == KEYDOWN:
            if e.key == K_LEFT:
                packman.x_speed = -5
            elif e.key == K_RIGHT:
                packman.x_speed = 5
            elif e.key == K_UP:
                packman.y_speed = -5
            elif e.key == K_DOWN:
                packman.y_speed = 5
            elif e.key == K_SPACE:
                packman.fire()

            elif e.key == K_ESCAPE:  
                if pausa == False:
                    pausa = True
                else: 
                    pausa = False

        elif e.type == KEYUP:
            if e.key == K_LEFT:
                packman.x_speed = 0
            elif e.key == K_RIGHT:
                packman.x_speed = 0
            elif e.key == K_UP:
                packman.y_speed = 0
            elif e.key == K_DOWN:
                packman.y_speed = 0


    if not finish:
        if pausa == False: 

            window.blit(img, (0, 0))

            packman.update()
            hero_bullets.update()
            enemy_bullets.update()

            packman.reset()
            hero_bullets.draw(window)
            enemy_bullets.draw(window)
            barriers.draw(window)
            final_sprite.reset()

            sprite.groupcollide(monsters, hero_bullets, True, True)
            sprite.groupcollide(enemy_bullets, barriers, False, False)

            monsters.update()
            monsters.draw(window)

            if sprite.spritecollide(packman, enemy_bullets, True):
                finish = True
                img = image.load('derrota.png')
                d = img.get_width() // img.get_height()
                window.fill((255, 255, 255))
                window.blit(transform.scale(img, (win_height * d, win_height)), (90, 0))

            if sprite.spritecollide(packman, monsters, False):
                finish = True
                img = image.load('derrota.png')
                d = img.get_width() // img.get_height()
                window.fill((255, 255, 255))
                window.blit(transform.scale(img, (win_height * d, win_height)), (90, 0))

            if sprite.collide_rect(packman, final_sprite):
                finish = True
                img = image.load('victoria.png')
                window.fill((255, 255, 255))
                window.blit(transform.scale(img, (win_width, win_height)), (0, 0))

            tiempo_transcurrido = time.get_ticks()
            if tiempo_transcurrido - ultimo_disparo > delay_para_disparar:
                if monster1.alive():
                    monster1.enemyfire()
                if monster2.alive():
                    monster2.enemyfire()
                ultimo_disparo = tiempo_transcurrido

        display.update()
