
import pygame
import pygame.event
import pygame.locals

from  pygame import*

pygame.init()
class world:
    def __init__(self,x=500,y=500):
        self.wid=x
        self.hei=y
        self.win=None


    def draw(self):
        import pygame
        pygame.init()
        self.win=pygame.display.set_mode((self.wid,self.hei))
        surface=self.win
        x = 0
        x1 = 50
        x2 = 100
        x3 = 150
        x4 = 200
        x5 = 250
        x6 = 300
        x7 = 350
        x8 = 400
        x9 = 450
        b = 5
        surface.fill((0, 0, 0))
        #pygame.draw.rect(surface, (255, 255, 255), (50, 50, 350, 450))   #safhe
        #pygame.draw.rect(surface, (204, 255, 204), (40, 40, 370, 10))    #hashie
        #pygame.draw.rect(surface, (204, 255, 204), (40, 500, 370, 10))   #hashie
        #pygame.draw.rect(surface, (204, 255, 204), (40, 40, 10, 460))    #hashie
        #pygame.draw.rect(surface, (204, 255, 204), (400, 40, 10, 460))   #hashie
        pygame.draw.rect(surface, (255, 255, 0), (x1, x, b, x2))      #divar1
        pygame.draw.rect(surface, (255, 255, 0), (x3, x, b, x1))      #divar2
        pygame.draw.rect(surface, (255, 255, 0), (x5, x, b, x1))      #divar3
        pygame.draw.rect(surface, (255, 255, 0), (x6, x, b, x1))      #divar4
        pygame.draw.rect(surface, (255, 255, 0), (x,  x1, x4, b))     #divar5
        pygame.draw.rect(surface, (255, 255, 0), (x6, x1, x4, b))     #divar6
        pygame.draw.rect(surface, (255, 255, 0), (x2, x1, b, x2))     #divar7
        pygame.draw.rect(surface, (255, 255, 0), (x2, x2, x2, b))     #divar8
        pygame.draw.rect(surface, (255, 255, 0), (x5, x2, x3, b))     #divar9
        pygame.draw.rect(surface, (255, 255, 0), (x, x3, x2+5, b))    #divar10
        pygame.draw.rect(surface, (255, 255, 0), (x3, x2, b, x2))     #divar11
        pygame.draw.rect(surface, (255, 255, 0), (x3, x3, x1, b))     #divar12
        pygame.draw.rect(surface, (255, 255, 0), (x5, x2, b, x1))     #divar13
        pygame.draw.rect(surface, (255, 255, 0), (x1, x4, x2+5, b))   #divar14
        pygame.draw.rect(surface, (255, 255, 0), (x4, x4, x2+5, b))   #divar15
        pygame.draw.rect(surface, (255, 255, 0), (x6, x3, b, x1))     #divar16
        pygame.draw.rect(surface, (255, 255, 0), (x1, x4, b, x1))     #divar17
        pygame.draw.rect(surface, (255, 255, 0), (x2, x4, b, x2))     #divar18
        pygame.draw.rect(surface, (255, 255, 0), (x1, x5, x1, b))     #divar19
        pygame.draw.rect(surface, (255, 255, 0), (x3, x5, x2, b))     #divar20
        pygame.draw.rect(surface, (255, 255, 0), (x6, x5, x1, b))     #divar21
        pygame.draw.rect(surface, (255, 255, 0), (x, x6, x1, b))      #divar22
        pygame.draw.rect(surface, (255, 255, 0), (x3, x5, b, x1))     #divar23
        pygame.draw.rect(surface, (255, 255, 0), (x4, x5, b, x2))     #divar24
        pygame.draw.rect(surface, (255, 255, 0), (x6, x5, b, x1))     #divar25
        pygame.draw.rect(surface, (255, 255, 0), (x3, x6, x2, b))     #divar26
        pygame.draw.rect(surface, (255, 255, 0), (x6, x6, x1, b))     #divar27
        pygame.draw.rect(surface, (255, 255, 0), (x1, x6, b, x2))     #divar28
        pygame.draw.rect(surface, (255, 255, 0), (x,  x8, x1+5, b))   #divar29
        pygame.draw.rect(surface, (255, 255, 0), (x2, x7, b, x2))     #divar30
        pygame.draw.rect(surface, (255, 255, 0), (x3, x7, b, x1))     #divar31
        pygame.draw.rect(surface, (255, 255, 0), (x5, x7, x1, b))     #divar32
        pygame.draw.rect(surface, (255, 255, 0), (x2, x8, x2, b))     #divar33
        pygame.draw.rect(surface, (255, 255, 0), (x5, x8, b, x1))     #divar34
        pygame.draw.rect(surface, (255, 255, 0), (x6, x8, b, x1))     #divar35
        pygame.draw.rect(surface, (255, 255, 0), (x7, x, b, x4))      #divar36
        pygame.draw.rect(surface, (255, 255, 0), (x, x9, x5+5, b))      #divar37
        pygame.draw.rect(surface, (255, 255, 0), (x7, x5, b, x4))     #divar38
        pygame.draw.rect(surface, (255, 255, 0), (x8, x2, b, x6))     #divar39
        pygame.draw.rect(surface, (255, 255, 0), (x9, x1, b, x1))     #divar40
        pygame.draw.rect(surface, (255, 255, 0), (x8, x4, x1, b))     #divar41
        pygame.draw.rect(surface, (255, 255, 0), (x8, x8, x1+5, b))     #divar42
        pygame.draw.rect(surface, (255, 255, 0), (x9, x6, b, x2))     #divar43
        pygame.draw.rect(surface, (255, 255, 0), (x6, x9, x2, b))     #divar44
        pygame.draw.rect(surface, (255, 255, 0), (x9, x9, x1, b))     #divar45
def ghadr(n):
    return int((n**2)**0.5)
def gherd(n):
    s=n-int(n)
    if s>=0.5:
        return int(n)+1
    elif s<0.5:
        return int(n)
    elif s==0:
        return int(n)
class tank:
    import pygame
    import math
    import pygame.event
    def __init__(self):
        self.counterx=0
        self.countery=0
        self.x1=None
        self.y1=None
        self.x2=None
        self.y2=None
        self.x3=None
        self.y3=None
        self.x4=None
        self.y4=None
        self.shovel=3
        self.m=None
        self.w_key=False
        self.wid=20
        self.center=[5+self.wid//2,160+self.wid//2]
        self.radium=5
        self.mouse=pygame.mouse.get_pos()
    def draw(self):
        self.mouse=pygame.mouse.get_pos()
        self.center[1]=-self.center[1]
        w=-self.mouse[1]
        b=self.center[1]-w
        a=self.center[0]-self.mouse[0]
        if a!=0 and -18<b<18 :
            self.center[1]=-self.center[1]
            x1=self.center[0]-self.wid//2
            
            x2=x1
            x3=self.center[0]+self.wid//2
            x4=x3
            y1=self.center[1]-self.wid//2
            y3=y1
            y2=self.center[1]+self.wid//2
            y4=y2
            self.m=0
            m=0
            if  world.win.get_at((ghadr(x1),ghadr(y1)))==(255,255,0,255):
                self.m=1
            else:
                m+=1
                
            if world.win.get_at((ghadr(x2),ghadr(y2)))==(255,255,0,255):
                self.m=1
            else:
                m+=1
            if world.win.get_at((ghadr(x3),ghadr(y3)))==(255,255,0,255):
                self.m=1
            else:
                m+=1
            if world.win.get_at((ghadr(x4),ghadr(y4)))==(255,255,0,255):
                self.m=1
            else:
                m+=1
            if self.m==0 and m>0:
                self.x1=ghadr(x1)
                self.x2=ghadr(x2)
                self.x3=ghadr(x3)
                self.x4=ghadr(x4)
                self.y1=ghadr(y1)
                self.y2=ghadr(y2)
                self.y3=ghadr(y3)
                self.y4=ghadr(y4)
                self.m=0
            pygame.draw.line(world.win,(0,200,0),(self.x1,self.y1),(self.x3,self.y3),3)
            
            pygame.draw.line(world.win,(0,200,0),(self.x1,self.y1),(self.x2,self.y2),3)
            pygame.draw.line(world.win,(0,200,0),(self.x4,self.y4),(self.x3,self.y3),3)
            pygame.draw.line(world.win,(0,200,0),(self.x2,self.y2),(self.x4,self.y4),3)



            pygame.draw.circle(world.win,(0,200,0),(self.center[0],self.center[1]),self.radium)
            if self.center[0]>self.mouse[0]:
                pygame.draw.line(world.win,(200,0,0),(self.center[0],self.center[1]),(self.center[0]-8,self.center[1]))
        
            else:
                pygame.draw.line(world.win,(200,0,0),(self.center[0],self.center[1]),(self.center[0]+8,self.center[1]))
            pygame.display.update()

        elif a!=0 and b!=0:
            #ax+by+c=0
            c=-(a*self.center[0]+b*self.center[1])

            c1=(self.wid//2)*((a**2+b**2)**0.5)-(a*self.center[0])-(b*self.center[1])
            #s=(c-c1)//((a**2+b**2)**0.5)
            
            c2=(-self.wid//2)*((a**2+b**2)**0.5)-(a*self.center[0])-(b*self.center[1])
            #-bx+ay+c=0
            if a/b>0:
                c3=(-self.wid//2)*((a**2+b**2)**0.5)-(-b*self.center[0])-(a*self.center[1])
                c4=(self.wid//2)*((a**2+b**2)**0.5)-(-b*self.center[0])-(a*self.center[1])
            else:
                c3=(self.wid//2)*((a**2+b**2)**0.5)-(-b*self.center[0])-(a*self.center[1])
                c4=(-self.wid//2)*((a**2+b**2)**0.5)-(-b*self.center[0])-(a*self.center[1])

            
            self.center[1]=-self.center[1]
            x1=(b*c3-a*c1)/(a**2+b**2)
            x1=gherd(x1)
            y1=((a*x1)+c1)//-b
            x2=(b*c3-a*c2)/(a**2+b**2)
            x2=gherd(x2)
            y2=((a*x2)+c2)//-b
            x3=(b*c4-a*c1)/(a**2+b**2)
            x3=gherd(x3)
            y3=((a*x3)+c1)//-b
            x4=(b*c4-a*c2)/(a**2+b**2)
            x4=gherd(x4)
            y4=((a*x4)+c2)//-b
            z=((x1-x2)**2+(y1-y2)**2)**0.5
            if ((x1-x2)**2+(y1-y2)**2)**0.5<15:
                print(z)
                if a/b<0:
                    x2-=1
                    x4-=1
                    y2-=1
                    y4-=1
                else:
                    x2+=1
                    x4+=1
                    y2-=1
                    y4-=1
            self.m=0
            m=0
            if  world.win.get_at((ghadr(x1),ghadr(y1)))==(255,255,0,255):
                self.m=1
            else:
                m+=1
            if world.win.get_at((ghadr(x2),ghadr(y2)))==(255,255,0,255):
                self.m=1
            else:
                m+=1
            if world.win.get_at((ghadr(x3),ghadr(y3)))==(255,255,0,255):
                self.m=1
            else:
                m+=1
            if world.win.get_at((ghadr(x4),ghadr(y4)))==(255,255,0,255):
                self.m=1
            else:
                m+=1
            if self.m==0 and m>0:
                self.x1=ghadr(x1)
                self.x2=ghadr(x2)
                self.x3=ghadr(x3)
                self.x4=ghadr(x4)
                self.y1=ghadr(y1)
                self.y2=ghadr(y2)
                self.y3=ghadr(y3)
                self.y4=ghadr(y4)
                self.m=0

                
            
            pygame.draw.line(world.win,(0,200,0),(self.x1,self.y1),(self.x3,self.y3),3)
            
            pygame.draw.line(world.win,(0,200,0),(self.x1,self.y1),(self.x2,self.y2),3)
            pygame.draw.line(world.win,(0,200,0),(self.x4,self.y4),(self.x3,self.y3),3)
            pygame.draw.line(world.win,(0,200,0),(self.x2,self.y2),(self.x4,self.y4),3)



            pygame.draw.circle(world.win,(0,200,0),(self.center[0],self.center[1]),self.radium)
            if self.mouse[0]>self.center[0]:
            
                s=ghadr(((a*(self.center[0]+5))+c)//-b)
            
                pygame.draw.line(world.win,(200,0,0),(self.center[0],self.center[1]),(self.center[0]+5,s))
        
            else:
                s=ghadr(((a*(self.center[0]-5))+c)//-b)
            
                pygame.draw.line(world.win,(200,0,0),(self.center[0],self.center[1]),(self.center[0]-5,s))

            pygame.display.update()
        elif a==0 and b!=0:
            self.center[1]=-self.center[1]
            x1=self.center[0]-self.wid//2
            
            x2=self.center[0]-self.wid//2
            x3=self.center[0]+self.wid//2
            x4=self.center[0]+self.wid//2
            y1=self.center[1]-self.wid//2
            y3=self.center[1]-self.wid//2
            y2=self.center[1]+self.wid//2
            y4=y2
            self.m=0
            m=0
            if  world.win.get_at((ghadr(x1),ghadr(y1)))==(255,255,0,255):
                self.m=1
            else:
                m+=1
            if world.win.get_at((ghadr(x2),ghadr(y2)))==(255,255,0,255):
                self.m=1
            else:
                m+=1
            if world.win.get_at((ghadr(x3),ghadr(y3)))==(255,255,0,255):
                self.m=1
            else:
                m+=1
            if world.win.get_at((ghadr(x4),ghadr(y4)))==(255,255,0,255):
                self.m=1
            else:
                m+=1
            if self.m==0 and m>0:
                self.x1=ghadr(x1)
                self.x2=ghadr(x2)
                self.x3=ghadr(x3)
                self.x4=ghadr(x4)
                self.y1=ghadr(y1)
                self.y2=ghadr(y2)
                self.y3=ghadr(y3)
                self.y4=ghadr(y4)
                self.m=0

                
            
            pygame.draw.line(world.win,(0,200,0),(self.x1,self.y1),(self.x3,self.y3),3)
            
            pygame.draw.line(world.win,(0,200,0),(self.x1,self.y1),(self.x2,self.y2),3)
            pygame.draw.line(world.win,(0,200,0),(self.x4,self.y4),(self.x3,self.y3),3)
            pygame.draw.line(world.win,(0,200,0),(self.x2,self.y2),(self.x4,self.y4),3)


            pygame.draw.circle(world.win,(0,200,0),(self.center[0],self.center[1]),self.radium)
            if self.center[1]>self.mouse[1]:
                pygame.draw.line(world.win,(200,0,0),(self.center[0],self.center[1]),(self.center[0],self.center[1]-8))
        
            else:
                pygame.draw.line(world.win,(200,0,0),(self.center[0],self.center[1]),(self.center[0],self.center[1]+8))
            pygame.display.update()
        elif a==0 and b==0:
            pygame.draw.line(world.win,(0,200,0),(self.x1,self.y1),(self.x3,self.y3),3)
            
            pygame.draw.line(world.win,(0,200,0),(self.x1,self.y1),(self.x2,self.y2),3)
            pygame.draw.line(world.win,(0,200,0),(self.x4,self.y4),(self.x3,self.y3),3)
            pygame.draw.line(world.win,(0,200,0),(self.x2,self.y2),(self.x4,self.y4),3)


            pygame.draw.circle(world.win,(0,200,0),(ghadr(self.center[0]),ghadr(self.center[1])),self.radium)
            self.center[1]=-self.center[1]
            pygame.display.update()
            
        


            
            
            
            
    def move(self):
        if self.m==0 and w_key==True:
            self.mouse=pygame.mouse.get_pos()
            y=(-self.mouse[1])-(-self.center[1])
            x=self.mouse[0]-self.center[0]
            c=self.center[0]
            if c==self.center[0]:
                if x!=0 and y!=0:
                    m=y/x
                    if self.center[0]<485 and self.center[1]<485 and  self.mouse[0]> self.center[0]:
                        self.center[0]+=1
                        
                        self.center[1]=-(m*self.center[0]+(-self.center[1])-m*c)
                        self.center[0]=int(self.center[0])
                        self.center[1]=int(self.center[1])
                    
            
                    elif self.center[0]>25 and self.center[1]>25 and  self.mouse[0]< self.center[0]:
                        self.center[0]-=1
                        
                        self.center[1]=-(m*self.center[0]+(-self.center[1])-m*c)
                        self.center[0]=int(self.center[0])
                        self.center[1]=int(self.center[1])
                elif x==0:
                    self.counterx=+1
                    if self.counterx%4==0:
                        m=2
                    else:
                        m=0
                    if self.center[1]>self.mouse[1] and self.center[0]>15 and self.center[1]>15: 
                        self.center[1]-=1
                        self.center[1]+=m
                    elif self.center[0]<485 and self.center[1]<485 and self.center[1]<self.mouse[1] :
                        self.center[1]+=1
                        self.center[1]-=m
                elif y==0:
                    self.countery=+1
                    if self.countery%4==0:
                        g=10
                    else:
                        g=0
                    if self.mouse[0]> self.center[0] and self.center[0]<485 and self.center[1]<485:
                        self.center[0]+=1
                        self.center[0]-=g
                    elif self.center[0]>15 and self.center[1]>15 and  self.mouse[0]< self.center[0]:
                        self.center[0]-=1
                        self.center[0]+=g

    def fire(self):
        if self.shovel>0 and pygame.mouse.get_pressed()[0]:
            bullet=Bullet()
            bullet.begin()
            bullet.move()
            #self.shovel-=1
             
            
class Bullet:
    def __init__(self):
        self.x=None
        self.y=None
        self.id=1
        self.store=None
        self.mouse=None
    def begin(self):
        self.mouse=pygame.mouse.get_pos()
        a=(-self.mouse[1])-(-tank.center[1])
        b=self.mouse[0]-tank.center[0]
        c=-(a*self.mouse[0]+b*self.mouse[1])
        if self.mouse[0]>tank.center[0]:
            self.x=tank.center[0]+5
            self.y=ghadr(((a*self.x)+c)//-b)
        elif self.mouse[0]<tank.center[0]:
            self.x=tank.center[0]-5
            self.y=ghadr(((a*self.x)+c)//-b)
        elif self.mouse[0]==tank.center[0]:
            self.x=tank.center[0]
            if self.mouse[1]>tank.center[1]:
                self.y=tank.center[1]+8
            else:
                self.y=tank.center[1]-8
    def move(self):
        self.mouse=pygame.mouse.get_pos()
        a=(-self.mouse[1])-(-self.y)
        b=self.mouse[0]-self.x
        c=-(a*self.x+b*self.y)
        
        if self.mouse[0]>self.x:
            #print(a//b)
            for i in range(400):
                p=a
                #print(self.x+3,self.y)
                #h1=world.win.get_at((self.x+3,ghadr(self.y)))
                #h2=world.win.get_at((self.x-3,ghadr(self.y)))
                #h3=world.win.get_at((self.x,ghadr(self.y+3)))
                #h4=world.win.get_at((self.x,ghadr(self.y-3)))
                #if h1==(255,255,0,255) or h2==(255,255,0,255) or h3==(255,255,0,255) or h4==(255,255,0,255):
                    #a=-b
                   # b=p
                    #c=-(a*self.x+b*self.y)
                #else:
                    #a=a
                    #b=b
                    #c=-(a*self.x+b*self.y)
                    
                    
                world.draw()
                tank.draw()
                if ghadr(a//b)==0:
                    if i%7==0:
                        self.x-=1
                    else:
                        self.x+=1
                elif ghadr(a//b)<=2:
                    if i%4==0:
                        self.x-=1
                    else:
                        self.x+=1
                elif ghadr(a//b)>5:
                    #print('hi')
                    if i%11==0:
                        self.x-=8
                    else:
                        self.x+=1
                elif ghadr(a//b)>2:
                    
                    if i%5==0:
                        self.x-=3
                    else:
                        self.x+=1
                self.y=ghadr(((a*self.x)+c)//-b)
                pygame.draw.circle(world.win,(255,0,0),(self.x,self.y),3)
                pygame.display.update()
        elif self.mouse[0]<self.x:
            for i in range(400):
                world.draw()
                tank.draw()
                if ghadr(a//b)==0:
                    if i%7==0:
                        self.x+=1
                    else:
                        self.x-=1
                elif ghadr(a//b)<=2:
                    if i%4==0:
                        self.x+=1
                    else:
                        self.x-=1
                elif ghadr(a//b)>2:
                    if i%5==0:
                        self.x+=3
                    else:
                        self.x-=1
                elif ghadr(a//b)>5:
                    if i%200==0:
                        self.x+=199
                    else:
                        self.x-=1
                self.y=((a*self.x)+c)//-b
                pygame.draw.circle(world.win,(255,0,0),(self.x,self.y),3)
                pygame.display.update()        
        elif self.mouse[0]==self.x:
            #print('hi')
            if self.mouse[1]>self.y:
                for i in range(400):
                    world.draw()
                    tank.draw()
                    if i%3==0:
                        self.y-=1
                    else:
                        self.y+=1
                    pygame.draw.circle(world.win,(255,0,0),(self.x,self.y),3)
                    pygame.display.update()        
            else:
                for i in range(400):
                    world.draw()
                    tank.draw()
                    if i%3==0:
                        self.y+=1
                    else:
                        self.y-=1
                    pygame.draw.circle(world.win,(255,0,0),(self.x,self.y),3)
                    pygame.display.update()

        elif self.mouse[1]==self.y:
        
            if self.mouse[0]>self.x:
                for i in range(400):
                    world.draw()
                    tank.draw()
                    if i % 3==0:
                        self.x-=1
                    else:
                        self.x+=1
                    pygame.draw.circle(world.win,(0,255,0),(self.x,self.y),3)
                    pygame.display.update()

            else:
                for i in range(400):
                    world.draw()
                    tank.draw()
                    if i % 3==0:
                        self.x+=1
                    else:
                        self.x-=1
                    
                    pygame.draw.circle(world.win,(0,255,0),(self.x,self.y),3)
                    pygame.display.update()



import sys
def quitgame():
    pygame.quit()
    sys.exit()





world=world()
world.draw()
tank=tank()
tank.draw()
n=0
w_key=False
while True:
    for event in pygame.event.get():
    
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT:
                w_key=True
            elif event.key==pygame.K_ESCAPE:
                quitgame()
        elif event.type==pygame.KEYUP:
            if event.key==pygame.K_RIGHT:
                w_key=False
    n+=1
    if n%150==0:
        world.draw()
    tank.draw()
    tank.fire()
    if n%15==0:
        tank.move()

        
        
    
