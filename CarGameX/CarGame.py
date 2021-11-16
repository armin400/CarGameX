import pygame, sys
pygame.init() #kasutab pygame võimalusi
from pygame.locals import* #impordik kõik moodulid
import random #panen vastasautod suvaliselt peale sõitma
import math #selleks, et tuvastada kokkupõrget ja autode vahesid
import time #Selleks, et anda alguse aeg valmistuda
screen = pygame.display.set_mode((798,800)) #ekraani suurus

#lisame pygame mixeri häälte ja muusika jaoks
pygame.mixer.init()
#muudan pealkirja screeni menüül
pygame.display.set_caption('Car Game X')

#logo pildi muutmine
logo = pygame.image.load('logo1.jpeg')
pygame.display.set_icon(logo)


############ PEAMENÜÜ ###########
IntroFont = pygame.font.Font("freesansbold.ttf", 38)
def introImg(x,y):
    intro = pygame.image.load("intro.png")
    
    screen.blit(intro,(x,y))
def instructionIMG(x,y):
    instruct = pygame.image.load("instruction.png")
    run = True
    while run:
        screen.blit(instruct,(x,y))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
                        

def aboutIMG(x,y):
    aboutimg = pygame.image.load("About.png")
    run = True
    while run:
        screen.blit(aboutimg,(x,y))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False    
                
def play(x,y):
    playtext = IntroFont.render("Mäng",True,(255,0,0))
    screen.blit (playtext,(x,y))
def ABOUT(x,y):
    aboutText = IntroFont.render("Info",True,(255,0,0))
    screen.blit (aboutText,(x,y))
def Instruction(x,y):
    instructionText = IntroFont.render("Instruktsioon",True,(255,0,0))
    screen.blit(instructionText,(x,y))


def introscreen():
    run = True
    pygame.mixer.music.load('knightrider.mp3')
    pygame.mixer.music.play()
    while run :
        screen.fill((0,0,0))
        introImg(0,0)
        play(100,450)
        Instruction(290,450)
        ABOUT(640,450)

        ####### leiame hiire asukoha vastavalt clickile #######
        x,y = pygame.mouse.get_pos()

        ###### clickitavad nupud
        button1 = pygame.Rect(60,440,175,50)
        button2 = pygame.Rect(265,440,300,50)
        button3 = pygame.Rect(600,440,165,50)

        ##### kastide reageerimine hiire juureshoidmisel######
        ###### arvestab argumentidega, muudab kasti värvi #####
        pygame.draw.rect(screen, (0,0,255), button1,6)
        pygame.draw.rect(screen, (0,0,255), button2,6)
        pygame.draw.rect(screen,(0,0,255),button3,6)

        #### kui vajutada Mängi nuppu
        if button1.collidepoint(x,y):
        ### kasti aktiivseks muuutine, punane äär
            pygame.draw.rect(screen, (155,0,0), button1,6)
        #### Mäng algab, kui vajutada Mängi nuppu
            if click:
                countdown() ## algab countdown, mille järgselt algab mäng


        #### kui hiir on nupu 2 peal (instruktsioon)
        if button2.collidepoint(x,y):
        ### kasti aktiivseks muuutine, punane äär
            pygame.draw.rect(screen, (155,0,0), button2,6)
        #### kui vajutada peale instruktsiooni nupule
            if click:
                instructionIMG(0,0)### näitab instruktsioonimenüüd

        
        #### kui hiir nupu 3 peal(info)
        if button3.collidepoint(x,y):
        ### kasti aktiivseks muuutine, punane äär
            pygame.draw.rect(screen,(155,0,0),button3,6)
        #### kui vajutada peale info nupule ####
            if click:
                aboutIMG(0,0) ### näitab info menüüd
                
        ###### kontrollime hiireklicki asukohta (kinnipanek)
        click = False
        for event in pygame.event.get():
         if event.type == pygame.QUIT:
            run = False
         if event.type == pygame.MOUSEBUTTONDOWN:
             if event.button == 1:
                 click = True
        pygame.display.update()

#Countdowni loopi valmistamine
def countdown():
    font2 = pygame.font.Font('freesansbold.ttf', 85)
    countdownBacground = pygame.image.load('bg.png')
    three = font2.render('3',True, (187,30,16))
    two =   font2.render('2',True, (255,255,0))
    one =   font2.render('1',True, (51,165,50))
    go =    font2.render('GO!!!',True, (0,255,0))
    
    ##### countdowni tühi taust #####
    screen.blit(countdownBacground, (0,0))
    pygame.display.update()

        ###### Numberi näitamine (3) ######
    screen.blit(three,(350,250))
    pygame.display.update()
    time.sleep(0.5)
    ##### läbipaistev taust 3 #####
    screen.blit(countdownBacground, (0,0))
    pygame.display.update()
    time.sleep(0.5)

        ###### Numberi näitamine (2) ######
    screen.blit(two,(350,250))
    pygame.display.update()
    time.sleep(0.5)
    ##### läbipaistev taust 2 #####
    screen.blit(countdownBacground, (0,0))
    pygame.display.update()
    time.sleep(0.5)

        ###### Numberi näitamine (1) ######
    screen.blit(one,(350,250))
    pygame.display.update()
    time.sleep(0.5)
    ##### läbipaistev taust 1 #####
    screen.blit(countdownBacground, (0,0))
    pygame.display.update()
    time.sleep(0.5)

        ###### Näitamine  Go!!! ######
    screen.blit(go,(300,250))
    pygame.display.update()
    time.sleep(0.5)
    gameloop() #Gameloopi näitamine, sest siit hakkab mäng
    pygame.display.update()

    
    
#Programmi käik
def gameloop():
    
    ####### Muusika ####### 
    pygame.mixer.music.load('BackgroundMusic.mp3')
    pygame.mixer.music.play()
    ###### Kokkupõrke hääl ######
    crash_sound = pygame.mixer.Sound('car_crash.wav')
    
    #Score näitamine
    score_value = 0
    font1= pygame.font.Font("freesansbold.ttf",25)
    
    def show_score(x,y):
        score = font1.render("SCORE: "+ str(score_value), True, (255,0,0))
        screen.blit(score, (x,y))
        
    #Highscore osa
    with open ("highscore.txt","r") as f: #tegin mängukausta tekst faili, mängu sees näitan seda ainult lugemiseks ja muutmiseks
            highscore = f.read()
    def show_highscore(x,y):
        Hiscore_text = font1.render('HighScore: ' + str(highscore),True,(255,0,0))
        screen.blit (Hiscore_text,(x,y))
        pygame.display.update()
    
    ###### Mäng läbi osa #######

    def gameover(x,y):
        gameoverImg = pygame.image.load("gameover.png")
        run = True
        while run:

            screen.blit(gameoverImg,(x,y))
            time.sleep(0.5)
            show_score(330,600)
            time.sleep(0.5)
            show_highscore(330,650)
            pygame.display.update()
            
            for event in pygame.event.get():
             if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()
             if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    countdown()
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
    
                  
    #tasutapildi lisamine
    bg = pygame.image.load('bg.png')
    
    
    # oma auto lisamine
    maincar = pygame.image.load('car.png')
    maincarX = 250
    maincarY = 695
    maincarX_change = 0
    maincarY_change = 0
    
    #Teiste autode lisamine
    car1 = pygame.image.load('car1.jpeg')
    car1X = random.randint(178,490)
    car1Y = 0
    car1Ychange = 10
    
    car2 = pygame.image.load('car2.png')
    car2X = random.randint(178,490)
    car2Y = 0
    car2Ychange = 10
    
    car3 = pygame.image.load('car3.png')
    car3X = random.randint(178,490)
    car3Y = 0
    car3Ychange = 10
   
   
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.KEYDOWN: #mis juhtub, kui vajutada järgnevaid nuppe ALLa
                if event.key == pygame.K_RIGHT:
                    maincarX_change += 5
            
                if event.key == pygame.K_LEFT:
                    maincarX_change -= 5
                
                if event.key == pygame.K_UP:
                    maincarY_change -= 5
                    
                if event.key == pygame.K_DOWN:
                    maincarY_change += 5
                    
                    #mis juhtub, kui nuppu lahti lasta
            if event.type == pygame.KEYUP: 
                if event.key == pygame.K_RIGHT:
                    maincarX_change = 0
            
                if event.key == pygame.K_LEFT:
                    maincarX_change = 0
                
                if event.key == pygame.K_UP:
                    maincarY_change = 0
                    
                if event.key == pygame.K_DOWN:
                    maincarY_change = 0
                   
                #Panen paika tee piirid
        if maincarX < 178:
            maincarX = 178
        if maincarX > 490:
            maincarX = 490
        
        if maincarY < 0:
            maincarY = 0
        if maincarY > 690:
            maincarY = 690


        #tausta värvi muutmine
        screen.fill((0,0,0))

        #näitan taustapilti
        screen.blit(bg,(0,0))
        

        #põhiauto näitamine
        screen.blit(maincar,(maincarX,maincarY))
        
        #Teiste autode näitamine / PART2, liikuma panemine suvalisest kohast
        screen.blit(car1,(car1X,car1Y))
        screen.blit(car2,(car2X,car2Y))
        screen.blit(car3,(car3X,car3Y))
        #show score näitamine
        show_score (600,100)
        #näita highscore
        show_highscore (600,50)
        
        
        #Põhiauto liikuma panek
        maincarX += maincarX_change
        maincarY += maincarY_change
        
        #Vastaste liikumine
        car1Y += car1Ychange
        car2Y += car2Ychange
        car3Y += car3Ychange
        
        #vastaste lõpmatu liikumine(kui läbivad alumise punkti satuvad nad ülesse tagasi
        if car1Y > 670:
            car1Y = -100
            car1X = random.randint(178,490)
            score_value += 1
            
        if car2Y > 670:
            car2Y = -150
            car2X = random.randint(178,490)
            score_value += 1
            
        if car3Y > 670:
            car3Y = -200
            car2X = random.randint(178,490)
            score_value += 1
            
        #kontroll, kas tekkis uus Highscore
        if score_value > int(highscore):
            highscore = score_value
        
        #KOKKUPÕRGETE event

        #määran vahe kõigi kolme auto ja põhiauto vahel (kui lähedal peab olema, et tekiks kokkupõrge)
        
        #Peaauto ja auto1
        def iscollision(car1X,car1Y,maincarX,maincarY):
            distance = math.sqrt(math.pow(car1X-maincarX,2) + math.pow(car1Y - maincarY,2)) 

            #kontroll kas vahe on väiksem kui 50

            if distance < 50: 
                return True
            else:
                return False

        #peaauto ja auto2
        def iscollision(car2X,car2Y,maincarX,maincarY):
            distance = math.sqrt(math.pow(car2X-maincarX,2) + math.pow(car2Y - maincarY,2))

            #kontroll kas vahe on väiksem kui 50
            if distance < 50:
                return True
            else:
                return False

        #peaaauto ja auto3
        def iscollision(car3X,car3Y,maincarX,maincarY):
            distance = math.sqrt(math.pow(car3X-maincarX,2) + math.pow(car3Y - maincarY,2))

            #kontroll kas vahe on väiksem kui 50
            if distance < 50:
                return True
            else:
                return False
        
        #annan kokkupõrkele väärtuse

        #avariituvastamine peaauto ja auto1
        coll1 = iscollision(car1X,car1Y,maincarX,maincarY) 

        #avariituvastamine peaauto ja auto2
        coll2 = iscollision(car2X,car2Y,maincarX,maincarY) 

        #avariituvastamine peaauto ja auto3
        coll3 = iscollision(car3X,car3Y,maincarX,maincarY) 

        #kui tekib kokkupõrge (peaauto ja auto1)
        if coll1: 
            
            car1Ychange = 0
            car2Ychange = 0
            car3Ychange = 0
            car1Y = 0
            car2Y = 0
            car3Y = 0
            maincarX_change = 0
            maincarY_change = 0
            pygame.mixer.music.stop() #peale avariid muusika lõppeb ja tekib crash hääl
            crash_sound.play()
            
            ###### Mäng läbi #######
            time.sleep(1)
            gameover(0,0)
        
        #kui tekib kokkupõrge (peaauto ja auto2)
        if coll2:
            
            car1Ychange = 0
            car2Ychange = 0
            car3Ychange = 0
            car1Y = 0
            car2Y = 0
            car3Y = 0
            maincarX_change = 0
            maincarY_change = 0
            pygame.mixer.music.stop() #peale avariid muusika lõppeb ja tekib crash hääl
            crash_sound.play()
            
            ###### Mäng läbi #######
            time.sleep(1)
            gameover(0,0)

        #kui tekib kokkupõrge (peaauto ja auto3) 
        if coll3:
            
            car1Ychange = 0
            car2Ychange = 0
            car3Ychange = 0
            car1Y = 0
            car2Y = 0
            car3Y = 0
            maincarX_change = 0
            maincarY_change = 0
            pygame.mixer.music.stop() #peale avariid muusika lõppeb ja tekib crash hääl
            crash_sound.play()
            
            ###### Mäng läbi #######
            time.sleep(1)
            gameover(0,0)
            
            if car1Ychange == 0 and car2Ychange == 0 and car3Ychange == 0 :
              pass
        
        
            with open ("highscore.txt","w") as f:
                File = open("highscore.txt", w)
                f.write(str(highscore))
                File.close()
            
        #ALATI uuenda pilti
        pygame.display.update()       
introscreen()