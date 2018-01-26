
import pygame
import pygame.event
import pygame.locals

from  pygame import*

pygame.init()
n=0
class world:
    def __init__(self,x=500,y=500):
        self.wid=x
        self.hei=y
        self.win=None


    def draw(self):
        import pygame
        pygame.init()
        self.win=pygame.display.set_mode((self.wid,self.hei))
        #self.win.fill(255,255,255)
        pygame.draw.line(self.win,(200,200,0),(0,0),(self.wid,0),10)
        pygame.draw.line(self.win,(200,200,0),(0,0),(0,self.hei),10)
        pygame.draw.line(self.win,(200,200,0),(self.wid,0),(self.wid,self.hei),10)
        pygame.draw.line(self.win,(200,200,0),(0,self.hei),(self.wid,self.hei),10)
        pygame.display.update()
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
    #import pygame.local
    
    def __init__(self):

        self.w_key=False
        self.speed=0
        self.counter=0
        self.m=None
        self.color=(200,0,0)
        self.wid=20
        self.center=[15+self.wid//2,15+self.wid//2]
        self.radium=5
        self.mouse=pygame.mouse.get_pos()
        #pygame.draw.rect(world.win,(200,200,0),(50,50,10,10))
    def draw(self):
        #world.draw()
        self.mouse=pygame.mouse.get_pos()
        self.center[1]=-self.center[1]
        w=-self.mouse[1]
        b=self.center[1]-w
        a=self.center[0]-self.mouse[0]
        if a!=0 and b==0:
            self.center[1]=-self.center[1]
            x1=self.center[0]-self.wid//2
            
            x2=x1
            x3=self.center[0]+self.wid//2
            x4=x3
            y1=self.center[1]-self.wid//2
            y3=y1
            y2=self.center[1]+self.wid//2
            y4=y2
            
            #if world.win.get_at((x1,y1))==(200,200,0,255):
                #n=1
            #elif world.win.get_at((x2,y2))==(200,200,0,255):
                #n=1
            #elif world.win.get_at((x3,y3))==(200,200,0,255):
                #n=1
            #elif world.win.get_at((x4,y4))==(200,200,0,255):
                #n=1

                
                
            
            pygame.draw.line(world.win,(0,200,0),(x1,-y1),(x3,-y3),3)
            
            pygame.draw.line(world.win,(0,200,0),(x1,-y1),(x2,-y2),3)
            pygame.draw.line(world.win,(0,200,0),(x4,-y4),(x3,-y3),3)
            pygame.draw.line(world.win,(0,200,0),(x2,-y2),(x4,-y4),3)



            pygame.draw.circle(world.win,(0,200,0),(self.center[0],self.center[1]),self.radium)
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
            #print(z)
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
            
            
            #if world.win.get_at((int(x1),int(y1)))==(200,200,0,255):
               # n=1
            #elif world.win.get_at((x2,y2))==(200,200,0,255):
                #n=1
            #elif world.win.get_at((x3,y3))==(200,200,0,255):
                #n=1
            #elif world.win.get_at((x4,y4))==(200,200,0,255):
               # n=1
                
                
            
            pygame.draw.line(world.win,(0,200,0),(x1,-y1),(x3,-y3),3)
            
            pygame.draw.line(world.win,(0,200,0),(x1,-y1),(x2,-y2),3)
            pygame.draw.line(world.win,(0,200,0),(x4,-y4),(x3,-y3),3)
            pygame.draw.line(world.win,(0,200,0),(x2,-y2),(x4,-y4),3)



            pygame.draw.circle(world.win,(0,200,0),(self.center[0],self.center[1]),self.radium)
            s=((a*(self.center[0]+5))+c)//-b
            s=-s
            #pygame.draw.line(world.win,(200,0,0),(self.center[0],self.center[1]),(self.center[0]+5,s))
        
        


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

            
            #if world.win.get_at((x1,y1))==(200,200,0,255):
                #n=1
            #elif world.win.get_at((x2,y2))==(200,200,0,255):
                #n=1
            #elif world.win.get_at((x3,y3))==(200,200,0,255):
                #n=1
            #elif world.win.get_at((x4,y4))==(200,200,0,255):
                #n=1

                
            
            pygame.draw.line(world.win,(0,200,0),(x1,-y1),(x3,-y3),3)
            
            pygame.draw.line(world.win,(0,200,0),(x1,-y1),(x2,-y2),3)
            pygame.draw.line(world.win,(0,200,0),(x4,-y4),(x3,-y3),3)
            pygame.draw.line(world.win,(0,200,0),(x2,-y2),(x4,-y4),3)


            pygame.draw.circle(world.win,(0,200,0),(self.center[0],self.center[1]),self.radium)
            #pygame.draw.line(world.win,(200,0,0),(self.center[0],self.center[1]),(self.center[0],self.center[1]+8))
        
        


            pygame.display.update()


            #pygame.draw.line(world.win,(200,0,0),(self.center[0],self.center[1]),(self.center[0]+8,self.center[1]))
        
        


            
            
            
            
    def move(self):
        self.counter+=1
        if self.counter%10==0:
            self.speed=0
        else:
            self.speed=0
        
        if self.w_key==True:
            #print('hi')
        
            self.mouse=pygame.mouse.get_pos()
            y=(-self.mouse[1])-(-self.center[1])
            x=self.mouse[0]-self.center[0]
            c=self.center[0]
            if x!=0 and y!=0:
                m=y/x
                #c=self.center[0]
                #y=mx+(-self.center[1])-msef.center[0]
                if self.mouse[0]> self.center[0]:
                    self.center[0]+=1
                    self.center[0]-=self.speed
                    self.center[1]=-(m*self.center[0]+(-self.center[1])-m*c)
                    self.center[0]=int(self.center[0])
                    self.center[1]=int(self.center[1])
                
        
                else:
                    self.center[0]-=1
                    self.center[0]+=self.speed
                    self.center[1]=-(m*self.center[0]+(-self.center[1])-m*c)
                    self.center[0]=int(self.center[0])
                    self.center[1]=int(self.center[1])
            
world=world()
world.draw()
tank=tank()
tank.draw()
n=0
speed=0
w_key=False
        

while True:

    for event in pygame.event.get():
    
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT:
                tank.w_key=True
        elif event.type==pygame.KEYUP:
            if event.key==pygame.K_RIGHT:
                tank.w_key=False
    n+=1
    #if len(pygame.event.get())>0:
        #if pygame.event.get()[len(pygame.event.get())-1].type==pygame.KEYDOWN:
            #tank.w_key=True
    if n%150==0:
        world.draw()
    tank.draw()
    if n%15==0:
        tank.move()


        
        


while True:
    #print(pygame.mouse.get_pos())
    n+=1
    if n%4==0:
        speed=2
    else:
        speed=0
    for event in pygame.event.get():
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT:
                rightkey=True
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_RIGHT:
                rightkey=False
    move()
    win.fill((0,0,0))
    pygame.draw.circle(win,(100,0,0),(wid,hei),30)
    pygame.display.update()
        
        
    
