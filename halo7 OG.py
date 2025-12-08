
from pygame import *
#from pantallas.my_app import MiClaseDeMenu




#clase padre para otros sprites
class GameSprite(sprite.Sprite):
 #constructor de clase
 def __init__(self, player_image, player_x, player_y, size_x, size_y):
     # Llamada al constructor de la clase (Sprite):
     sprite.Sprite.__init__(self)
     # cada sprite debe almacenar la propiedad de imagen
     self.image = transform.scale(image.load(player_image), (size_x, size_y))


     # cada sprite debe almacenar la propiedad rect - el rectángulo en donde está dibujado
     self.rect = self.image.get_rect()
     self.rect.x = player_x
     self.rect.y = player_y
 # el método que dibuja al personaje en la ventana
 def reset(self):
     window.blit(self.image, (self.rect.x, self.rect.y))


# clase del jugador principal
class Player(GameSprite):
 # el método en el cual el sprite es controlado por las teclas de flechas del teclado
 def __init__(self, player_image, player_x, player_y, size_x, size_y, player_x_speed, player_y_speed):
     # Llamada al constructor de la clase (Sprite):
     GameSprite.__init__(self, player_image, player_x, player_y,size_x, size_y)


     self.x_speed = player_x_speed
     self.y_speed = player_y_speed


 def update(self):
      ''' mueve al personaje aplicando la velocidad actual en las direcciones horizontal y vertical'''
      # primero el movimiento horizontal
      if packman.rect.x <= win_width-80 and packman.x_speed > 0 or packman.rect.x >= 0 and packman.x_speed < 0:
        self.rect.x += self.x_speed
      # si vamos detrás de una pared, nos pararemos frente a él
      platforms_touched = sprite.spritecollide(self, barriers, False)
      if self.x_speed > 0: # vamos a la derecha, el borde derecho del personaje aparece frente al borde izquierdo de la pared
          for p in platforms_touched:
              self.rect.right = min(self.rect.right, p.rect.left) # si se tocaron varias paredes al mismo tiempo, entonces el borde derecho es el mínimo posible
      elif self.x_speed < 0: # vamos a la izquierda, ntonces colocamos el borde izquierdo del personaje frente al borde derecho de la pared
          for p in platforms_touched:
              self.rect.left = max(self.rect.left, p.rect.right) # si se tocaron varias paredes, entonces el borde izquierdo es el máximo
      if packman.rect.y <= win_height-80 and packman.y_speed > 0 or packman.rect.y >= 0 and packman.y_speed < 0:
        self.rect.y += self.y_speed
      # si vamos detrás de una pared, nos pararemos frente a él
      platforms_touched = sprite.spritecollide(self, barriers, False)
      if self.y_speed > 0: # yendo hacia abajo
          for p in platforms_touched:
              self.y_speed = 0
              # Estamos comprobando cuál de las plataformas es la más alta de las que están debajo, alineando con esta, y luego la tomamos somo apoyo:
              if p.rect.top < self.rect.bottom:
                  self.rect.bottom = p.rect.top
      elif self.y_speed < 0: # yendo hacia arriba
          for p in platforms_touched:
              self.y_speed = 0 # la velocidad vertical se amortigua al chocar con la pared
              self.rect.top = max(self.rect.top, p.rect.bottom) # alineando el borde superior contra los bordes inferiores de las paredes que se tocaron
 # el método "fire" (usamos la ubicación del jugador para crear una bala allí)
 def fire(self):
     bullet = Bullet('bala.png', self.rect.right, self.rect.centery, 60, 35, 55)
     hero_bullets.add(bullet)


# la clase del sprite del enemigo   
class Enemy(GameSprite):
 side = "left"
 def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
     # Llamada al constructor de la clase (Sprite):
     GameSprite.__init__(self, player_image, player_x, player_y, size_x, size_y)
     self.speed = player_speed


  #movimiento de un enemigo
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


# la clase del sprite de la bala  
class Bullet(GameSprite):
 def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
     # Llamada al constructor de la clase (Sprite):
     GameSprite.__init__(self, player_image, player_x, player_y, size_x, size_y)
     self.speed = player_speed
 #movimiento de un enemigo
 def update(self):
     self.rect.x += self.speed
     # desaparece después de alcanzar el borde de la pantalla
     if self.rect.x > win_width + 10:
         self.kill()


# Crear una ventana
win_width = 700
win_height = 500
display.set_caption("Halo 7")
window = display.set_mode((win_width, win_height))
icon = image.load('alfin.bmp')
display.set_icon(icon)
img = image.load('anillo.jpg')
window.blit(transform.scale(img, (win_width, win_height)), (0, 0))


#creando un grupo de paredes
barriers = sprite.Group()


# crear un grupo de balas
enemy_bullets = sprite.Group()
hero_bullets = sprite.Group()


# crear un grupo para los monstruos
monsters = sprite.Group()


# crear imágenes de las paredes
w1 = GameSprite('estructura.png',-100, 450, 850, 60)



# añadiendo paredes al grupo
barriers.add(w1)



# crear sprites
packman = Player('spartan.png', 46, 370, 80, 80, 0, 0)
final_sprite = GameSprite('fin.png', win_width - 85, win_height - 100, 80, 80)


monster1 = Enemy('sangeilii.png', win_width - 80, 40, 80, 80, 5)
monster2 = Enemy('sangeilii.png', win_width - 80, 400, 80, 80, 5)
monster3 = Enemy('sangeilii.png', win_width - 80, 0, 80, 80, 5)
monster4 = Enemy('sangeilii.png', win_width - 80, 450, 80, 80, 5)
# añadir un mosntruo al grupo
monsters.add(monster1)
monsters.add(monster2)
monsters.add(monster3)
monsters.add(monster4)



#la variable responsable de cómo terminó el juego
finish = False



# ciclo del juego
run = True
ultimo_disparo = 0
delay_para_disparar = 2000
while run:
 # el ciclo se activa cada 0,05 segundos
 time.delay(50)
  # iterar sobre todos los eventos que pudieron haber ocurrido
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


      elif e.type == KEYUP:
          if e.key == K_LEFT:
              packman.x_speed = 0
          elif e.key == K_RIGHT:
              packman.x_speed = 0
          elif e.key == K_UP:
              packman.y_speed = 0
          elif e.key == K_DOWN:
              packman.y_speed = 0


# comprobar que el juego todavía no haya finalizado
 if not finish:
     # actualizar el fondo cada iteración
     window.blit(img, (0, 0)) # rellenar la ventana con color
    
     # lanzar los movimientos de sprites
     packman.update()
     hero_bullets.update()
     enemy_bullets.update()


      # actualizarlas en una nueva ubicación en cada iteración del ciclo
     packman.reset()
     # dibujar las paredes 2
     #w1.reset()
     #w2.reset()
     hero_bullets.draw(window)
     enemy_bullets.draw(window)
     barriers.draw(window)
     final_sprite.reset()


     sprite.groupcollide(monsters, hero_bullets, True, True)
     sprite.groupcollide(enemy_bullets, barriers, False, False) # EXPLICALES LO QUE PASA CON EL PISO
     monsters.update()
     monsters.draw(window)


     # Comprobar la colisión del personaje con el enemigo y las paredes
     if sprite.spritecollide(packman, enemy_bullets, True):
        finish = True
        img = image.load('derrota.png')
        d = img.get_width() // img.get_height()
        window.fill((255, 255, 255))
        window.blit(transform.scale(img, (win_height * d, win_height)), (90, 0))
     if sprite.spritecollide(packman, monsters, False):
         finish = True
         # calcular la relación de aspecto
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
