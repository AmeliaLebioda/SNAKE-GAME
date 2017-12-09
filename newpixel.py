import pygame
import random

pygame.init()

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,155,0)

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Slither')
snakeheadimage=pygame.image.load('snakehead.png')
appleimage=pygame.image.load('apple2.png')
segment = pygame.image.load('segment.png')
tail = pygame.image.load('tail.png')

clock = pygame.time.Clock()

block_size= 25
FPS =10
direction =  "right"
smallfont = pygame.font.SysFont("comicsansms", 20)
medfont = pygame.font.SysFont("comicsansms", 50)
largefont = pygame.font.SysFont("comicsansms", 70)


def score (score):
    text = smallfont.render ("Score: " +str (score), True, black)
    gameDisplay.blit(text,  [0,0])

def text_objects(text, color, size):
    if size == "small":
        textSurface=smallfont.render(text, True, color)
    elif size == "med":
        textSurface=medfont.render(text, True, color)
    elif size == "large":
        textSurface=largefont.render(text, True, color)
    return textSurface, textSurface.get_rect()

def message_to_screen(msg,color, y_displace=0, size = "small"):
    textSurf, textRect = text_objects(msg, color, size)
    textRect.center = (display_width/2),(display_height/2)+ y_displace
    gameDisplay.blit(textSurf, textRect)


def snake(block_size, snakelist):
    
    if direction =="right":
        head = pygame.transform.rotate(snakeheadimage, 270)

    if direction =="left":
        head = pygame.transform.rotate(snakeheadimage, 90)
    
    if direction =="up":
        head = snakeheadimage

    if direction =="down":
        head = pygame.transform.rotate(snakeheadimage, 180)
    
    gameDisplay.blit(head, (snakelist [-1] [0], snakelist [-1][1]))



    if direction =="right":
        part = pygame.transform.rotate(segment, 270)

    if direction =="left":
        part = pygame.transform.rotate(segment, 90)
    
    if direction =="up":
        part = segment

    if direction =="down":
        part = pygame.transform.rotate(segment, 180)



    if direction =="right":
        endofsnake= pygame.transform.rotate(tail, 270)

    if direction =="left":
        endofsnake = pygame.transform.rotate(tail, 90)
    
    if direction =="up":
        endofsnake = tail

    if direction =="down":
        endofsnake= pygame.transform.rotate(tail, 180)
    
        
    for XnY in snakelist[1:-1]:
        gameDisplay.blit(part, (XnY[0],XnY[1]))
        
   
    gameDisplay.blit(endofsnake, (snakelist [0] [0], snakelist [0][1]))
    #pygame.draw.rect(gameDisplay, green, [XnY[0],XnY[1],block_size,block_size])
    

  
    
    
def start_menu():
    intro =True
    
    while intro:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                    
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
                if event.key == pygame.K_c:
                    intro = False

        

    
        gameDisplay.fill(white)
        message_to_screen("Welcome to Slither" , red, -100,"large")
        message_to_screen("The rules and functionalities are:", black, -20, "small" )
        message_to_screen ( "The snake can move in four directions.",black, 10, "small")
        message_to_screen("When the snake eats food its tail becomes longer." , black, 30, "small")
        message_to_screen("Food appears in random places.", black, 50, "small")
        message_to_screen("The game is over when the snake bites itself." ,black, 70, "small"  )
        message_to_screen("Press C to play or Q to quit", black, 150,"small")
        pygame.display.update()
        clock.tick(10)

         
def gameLoop():
    global direction
    gameExit = False
    gameOver = False

    snakeList =[]
    snakeLenght=3
    
    

    lead_x = display_width/2
    lead_y = display_height/2

 
    
    
    lead_x_change = 10
    lead_y_change = 0

    randAppleX=round (random.randrange(0,display_width-block_size)/10.0)*10.0
    randAppleY=round (random.randrange(0,display_height-block_size)/10.0)*10.0
    
    while not gameExit:
        
        while gameOver == True:
            gameDisplay.fill(white)
            message_to_screen("The game is over",red, -100, size ="large")
            message_to_screen("Press C to play again or Q to quit",black, 50, size = "small")
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameExit==True
                    gameOver==False
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_c:
                        direction = "right"
                        gameLoop()
            
                
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:  
                if event.key == pygame.K_LEFT:
                    direction = "left"
                    lead_x_change = -block_size
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    direction = "right"
                    lead_x_change = block_size
                    lead_y_change = 0
                elif event.key == pygame.K_UP:
                    direction = "up"
                    lead_y_change = -block_size
                    lead_x_change = 0
                elif event.key == pygame.K_DOWN:
                    direction = "down"
                    lead_y_change = block_size
                    lead_x_change = 0
        if lead_x>display_width or lead_x<0 or lead_y>display_height or lead_y<0:
           gameOver = True
                
        lead_x +=  lead_x_change
        lead_y +=  lead_y_change
        gameDisplay.fill(white)
        
        AppleThickness =20
 
        #pygame.draw.rect(gameDisplay, red, [randAppleX,randAppleY,AppleThickness,AppleThickness])
        gameDisplay.blit(appleimage, (randAppleX,randAppleY))
        snakeHead=[]
        #snakeTail = []
    
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        #snakeTail.append(lead_x - block_size)
        #snakeTail.append(lead_y - block_size)
        
        #snakeList.append(snakeTail)
        snakeList.append(snakeHead)
        print (len(snakeList))
        print (snakeList)
        
        
        
        if len(snakeList) > snakeLenght:
            del snakeList[0]

        for eachSegment in snakeList [:-1]:
            if eachSegment == snakeHead:
                gameOver=True
             
        

        
        snake(block_size,snakeList)
        score(snakeLenght - 1)
        pygame.display.update()

        if lead_x>=randAppleX and lead_x<=randAppleX+ AppleThickness:
            if lead_y>=randAppleY and lead_y<=randAppleY+AppleThickness:
               randAppleX=round (random.randrange(0,display_width-block_size)/10.0)*10.0
               randAppleY=round (random.randrange(0,display_height-block_size)/10.0)*10.0
               snakeLenght += 1
               
        
        clock.tick(FPS)


    pygame.quit()
    quit()
start_menu()
gameLoop()



