from pygame import *
from xd import *
from PyQt5.QtWidgets import QApplication

app_qt = QApplication([])

mixer.init()




mixer.init()

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
 def __init__(
     self, player_image, walk, walkcount, player_x, player_y, size_x, size_y, player_x_speed, player_y_speed):
     GameSprite.__init__(self, player_image, player_x, player_y, size_x, size_y)
     self.walk = walk
     self.walkcount = walkcount
     self.size_x = size_x
     self.size_y = size_y
     self.x_speed = player_x_speed
     self.y_speed = player_y_speed


 def update(self, win):
      if self.walkcount + 1 >= 80:
          self.walkcount = 0
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
      if self.y_speed != 0 or self.x_speed != 0:
          self.image = transform.scale(self.walk[int(self.walkcount%8)], (self.size_x, self.size_y))
          self.walkcount += 0.8
 def fire(self):
     sound = mixer.Sound("laser-gun-81720.mp3")
     sound.set_volume(0.3)
     sound.play()
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

img = image.load('fondo.png')
window.blit(transform.scale(img, (win_width, win_height)), (0, 0))

barriers = sprite.Group()
enemy_bullets = sprite.Group()
hero_bullets = sprite.Group()
monsters = sprite.Group()

w1 = GameSprite('estructura.png', -100, 450, 850, 60)
barriers.add(w1)

walk = [
    image.load('frame1.png'), image.load('frame2.png'), image.load('frame3.png'),image.load('frame4.png'), image.load('frame5.png'), image.load('frame6.png'), image.load('frame7.png'), image.load('frame8.png')]

packman = Player('frame1.png', walk, 0, 46, 370, 80, 80, 0, 0)
final_sprite = GameSprite('fin.png', win_width - 85, win_height - 100, 80, 80)

monster1 = Enemy('enemigoo.png', win_width - 80, 40, 80, 80, 5)
monster2 = Enemy('enemigoo.png', win_width - 80, 400, 80, 80, 5)
monster3 = Enemy('enemigoo.png', win_width - 80, 0, 80, 80, 5)
monster4 = Enemy('enemigoo.png', win_width - 80, 450, 80, 80, 5)

monsters.add(monster1)
monsters.add(monster2)
monsters.add(monster3)
monsters.add(monster4)

escena = False
finish = False
pausa = False  


mixer.music.load("Take a no. 5 and a no. 3.mp3")
mixer.music.play(loops=-1)
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
                    mixer.music.pause()
                    pausa = True

                    pausaa = VentanaPausa()
                    pausaa.exec_()

                    if pausaa.opcion == "continuar":
                        pausa = False
                        mixer.music.unpause()

                    elif pausaa.opcion == "salir":
                        run = False
                        pygame.quit()
                        exit()

                else: 
                    mixer.music.unpause()
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

            packman.update(window)
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
                mixer.music.load("Capricho corso.mp3")
                mixer.music.play(loops=-1)
                window.fill((255, 255, 255))
                window.blit(transform.scale(img, (win_height * d, win_height)), (90, 0))

            if sprite.spritecollide(packman, monsters, False):
                finish = True
                img = image.load('derrota.png')
                mixer.music.load("Capricho corso.mp3")
                mixer.music.play(loops=-1)
                d = img.get_width() // img.get_height()
                window.fill((255, 255, 255))
                window.blit(transform.scale(img, (win_height * d, win_height)), (90, 0))

            if sprite.collide_rect(packman, final_sprite):
                display.update()


            tiempo_transcurrido = time.get_ticks()
            if tiempo_transcurrido - ultimo_disparo > delay_para_disparar:
                if monster1.alive():
                    monster1.enemyfire()
                if monster2.alive():
                    monster2.enemyfire()
                ultimo_disparo = tiempo_transcurrido
    
    display.update()

