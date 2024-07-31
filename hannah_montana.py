import time
import random
import pygame
import pyglet
from pygame import mixer
stop_x_attack=False
x_again=False
pygame.display.set_caption("Hannah Montana")
mixer.init()
music_path=r"C:\\Users\\user\\Downloads\\Sakura-Girl-Daisy-chosic.com_.mp3"
music=pyglet.media.load(music_path)
music.play()
t=0.2
poop_color=(122,89,1)
score=0
pygame.font.init()
pygame.font.get_init()
font1=pygame.font.SysFont("None",30)
pygame.init()
width=1200
heigth=600
x=width//2
y=heigth//2
xfood=random.randint(0,width-10)
xfood=xfood-xfood%100
yfood=random.randint(0,heigth-10)
yfood=yfood-yfood%100
window=pygame.display.set_mode((width,heigth))
window.fill((0,0,0))
pygame.display.flip()
start_font=pygame.font.SysFont("None",50)
start_message1="Hanna Montana needs to eat cock and run from the mad cow."
start_message2="Good luck Hannah!!!   :)"
start_text1=start_font.render(start_message1,True,(255,0,0))
start_text2=start_font.render(start_message2,True,(255,0,0))
start_rect1=start_text1.get_rect()
start_rect2=start_text2.get_rect()
start_rect1.center=(width//2,heigth//2)
start_rect2.center=(width//2,heigth//2+50)
window.blit(start_text1,start_rect1)
pygame.display.flip()
time.sleep(2)
window.blit(start_text2,start_rect2)
pygame.display.flip()
time.sleep(5)
window.fill((0,0,0))
alert_font=pygame.font.SysFont("None",50)
alert_text=alert_font.render("Start!",True,(255,0,0))
alert_rect=alert_text.get_rect()
alert_rect.center=(width//2,heigth//2)
window.blit(alert_text,alert_rect)
pygame.display.flip()
time.sleep(1)
window.fill(poop_color)
#C:\Users\user\Desktop\images_\dick.jpg
dick=pygame.image.load(r"C:\\Users\\user\\Desktop\\images_\\dick.jpg")
hana_montana=pygame.image.load(r"C:\\Users\\user\\Desktop\\images_\\hana_montana.jpg")
pygame.display.set_icon(hana_montana)
window.blit(hana_montana,[x,y])
crazy_cow=pygame.image.load(r"C:\\Users\\user\\Desktop\\images_\\crazy_cow2.jpg")
x_attack=200
y_attack=200
x_attack_change=100
y_attack_change=100
x_attack_anterior=x_attack
y_attack_anterior=y_attack
counter=0
running=True
x_change=0
y_change=0
x_anterior=-1
y_anterior=-1
window.blit(crazy_cow,[x_attack,y_attack])
pygame.display.flip()
while running:
    if counter==161*4:
        music=pyglet.media.load(music_path)
        music.play()
        counter=0
    counter+=1
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                x_change=-100
                y_change=0
            elif event.key==pygame.K_RIGHT:
                x_change=100
                y_change=0
            elif event.key==pygame.K_UP:
                x_change=0
                y_change=-100
            elif event.key==pygame.K_DOWN:
                y_change=100
                x_change=0
    x_anterior=x
    y_anterior=y
    if x_change==-100 and x!=0:
        x+=x_change
    elif x_change==100 and x!=width-100:
        x+=x_change
    elif y_change==-100 and y!=0:
        y+=y_change
    elif y_change==100 and y!=heigth-100:
        y+=y_change
    time.sleep(t)
    if x==xfood and y==yfood:
        xfood=random.randint(0,width-100)
        yfood=random.randint(0,heigth-100)
        xfood=xfood-xfood%100
        yfood=yfood-yfood%100
        score+=1
        if t-0.01>0:
            t-=0.01
    #pygame.draw.rect(window,(255,0,0),[xfood,yfood,10,10])
    text1=font1.render(f"Score : {score}",True,(0,255,0))
    rect1=text1.get_rect()
    rect1.center=(50,20)
    if x!=0 and y!=0:
        pygame.draw.rect(window,poop_color,[0,0,100,100])
    window.blit(text1,rect1)
    window.blit(dick, ([xfood, yfood]))
    if x!=x_anterior or y!=y_anterior:
        pygame.draw.rect(window,poop_color,[x_anterior,y_anterior,100,100])
        window.blit(hana_montana,[x,y])
    if (x_attack==x and y_attack==y) or (y_attack==y and x==x_attack-0 and x_change==100 and x_attack_change==-100) or (y_attack==y and x==x_attack+0 and x_change==-100 and x_attack_change==100) or (x==x_attack and y_attack==y-0 and y_change==-100 and y_attack_change==100) or (x==x_attack and y_attack==y+0 and y_change==100 and y_attack_change==-100):
        running=False
        font2=pygame.font.SysFont("None",40)
        text2=font2.render(f"You lost.Your score is {score}.",True,(255,0,0))
        rect2=text2.get_rect()
        rect2.center=(width//2,heigth//2)
        window.fill((255,255,255))
        window.blit(text2,rect2)
        time.sleep(2)
    else:
        x_attack_anterior=x_attack
        y_attack_anterior=y_attack
        if x_again==True:
            x_attack+=x_attack_change
            x_again=False
        if x_attack == 0 or x_attack == width - 100:
            x_attack_change *= -1
            y_attack+= y_attack_change
            stop_x_attack=True
        if y_attack == 0 or y_attack == heigth - 100:
            y_attack_change *= -1
        if stop_x_attack==False:
            x_attack+=x_attack_change
        else:
            stop_x_attack=False
            x_again=True
        window.blit(crazy_cow,[x_attack,y_attack])
        if x_attack!=x_attack_anterior or y_attack!=y_attack_anterior:
            pygame.draw.rect(window,poop_color,[x_attack_anterior,y_attack_anterior,100,100])
    pygame.display.flip()
    if running==False:
        time.sleep(3)
print("Thank you for trying my game.")
print("developer email:kingambitrap@gmail.com")