from pygame import *
from xd import *
from PyQt5.QtWidgets import QApplication

app_qt = QApplication([])

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
     sound.set_volume(mixer.music.get_volume()/2)
     sound.play()
     bullet = Bullet('bala.png', None, None, None, self.rect.right, self.rect.centery, 60, 35, 55)
     hero_bullets.add(bullet)


class Enemy(GameSprite):
    side = "left"
    def __init__(self, player_image, health, player_x, player_y, size_x, size_y, player_speed):
        GameSprite.__init__(self, player_image, player_x, player_y, size_x, size_y)
        self.health = health
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
        if self.health == 0:
            self.kill()

    def enemyfire(self):
        bullet = Bullet('bala.png', 2500, None, time.get_ticks(), self.rect.left, self.rect.centery, 35, 40, 8)
        enemy_bullets.add(bullet)


class Bullet(GameSprite):
    def __init__(self, player_image, tracking_duration, direction, creation_time, player_x, player_y, size_x, size_y, player_speed):
        GameSprite.__init__(self, player_image, player_x, player_y, size_x, size_y)
        self.tracking_duration = tracking_duration
        self.direction = direction
        self.creation_time = creation_time
        self.speed = player_speed
        self.x = player_x
    
    def chase(self, target):
        target_vector = math.Vector2(target.rect.centerx, target.rect.centery)
        follower_vector = math.Vector2(self.rect.centerx, self.rect.centery)
        direction_to_target = target_vector - follower_vector
        distance = direction_to_target.length()
        if distance > 0:
            direction_vector = direction_to_target.normalize()
            step_vector = direction_vector * self.speed
            if step_vector.length() > distance:
                step_vector = direction_to_target 
            new_follower_vector = follower_vector + step_vector
            return [new_follower_vector.x, new_follower_vector.y]
        else:
            return [follower_vector.x, follower_vector.y]

    def update(self, target):
        if self in enemy_bullets:
            current_time = time.get_ticks()
            time_elapsed = current_time - self.creation_time
            is_tracking = time_elapsed < self.tracking_duration
            if is_tracking == True:
                new_pos = self.chase(target) 
                self.rect.centerx = new_pos[0] 
                self.rect.centery = new_pos[1]
                if time_elapsed + (1000 / 60) >= self.tracking_duration:
                    self.direction = new_pos
            else:
                self.rect.x -= self.speed
        else:
            self.rect.x += self.speed
        if self.rect.x > win_width + 10:
            self.kill()

def reset_game():
    global finish, pausa, win_state, ultimo_disparo, current_finish_img, img_switch_delay, last_img_switch

    finish = False
    pausa = False
    win_state = None
    ultimo_disparo = 0
    current_finish_img = 1
    last_img_switch = time.get_ticks()

    packman.rect.x = 46
    packman.rect.y = 370
    packman.x_speed = 0
    packman.y_speed = 0

    hero_bullets.empty()
    enemy_bullets.empty()
    monsters.empty()

    global monster1, monster2, monster3, monster4
    monster1 = Enemy('enemigoo.png', 3, win_width - 80, 40, 80, 80, 5)
    monster2 = Enemy('enemigoo.png', 3, win_width - 80, 400, 80, 80, 5)
    monster3 = Enemy('enemigoo.png', 3, win_width - 80, 0, 80, 80, 5)
    monster4 = Enemy('enemigoo.png', 3, win_width - 80, 450, 80, 80, 5)

    monsters.add(monster1, monster2, monster3, monster4)
    
    mixer.music.load("Take a no. 5 and a no. 3.mp3")
    mixer.music.play(loops=-1)


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

monster1 = Enemy('enemigoo.png', 3, win_width - 80, 40, 80, 80, 5)
monster2 = Enemy('enemigoo.png', 3, win_width - 80, 400, 80, 80, 5)
monster3 = Enemy('enemigoo.png', 3, win_width - 80, 0, 80, 80, 5)
monster4 = Enemy('enemigoo.png', 3, win_width - 80, 450, 80, 80, 5)

monsters.add(monster1)
monsters.add(monster2)
monsters.add(monster3)
monsters.add(monster4)

escena = False
finish = False
pausa = False  

current_finish_img = 1
finish_screen_image = None
win_state = None
last_img_switch = time.get_ticks()
img_switch_delay = 500


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
                packman.x_speed = -7
            elif e.key == K_RIGHT:
                packman.x_speed = 7
            elif e.key == K_UP:
                packman.y_speed = -7
            elif e.key == K_DOWN:
                packman.y_speed = 7
            elif e.key == K_SPACE:
                if finish != False and win_state != None:
                    reset_game()
                elif not finish:
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
            hero_bullets.update(packman)
            enemy_bullets.update(packman)

            packman.reset()
            hero_bullets.draw(window)
            enemy_bullets.draw(window)
            barriers.draw(window)
            final_sprite.reset()

            sprite.groupcollide(enemy_bullets, barriers, False, False)

            for i in monsters:
                if sprite.spritecollide(i, hero_bullets, False):
                    sprite.groupcollide(monsters, hero_bullets, False, True)
                    i.health -= 1

            monsters.update()
            monsters.draw(window)
            
            if sprite.spritecollide(packman, enemy_bullets, True):
                finish = True
                win_state = 'loss'
                mixer.music.load("Capricho corso.mp3")
                mixer.music.play(loops=-1)
            

            if sprite.spritecollide(packman, monsters, False):
                finish = True
                win_state = 'loss' 
                mixer.music.load("Capricho corso.mp3")
                mixer.music.play(loops=-1)


            if sprite.collide_rect(packman, final_sprite):
                finish = True
                win_state = 'win' 
                mixer.music.load("Capricho corso.mp3")
                mixer.music.play(loops=-1)

            tiempo_transcurrido = time.get_ticks()
            if tiempo_transcurrido - ultimo_disparo > delay_para_disparar:
                if monster1.alive():
                    monster1.enemyfire()
                if monster2.alive():
                    monster2.enemyfire()
                ultimo_disparo = tiempo_transcurrido
    else:
        now = time.get_ticks()
        

        if now - last_img_switch > img_switch_delay:
            current_finish_img = 3 - current_finish_img
            last_img_switch = now

        if win_state == 'loss':
            if current_finish_img == 1:
                img_file = 'derrota.png'
            else:
                img_file = 'derrota1.png'
        elif win_state == 'win':
            if current_finish_img == 1:
                img_file = 'victoria.png'
            else:
                img_file = 'victoria1.png'
        else:
            img_file = 'fondo.png' 

        finish_screen_image = image.load(img_file)
        
        d = finish_screen_image.get_width() // finish_screen_image.get_height()
        window.fill((255, 255, 255))
        window.blit(transform.scale(finish_screen_image, (win_height * d, win_height)), (90, 0))
    
    display.update()

