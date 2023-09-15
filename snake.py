import pygame
import random
import os
pygame.mixer.init()
pygame.init()
a=(255,34,65)
black=(0,0,0)
n=(255,255,255)
game_window=pygame.display.set_mode((1200,500))
pygame.display.set_caption("SNAKE GAME")
bg=pygame.image.load("images.jpeg")
bg = pygame.transform.scale(bg, (1200 , 500)).convert_alpha()
b=pygame.image.load("download.jpeg")
b = pygame.transform.scale(b, (950, 600)).convert_alpha()
g=pygame.image.load("images (1).jpeg")
g = pygame.transform.scale(g, (1200, 600)).convert_alpha()
font=pygame.font.SysFont(None,30)
def poly(game_window,color,list,p,q):
    for x,y in list:
      pygame.draw.rect(game_window,color,[x,y,p,q])
def func(text,color,x,y):
   screen=font.render(text,True,color)
   game_window.blit(screen,[x,y])
clock=pygame.time.Clock()
def welvome():
   pygame.mixer.music.load('mellow-reverse-opening-flyby-SBA-300420849-preview (1) (mp3cut.net).mp3')
   pygame.mixer.music.play()
   game_window.fill(black)
   game_window.blit(b,(0,0))
   func("!!WELCOME TO SNAKES!!",(0,200,255),650,200)
   func("   PRESS SPACE TO PLAY",(0,200,255),650,240)
   exit_game=False
   while not exit_game:
      for events in pygame.event.get():
          if (events.type==pygame.QUIT):
            exit_game=True
          if (events.type==pygame.KEYDOWN):
            if events.key==pygame.K_SPACE:
               pygame.mixer.music.load('Jhoome Jo Pathaan_320(PagalWorld.cm).mp3')
               pygame.mixer.music.play()
               game_loop()
      pygame.display.update()  
def game_loop():
   snake_list=[]
   snake_length=1
   exit_game=False
   quit_game=False
   x=600
   y=250
   score=0
   p=10
   q=10
   f_x=random.randint(20,600)
   f_y=random.randint(20,250)
   vel_x=0
   vel_y=0
   init=5
   fps=30
   if not os.path.exists("high.txt"):
       with open("high.txt","w") as f:
         f.write("0")
   with open("high.txt","r") as f:
       highscore=f.read()
   while not exit_game:
    
      if quit_game:
         with open("high.txt","w") as f:
            f.write(str(highscore))
         game_window.fill((255,255,255))
         game_window.blit(g,(0,0))
         func("GAME OVER!! PRESS ENTER TO CONTINUE",(255,255,255),400,230)
         for events in pygame.event.get():
            if (events.type==pygame.QUIT):
               exit_game=True
            if events.type==pygame.KEYDOWN :
               if events.key==pygame.K_RETURN:
                  welvome()
      else:
         for events in pygame.event.get():
            if (events.type==pygame.QUIT):
               exit_game=True
            if events.type==pygame.KEYDOWN :
               if events.key==pygame.K_RIGHT or events.key==pygame.K_i:
                  vel_x=init
                  vel_y=0
               elif events.key==pygame.K_LEFT or events.key==pygame.K_e:
                  vel_x=-init
                  vel_y=0
               elif events.key==pygame.K_UP:
                  vel_y=-init
                  vel_x=0
               elif events.key==pygame.K_DOWN:
                  vel_y=init
                  vel_x=0
               elif events.key==pygame.K_q:
                  score+=5
         x=x+vel_x
         y=y+vel_y
         if(abs(x-f_x)<6 and abs(y-f_y)<6):
           
            score+=10
            if score> int(highscore):
               highscore=score
            f_x=random.randint(20,600)
            f_y=random.randint(20,250)
            init=init+1
            snake_length+=3
         head=[]
         head.append(x)
         head.append(y)
         snake_list.append(head)
         if len(snake_list)>snake_length:
            del snake_list[0]
         if head in snake_list[:-1]:
            pygame.mixer.music.load('mixkit-arcade-retro-run-sound-220.wav')
            pygame.mixer.music.play()
            
            quit_game=True
         if x<0 or x>1200 or y<0 or y>500:
            pygame.mixer.music.load('mixkit-arcade-retro-run-sound-220.wav')
            pygame.mixer.music.play()
            quit_game=True
         
         game_window.fill((255,255,255))
         game_window.blit(bg,(0,0))
         poly(game_window,n,snake_list,p,q)
         func("SCORE: "+str(score)+"        HIGH SCORE :"+str(highscore),a,5,5)
         pygame.draw.rect(game_window,(0,0,255),pygame.Rect(f_x,f_y,10,10))
      clock.tick(fps)
      pygame.display.update()   
welvome()