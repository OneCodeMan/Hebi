#Hebi.py
import pygame
import time
import random

pygame.init()

#colors
white = (255,255,255)
#lights
dodgerblue = (30,144,255)
normal_blue = (0,0,215)
active_blue = (30,144,255)
normal_red = (215,0,0)
active_red = (240,128,128)
normal_pink = (255,192,203)
active_pink = (255,182,193)

#fruit colors
crimson = (220,20,60)
powderblue = (176,224,230)
hotpink = (255,105,180)
yellow = (255,255,0)
black = (0,0,0)
orange = (255,102,0)
darkorchid = (153,50,204)
lime = (0,255,0)
green = (0,128,0)

#snake colors
snake_blue = (0,191,255)
snake_pink = (255,20,147)
snake_violet = (255,0,255)
snake_red = (250,128,114)
snake_green = (0,250,154)

screen_width = 700
screen_height = 500

FPS = 30

position = pygame.mouse.get_pos()
click = pygame.mouse.get_pressed()


def text(message,color,location,size,window):
    '''Function used to draw text on screen'''
    introfont = pygame.font.SysFont(None, size)
    sentence = introfont.render(message,True,color)
    window.blit(sentence, location)


def intro():

    introRunning = True

    while introRunning:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        position = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()


        intro = pygame.display.set_mode((screen_width,screen_height))
        pygame.display.set_caption('Hebi')
        intro.fill(white)

        fruit_colors = [crimson,powderblue,yellow,hotpink,orange,darkorchid,lime,black]
        fruit_text = ["10 pts", "20 pts", "30 pts", "50 pts", "70 pts", "90 pts",
                      "100 pts", "Poison"]
            
        vertical = 90
        for i in range(len(fruit_colors)):
            pygame.draw.rect(intro,fruit_colors[i],(350,vertical,20,20))
            vertical += 40

        vertical = 90
        for i in range(len(fruit_text)):
            text(fruit_text[i],black,[380,vertical],30,intro)
            vertical += 40


        text("Hebi",green,[310,20],50,intro)
        text("Made by Dave Gumba",black,[285,60],20,intro)

        if 170 > position[0] > 40 and 150 > position[1] > 60:
            pygame.draw.rect(intro,active_blue,(40,90,130,60))
            text("Play",black,[80,110],30,intro)
            if click[0]==1:
                introRunning = False
                intro2()
        else:
            pygame.draw.rect(intro,normal_blue,(40,90,130,60))
            text("Play",black,[80,110],30,intro)

        if 170 > position[0] > 40 and 260 > position[1] > 200:
            pygame.draw.rect(intro,active_red,(40,200,130,60))
            text("Quit",black,[80,220],30,intro)
            if click[0]==1:
                pygame.quit()
                quit()
        elif introRunning == False:
            intro2()
        else:
            pygame.draw.rect(intro,normal_red,(40,200,130,60))
            text("Quit",black,[80,220],30,intro)
        
            
        pygame.display.update()


def intro2():

    intro2Running = True

    while intro2Running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        position = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
    
        intro2 = pygame.display.set_mode((screen_width,screen_height))
        pygame.display.set_caption('Hebi')
        intro2.fill(white)
        text("Choose Your Snake",green,[130,20],50,intro2)
        text("Are You A",black,[130,90],90,intro2)

        if 185 > position[0] > 125 and 210 > position[1] > 150:
            pygame.draw.rect(intro2,active_blue,(125,150,60,60))
            text("Boy",black,[130,240],30,intro2)
            text("Or",black,[260,180],30,intro2)
            text("Girl",black,[380,240],30,intro2)
            if click[0] == 1:
                intro2Running = False
                intro3()
        elif intro2Running == False:
             intro3()
        else:
            pygame.draw.rect(intro2,normal_blue,(125,150,60,60))
            text("Boy",black,[130,240],30,intro2)
            text("Or",black,[260,180],30,intro2)
            text("Girl",black,[380,240],30,intro2)

        if 430 > position[0] > 370 and 210 > position[1] > 150:
            pygame.draw.rect(intro2,active_pink,(370,150,60,60))
            text("Boy",black,[130,240],30,intro2)
            text("Or",black,[260,180],30,intro2)
            text("Girl",black,[380,240],30,intro2)
            if click[0]==1:
                intro2Running = False
                intro3()
                pygame.display.update()
        elif intro2Running == False:
            intro3()
        else:
            pygame.draw.rect(intro2,normal_pink,(370,150,60,60))
            text("Boy",black,[130,240],30,intro2)
            text("Or",black,[260,180],30,intro2)
            text("Girl",black,[380,240],30,intro2)

        pygame.display.update()

def intro3():

    intro3Running = True

    while intro3Running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        position = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
    
        intro3 = pygame.display.set_mode((screen_width,screen_height))
        pygame.display.set_caption('Hebi')
        intro3.fill(white)
        text("Just kidding!",black,[130,20],50,intro3)
        text("Color preference does not depend on your gender!",black,[100,70],30,intro3)
        text("Now choose your snake :)",black,[100,100],30,intro3)

        snake_colors = [snake_blue,snake_pink,snake_violet,snake_red,snake_green]

        horizontal = 120
        for i in range(len(snake_colors)):
            pygame.draw.rect(intro3,snake_colors[i],(horizontal,200,20,20))
            horizontal += 90


        if 140 > position[0] > 119 and 220 > position[1] > 200:
            if click[0] == 1:
                snake_color = snake_blue
                game_loop(snake_blue)
                
        elif 230 > position[0] > 210 and 220 > position[1] > 200:
            if click[0] == 1:
                snake_color = snake_pink
                game_loop(snake_pink)

        elif 320 > position[0] > 300 and 220 > position[1] > 200:
            if click[0] == 1:
                snake_color = snake_violet
                game_loop(snake_violet)

        elif 410 > position[0] > 390 and 220 > position[1] > 200:
            if click[0] == 1:
                snake_color = snake_red
                game_loop(snake_red)
                
        elif 500 > position[0] > 480 and 220 > position[1] > 200:
            if click[0] == 1:
                snake_color = snake_green
                game_loop(snake_green)       
        

        pygame.display.update()

def loss(snake_color):

    lost = True

    while lost:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        position = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        
        loserScreen = pygame.display.set_mode((screen_width,screen_height))
        pygame.display.set_caption('Hebi')
        loserScreen.fill(white)
        text("Game Over! Hope you had fun!", black, [100,250],50,loserScreen)

        if 230 > position[0] > 100 and 430 > position[1] > 300:
            pygame.draw.rect(loserScreen,active_blue,(100,300,130,60))
            if click[0] == 1:
                 game_loop(snake_color)
        else:
            pygame.draw.rect(loserScreen,normal_blue,(100,300,130,60))

        if 430 > position[0] > 300 and 360 > position[1] > 300:
            pygame.draw.rect(loserScreen,active_red,(300,300,130,60))
            if click[0] == 1:
                pygame.quit()
                quit()
        else:
            pygame.draw.rect(loserScreen,normal_red,(300,300,130,60))    

        text("Play again",black,[110,320],30,loserScreen)
        text("Quit",black,[330,320],30,loserScreen)
        pygame.display.update()


def fruit_generator():
    '''Generates fruit of a random color'''
    fruit_colors = [crimson,crimson,crimson,
                    crimson,crimson,crimson,crimson,crimson,crimson,crimson,
                    crimson,powderblue,powderblue,powderblue,powderblue,
                    powderblue,powderblue,powderblue,powderblue,powderblue,
                    yellow,yellow,yellow,yellow,yellow,yellow,
                    yellow,hotpink,hotpink,hotpink,
                    hotpink,orange,orange,orange,darkorchid,darkorchid,lime]
    x = random.randint(0,36)
    return fruit_colors[x]  

def game_loop(snake_color):
    
    gameScreen = pygame.display.set_mode((screen_width,screen_height))
    pygame.display.set_caption("Hebi")

    score = 0
    
    Exit = False
    Over = False

    x_pos = 350
    y_pos = 250
    delta_x = 0
    delta_y = 0
    snakeList = []
    snakeLength = 1
    randcolor = fruit_generator()

    AppleX = round(random.randrange(0, screen_width-10)/10.0)*10.0
    AppleY = round(random.randrange(0, screen_height-10)/10.0)*10.0

    # Poison
    PoisonX = round(random.randrange(0, screen_width-10)/10.0)*10.0
    PoisonY = round(random.randrange(0, screen_height-10)/10.0)*10.0
    

    clock = pygame.time.Clock()
    size = 10


    while not Exit:

        while Over == True:
            loss(snake_color)
            pygame.display.update()
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Exit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                   delta_x -= 10
                   delta_y = 0
                elif event.key == pygame.K_RIGHT:
                    delta_x += 10
                    delta_y = 0
                elif event.key == pygame.K_UP:
                    delta_y -= 10
                    delta_x = 0
                elif event.key == pygame.K_DOWN:
                    delta_y += 10
                    delta_x = 0

        if x_pos > 700 or x_pos < 0 or  y_pos > 500 or y_pos < 0 or (x_pos == PoisonX and y_pos == PoisonY):
            Over = True
        
            
        x_pos += delta_x
        y_pos += delta_y
        gameScreen.fill(white)
        text("Score: "+str(score),black,[0,5],30,gameScreen)
        text("Double tap to speed up!", black, [0,40], 20, gameScreen)
        pygame.draw.rect(gameScreen,randcolor,[AppleX,AppleY,size,size])
        pygame.draw.rect(gameScreen,black,[PoisonX,PoisonY,size,size])

        snakeHead = []
        snakeHead.append(x_pos)
        snakeHead.append(y_pos)
        snakeList.append(snakeHead)

        #Statement to make the snake not extend infinitely long
        if len(snakeList) > snakeLength:
            del snakeList[0]
            
        #Ends the game if the snake 'runs' into itself
        for i in snakeList[:-1]:
            if i == snakeHead:
                Over = True

        
        for XnY in snakeList:
            pygame.draw.rect(gameScreen,snake_color,[XnY[0],XnY[1],size,size])
        
        
        pygame.display.update()


        if x_pos == AppleX and y_pos == AppleY:
            if randcolor == crimson:
                score += 10
            elif randcolor == powderblue:
                score += 20
            elif randcolor == yellow:
                score += 30
            elif randcolor == hotpink:
                score += 50
            elif randcolor == orange:
                score += 70
            elif randcolor == darkorchid:
                score += 90
            elif randcolor == lime:
                score += 100
            
            randcolor = fruit_generator()
            AppleX = round(random.randrange(0, screen_width-10)/10.0)*10.0
            AppleY = round(random.randrange(0, screen_height-10)/10.0)*10.0
            pygame.draw.rect(gameScreen,randcolor,[AppleX,AppleY,size,size])

            # Poison
            PoisonX = round(random.randrange(0, screen_width-10)/10.0)*10.0
            PoisonY = round(random.randrange(0, screen_height-10)/10.0)*10.0
            
            snakeLength +=1

        pygame.display.update()
             

        clock.tick(FPS)

    pygame.quit()
    quit()

    
intro()
