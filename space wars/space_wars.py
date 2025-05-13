# adauga modulul pygame
import pygame  
import random 
from pygame.locals import *
from pygame import mixer
import time

# setarile jocului ################ ruleaza o singura data
speedp1 = 5
speedl = 10
speede1 = 1
speedb = 2
speedl2 = 5

pfp = pygame.image.load(r"boss.png")
pygame.display.set_caption('Space Wars')
pygame.display.set_icon(pfp)


# initializeaza pygame
pygame.init() 
mixer.init()
# ceas pentru a numara frame-urile pe sec
clock = pygame.time.Clock()  


#sunete
laserplayer = r'laser-shot-ingame-230500.mp3'
laser = pygame.mixer.Sound(laserplayer)
evillaugh = r'laser-shot-ingame-230500.mp3'
evill = pygame.mixer.Sound(evillaugh)
evill.set_volume(1.0)
channel = pygame.mixer.find_channel()
bkmusic = r'retro-game-music-245230.mp3'
pygame.mixer.music.load(bkmusic)
pygame.mixer.music.play()
pygame.mixer.music.play(loops=-1, start=0.0)
expl = r'small-explosion-106769.mp3'
exp = pygame.mixer.Sound(expl)
nextlvl = r'next-level-160613.mp3'
nlvl = pygame.mixer.Sound(nextlvl)
laser.set_volume(0.5)
nlvl.set_volume(0.1)


# numarul de frame-uri pe sec (viteza jocului)
FPS = 60  

# dimensiunea ecranului
SCREENSIZE = SCREENWIDTH, SCREENHEIGHT = 800, 600  

# initializeaza fereastra de joc
screen = pygame.display.set_mode(SCREENSIZE)  

# variabile pentru culori RGB (0-255)
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
yellow = (255, 255, 0)
green = (0, 255, 0)

# variabila ce ne indica stadiul jocului
gameState = "running"  




backgroundImage = pygame.image.load(r"bg_spw.png")
backgroundImage1 = pygame.transform.scale(backgroundImage, SCREENSIZE)

p = pygame.image.load(r"pngegg.png")
p1 = pygame.transform.scale(p,(100,80))
p1_rect = p1.get_rect()
p1_rect.y = 10



l = pygame.image.load(r"laser.png")
l1 = pygame.transform.scale(l,(30,50))
l1_rect = l1.get_rect()
l1_rect.y = p1_rect.y 
l1_rect.x = p1_rect.x+50







l21 = pygame.image.load(r"boslaser.png")
l2 = pygame.transform.scale(l21,(30,50))
l2_rect = l2.get_rect()





 



e = pygame.image.load(r"enemy.png")
e1 = pygame.transform.scale(e,(100,80))
e1_rect = e1.get_rect()
e1_rect.x = 10
e2 = e1
e3 =e1
e4 = e1
e5 = e1
e2_rect = e2.get_rect()
e2_rect.x = 150
e3_rect = e3.get_rect()
e3_rect.x = 350
e4_rect = e4.get_rect()
e4_rect.x = 500
e5_rect = e5.get_rect()
e5_rect.x = 700


y_position = 10 


e1_rect.y = -150
e5_rect.y =-150
e4_rect.y = -150
e3_rect.y = -150
e2_rect.y = -150



b = pygame.image.load(r"boss.png")
b1 = pygame.transform.scale(b,(500,200))
b1_rect = b1.get_rect()
b1_rect.y = -250
b1_rect.x = 150
bosslife = 30


l2_rect.y = b1_rect.y 
l2_rect.x = b1_rect.x

score = 0
life = 3


draw = True
boss = True


set_time = 0
first = True


smallfont = pygame.font.SysFont('Arial',50)
def textdraw(text,font,x,y,size,colour):
  font = pygame.font.SysFont(None, 50)
  text = font.render(text,True,yellow,None)
  screen.blit(text,(0,0))
def textdraw2(text,font,x,y,size,colour):
  font = pygame.font.SysFont(None, 50)
  text = font.render(text,True,red,None)
  screen.blit(text,(0,40))

font2 = pygame.font.SysFont(None, 50)
text2 = font2.render("ALL CLEAR TRY AND GET",True,green,None)
text3 = font2.render("A HIGH SCORE NOW",True,green,None)
text4 = font2.render("YOU LOST",True,green,None)




# loop-ul jocului #################### ruleaza de 60 de ori pe sec
while gameState != "exit":
  # verifica evenimentele cu userul (ex. tastatura, click etc. )
  for event in pygame.event.get(): 
    # daca buntonul de X al ferestrei a fost apasat
    if event.type == pygame.QUIT:  
      # se iese din joc
      gameState = "exit"  
  
  # codul tau incepe aici ##############################
  screen.blit(backgroundImage1,(0,0))
  
  screen.blit(l1,l1_rect)
  screen.blit(p1,p1_rect)
  
  
  textdraw("Score: " + str(score), None,20,20,50,green)
  textdraw2("Life: " + str(life), None,20,40,50,green)
  
  if draw :
    screen.blit(e1,e1_rect)
    screen.blit(e2,e2_rect)
    screen.blit(e3,e3_rect)
    screen.blit(e4,e4_rect)
    screen.blit(e5,e5_rect)
    e1_rect.y += speede1
    e5_rect.y += speede1
    e4_rect.y += speede1
    e3_rect.y += speede1
    e2_rect.y += speede1
  else:
    e1_rect.y = -150
    e2_rect.y = -150
    e3_rect.y = -150
    e4_rect.y = -150
    e5_rect.y = -150
    
  
  screen.blit(b1,b1_rect)
  #boss
  if score == 20 or score == 100 or score == 150 and boss :
    draw = False
    screen.blit(b1,b1_rect)
    if b1_rect.y != 50:
      b1_rect.y += speedb
      if channel:
        channel.play(evill)
    b1_rect.x += speedb
    if b1_rect.x == SCREENWIDTH - 250:
      speedb = -5
    if b1_rect.x == -50:
      speedb = 5
    if b1_rect.y == 50:
      screen.blit(l2,l2_rect)
      l2_rect.y += speedl2
      
    if l2_rect.y > SCREENHEIGHT:
      l2_rect.y =b1_rect.y
      l2_rect.x = b1_rect.x
    if l2_rect.colliderect(p1_rect):
      life -= 1
      l2_rect.y =b1_rect.y
      l2_rect.x = b1_rect.x
    if l1_rect.colliderect(b1_rect):
      bosslife -= 1
      l1_rect.y = p1_rect.y
      l1_rect.x = p1_rect.x
    if bosslife <= 0: 
      boss =False
      draw = True
      score += 20
      
      
  if boss == False:
    b1_rect.y = -250
    
    
  
  if score == 40:
    
    p = pygame.image.load(r"p2.png") 
    p1 = pygame.transform.scale(p,(100,80))
    l = pygame.image.load(r"boslaser.png")
    l1 = pygame.transform.scale(l,(30,50))
    speedl = 12
    nlvl.play()
    
  #boss 2 
  if score == 99 :
    b = pygame.image.load(r"b2.png")
    b1 = pygame.transform.scale(b,(500,200))
    boss = True
    bosslife = 40
    
    
  if score >= 120:
    speedl = 8
    speedp1 = 3 
    screen.blit(text2,(0,70))
    screen.blit(text3,(0,110))
    
    
 
 
 

  if l1_rect.y == p1_rect.y :
    laser.play()
  
  

        
        
  current_time = pygame.time.get_ticks()     
  if first == True:
    # peste 3 sec fata de timpul curent
    set_time = current_time + 3000 #3s
    # il facem false pe first pt a nu seta din nou timpul la urmatorul frame
    first = False

  # daca timpul curent ajunge sa fie mai mare sau egal cu timpul setat de noi
  if current_time >= set_time:
    l1_rect.y -= speedl
    

  if l1_rect.colliderect(e1_rect):
    e1_rect.y = -75
    e1_rect.x = random.randint(10,SCREENWIDTH-100)
    l1_rect.y = p1_rect.y
    l1_rect.x = p1_rect.x
    score += 1
    exp.play()
        
      
  if l1_rect.colliderect(e2_rect):
    e2_rect.y = -75
    e2_rect.x = random.randint(10,SCREENWIDTH-100)
    l1_rect.y = p1_rect.y
    l1_rect.x = p1_rect.x
    score += 1
    exp.play()
    
  if l1_rect.colliderect(e3_rect):
    e3_rect.y = -75
    e3_rect.x = random.randint(10,SCREENWIDTH-100)
    l1_rect.y = p1_rect.y
    l1_rect.x = p1_rect.x
    score += 1
    exp.play()
    
  if l1_rect.colliderect(e4_rect):
    e4_rect.y = -75
    e4_rect.x = random.randint(10,SCREENWIDTH-100)
    l1_rect.y = p1_rect.y
    l1_rect.x = p1_rect.x
    score += 1
    exp.play()
    
  if l1_rect.colliderect(e5_rect):
    e5_rect.y = -75
    e5_rect.x = random.randint(10,SCREENWIDTH-100)
    l1_rect.y = p1_rect.y
    l1_rect.x = p1_rect.x
    score += 1  
    exp.play()
  if p1_rect.y == e1_rect.y or  p1_rect.y == e2_rect.y or  p1_rect.y == e3_rect.y or  p1_rect.y == e4_rect.y or  p1_rect.y == e5_rect.y:
    life -= 1
    e1_rect.y = 10
    e5_rect.y =10 
    e4_rect.y = 10
    e3_rect.y = 10
    e2_rect.y = 10
  
  p1_rect.y = 500
  
  
  
  
  
  
  
  keys = pygame.key.get_pressed()
  if keys[pygame.K_LEFT]:
    if p1_rect.x > 0:
      p1_rect.x -= speedp1
  if keys[pygame.K_RIGHT]:
    if p1_rect.x < SCREENWIDTH - 100:
      p1_rect.x += speedp1
  
     
      
      
  if l1_rect.y < 0:
      l1_rect.x =  p1_rect.x
      l1_rect.y = p1_rect.y
      
    
  if life == 0:
    screen.blit(text4,(300,300))  
    draw = False
    speedl = 0
    speedp1 = 0
      
      
      

    

  # codul tau se termina aici ###############################
  
  # updateaza ecranul
  pygame.display.flip()
  # numara frame-urile pe secunda
  clock.tick(FPS) 

# am iesit in afara loop-ului jocului ###############

# printam ca jocul s-a incheiat
print("The game has closed")

# oprim pygame
pygame.quit()