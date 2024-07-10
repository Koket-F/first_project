import pygame
import math
import sys

pygame.init()
width, height = 800, 800
yellow = (255, 255, 0)
White= (255,255,255)
v = int(input('initial velocity'))
Theta =int(input('angle'))
Font = pygame.font.SysFont('comicsans',16)
Blue =(100,149,237)
win = pygame.display.set_mode((width, height))
pygame.display.set_caption('projectile_motion')
HEIGHT=[]

class Object:
    g = 9.80665  # Positive, since we subtract it in the update
    SCALE = 1  # Adjust the scale for visualization
    TIMESTEP = 1 / 60  # Time step in seconds

    def __init__(self, theta, x, y, radius, color, v):
        self.x = x
        self.y = y
        self.v = v
       
        self.theta = math.radians(Theta)
        self.vy = math.sin(self.theta) * v
        self.vx = math.cos(self.theta) * v
        self.radius = radius
        self.color = color
        self.path = []
        

    def draw(self, win):
        x = self.x * self.SCALE + width / 2
        y = height - (self.y * self.SCALE + height / 2)  # Invert y for correct drawing
        if len(self.path) > 2:
            updated_points = []
            
            for points in self.path:
                px, py = points
                px = px * self.SCALE + width / 2
                py = height - (py * self.SCALE + height / 2)  # Invert y for correct drawing
                updated_points.append((px, py))
                
                text2 = Font.render('range',1,White)
                win.blit(text2,(300,413))
            
            pygame.draw.lines(win, self.color, False, updated_points, 2)
        pygame.draw.circle(win, self.color, (int(x), int(y)), self.radius)
        if len(self.path) > 2:
            range = []
            for points in self.path:
                px, py = points
                px = px * self.SCALE + width / 2
                py = height - (py * self.SCALE + height / 2)  # Invert y for correct drawing
                range.append((px,410))
            pygame.draw.lines(win,Blue,False,range,2)
            
        
        
    
    

    def update_position(self):
        self.vy -= self.g * self.TIMESTEP
        
        self.x += self.vx * self.TIMESTEP
        self.y += self.vy * self.TIMESTEP
        if self.y>0 and Theta>0:
         self.path.append((self.x, self.y))
        elif Theta==0:
         self.vy=0
         self.path.append((self.x,self.y))
        
        
         
         
        
        
        else:
            self.vx=0
            self.vy=0
            
            
        
    
         

ball = Object(Theta, -390, 0, 10, yellow, v)
def main():
    run = True
    clock = pygame.time.Clock()
      # 45 degrees for initial angle
    
    while run:
        clock.tick(60)
        win.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        ball.update_position()
        ball.draw(win)
        
        pygame.draw.line(win, White, (0, 400), (800, 400), 2)
        pygame.display.update()
    pygame.quit()
    sys.exit()

main()
 