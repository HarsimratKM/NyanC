#Author's Name: Excelia Dewi and Harshimrat Kaur
#Last Modified By: Excelia Dewi and Harshimrat Kaur
#Date Last Modified: 5 August 2013
""" 
  Program Description: this is a side scroller mini games, the main character is the famous nyan cat. 
                       user has control of nyan cat up and down by using mouse. nyan cat purpose is to 
                       save nyan baloon.
                       the game has 3 different level easy, medium and hard.
                       in the easy level nyan cat have to avoid small asteroid. In medium level 
                       nyan cat has to avoid combination of small and big asteroid and for the hard level
                       nyan cat has to avoid small, big asteroid and tac nyan (Nyan cat number one enemy).
                        
  Version 2.0 - *     medium level has been completed. lives sprites have been added the function is
                      it will gain lives 1 point everytime user can collect it. enemies added, now there
                      are small and huge asteroids.
                      Still has problem with start and end screen also the background music.
    """
    
import pygame, random, sys
pygame.init()

#set the dimensions of the game screen
screen = pygame.display.set_mode((600, 280))

#create Nyan Cat sprite (the main character)
class NyanCat(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("nyan-rainbow.gif")
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        
        if not pygame.mixer:
            print("Problem with sound")
        else:
            #initialize sounds effect for the game
            pygame.mixer.init()
            self.sndGain = pygame.mixer.Sound("gain.ogg") #sounds when collide with nyan balloon
            self.sndHit = pygame.mixer.Sound("hit.ogg") #sounds when collide with Tac Nyan
            self.sndNyan = pygame.mixer.Sound("nyan_sound.ogg") #background music
            #self.sndNyan.play(-1) #make the background music iterate through the game
        
    def update(self):
        #make Nyan Cat movement cannot exceed the top and the bottom of the screen
        mousex, mousey = pygame.mouse.get_pos()
        if mousey > 265:
            mousey = 265   
        if mousey < 15:
            mousey = 15
        self.rect.center = (38, mousey)

#creating the background sprites that looping through the game, 
#give an illusion that nyan cat moving forward
class Space(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("space.gif")
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        self.dx = 20
        self.reset()
        
    def update(self):
        self.rect.right -= self.dx
        if self.rect.right == screen.get_width():
            self.reset() 
    
    def reset(self):
        self.rect.left = 0
        
#create Tac Nyan sprite        
class TacNyan(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("tac-nyan.gif")
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        self.reset()

    def update(self):
        self.rect.centerx -= self.dx
        self.rect.centery -= self.dy
        if self.rect.right < -1:
            self.reset()
    
    def reset(self):
        self.rect.left = 600
        self.rect.centery = random.randrange(0, screen.get_width())
        self.dy = random.randrange(1, 2)
        self.dx = random.randrange(10, 12)
        
#create small Asteroid sprites      
class SmallAsteroid(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("small-asteroid.gif")
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        self.reset()

    def update(self):
        self.rect.centerx -= self.dx
        self.rect.centery -= self.dy
        if self.rect.right < -1:
            self.reset()
    
    def reset(self):
        self.rect.left = 600
        self.rect.centery = random.randrange(0, screen.get_width())
        self.dy = random.randrange(1, 2)
        self.dx = random.randrange(10, 12)
        
        
class HugeAsteroid(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("huge-asteroid.gif")
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        self.reset()

    def update(self):
        self.rect.centerx -= self.dx
        self.rect.centery -= self.dy
        if self.rect.right < -1:
            self.reset()
    
    def reset(self):
        self.rect.left = 600
        self.rect.centery = random.randrange(0, screen.get_width())
        self.dy = random.randrange(1, 2)
        self.dx = random.randrange(10, 12)
        
        
class Lives(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("lives.gif")
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        self.reset()
        
        self.dx = 10
        
    def update(self):
        self.rect.right -= self.dx;
        if self.rect.right < -1:
            self.reset()
            
    def reset(self):
        self.rect.left = 600
        self.rect.centery = random.randrange(0, screen.get_height())


#create Nyan Balloon sprite
class NyanBaloon(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("nyan-baloon.gif")
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        self.reset()
        
        self.dx = 10
        
    def update(self):
        self.rect.right -= self.dx;
        if self.rect.right < -1:
            self.reset()
            
    def reset(self):
        self.rect.left = 600
        self.rect.centery = random.randrange(0, screen.get_height())
        
#creates the simple score system      
class Scoreboard(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.lives = 5
        self.score = 0
        self.font = pygame.font.SysFont("Lucida Console", 20)
        
    def update(self):
        self.text = "Nyan: %d | Score: %d" % (self.lives, self.score)
        self.image = self.font.render(self.text, 1, (255, 177, 0))
        self.rect = self.image.get_rect()
        self.rect.right = 600
 
#handling the game event        
def gameEasy():
    pygame.display.set_caption("Nyan Cat - Saving Nyan Balloon") #set caption
    background = pygame.Surface(screen.get_size())
    background.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    
    #create variable to contain sprite
    nyan = NyanCat()
    baloon = NyanBaloon()
    space = Space()
    asteroid1 = SmallAsteroid()
    asteroid2= SmallAsteroid()
    asteroid3 = SmallAsteroid()
    scoreboard = Scoreboard()

    
    #handle multiple sprites and the order each sprites get update
    friendSprites = pygame.sprite.OrderedUpdates(space, baloon, nyan)
    
    #create multiple Tac Nyan sprites
    enemySprites = pygame.sprite.Group(asteroid1,asteroid2,asteroid3)

    
    #sprites for scoring
    scoreSprites = pygame.sprite.Group(scoreboard)
    
    clock = pygame.time.Clock()
    keepGoing = True
    while keepGoing:
        clock.tick(30)
        pygame.mouse.set_visible(False)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
                
        #check collisions
        if nyan.rect.colliderect(baloon.rect):
            nyan.sndGain.play()
            baloon.reset()
            scoreboard.score += 100

        #check the lives value and if nyan cat hit tac nyan his lives decrease
        hitEnemies = pygame.sprite.spritecollide(nyan, enemySprites, False)
        if hitEnemies:
            nyan.sndHit.play()
            scoreboard.lives -= 1
            if scoreboard.lives <= 0:
                keepGoing = False
            for theEnemy in hitEnemies:
                theEnemy.reset()
            
                
                
        friendSprites.update()
        enemySprites.update()
        scoreSprites.update()
        
        friendSprites.draw(screen)
        enemySprites.draw(screen)
        scoreSprites.draw(screen)
            
        pygame.display.flip()
    
    nyan.sndNyan.stop()
    
    #return mouse cursor
    pygame.mouse.set_visible(True) 
    return scoreboard.score

def gameMedium():
    pygame.display.set_caption("Nyan Cat - Saving Nyan Balloon") #set caption
    background = pygame.Surface(screen.get_size())
    background.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    
    #create variable to contain sprite
    nyan = NyanCat()
    baloon = NyanBaloon()
    space = Space()
    asteroid1 = SmallAsteroid()
    asteroid2= SmallAsteroid()
    asteroid3 = SmallAsteroid()
    bigAsteroid1 = HugeAsteroid()
    bigAsteroid2 = HugeAsteroid()
    bigAsteroid3 = HugeAsteroid()
    lives = Lives()
    scoreboard = Scoreboard()

    
    #handle multiple sprites and the order each sprites get update
    friendSprites = pygame.sprite.OrderedUpdates(space, baloon, lives, nyan)
    
    #create multiple Tac Nyan sprites
    enemySprites = pygame.sprite.Group(asteroid1,asteroid2,asteroid3, bigAsteroid1, bigAsteroid2, bigAsteroid3)

    
    #sprites for scoring
    scoreSprites = pygame.sprite.Group(scoreboard)
    
    clock = pygame.time.Clock()
    keepGoing = True
    while keepGoing:
        clock.tick(30)
        pygame.mouse.set_visible(False)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
                
        #check collisions
        if nyan.rect.colliderect(lives.rect):
            nyan.sndGain.play()
            lives.reset()
            scoreboard.lives += 1
        
        #check collisions
        if nyan.rect.colliderect(baloon.rect):
            nyan.sndGain.play()
            baloon.reset()
            scoreboard.score += 100

        #check the lives value and if nyan cat hit tac nyan his lives decrease
        hitEnemies = pygame.sprite.spritecollide(nyan, enemySprites, False)
        if hitEnemies:
            nyan.sndHit.play()
            scoreboard.lives -= 1
            if scoreboard.lives <= 0:
                keepGoing = False
            for theEnemy in hitEnemies:
                theEnemy.reset()
            
                
                
        friendSprites.update()
        enemySprites.update()
        scoreSprites.update()
        
        friendSprites.draw(screen)
        enemySprites.draw(screen)
        scoreSprites.draw(screen)
            
        pygame.display.flip()
    
    nyan.sndNyan.stop()
    
    #return mouse cursor
    pygame.mouse.set_visible(True) 
    return scoreboard.score

def instructions():
    pygame.display.set_caption("Nyan Cat - Saving Nyan Balloon")

    nyan = NyanCat()
    space = Space()
    
    #create instructions and prints all the words in the screen
    allSprites = pygame.sprite.Group(space, nyan)
    insFont = pygame.font.SysFont(None, 25)
    insLabels = []
    instructions = (
    "You are the fabulous Nyan Cat,",
    "saving Nyan Baloon in outer space.",
    "Fly towards the nyan balloon to save him and gain score!",    
    "avoid the enemies to stay alive",
    "Steer with the mouse.",
    "press 1 for easy",
    "2 for medium", 
    "3 for hard level",
    "escape to quit..."
    )
    
    for line in instructions:
        tempLabel = insFont.render(line, 1, (255, 177, 0))
        insLabels.append(tempLabel)
 
    #handle if the user want to continue the game by clicking the mouse or just simply want to quit 
    keepGoing = True
    clock = pygame.time.Clock()
    pygame.mouse.set_visible(False)
    while keepGoing:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
                donePlaying = True
            elif event.type == pygame.KEYDOWN:
                 if event.key == pygame.K_ESCAPE:
                    keepGoing = False
                    donePlaying = True
                 if event.key == pygame.K_1:
                    gameEasy()
                 if event.key == pygame.K_2:
                     gameMedium()
    
        allSprites.update()
        allSprites.draw(screen)

        for i in range(len(insLabels)):
            screen.blit(insLabels[i], (80, 30*i))

        pygame.display.flip()
        
    nyan.sndNyan.stop()    
    pygame.mouse.set_visible(True)
    return donePlaying


def end(score):
    pygame.display.set_caption("Nyan Cat - Saving Nyan Balloon")

    nyan = NyanCat()
    space = Space()
    
    #create instructions and prints all the words in the screen
    allSprites = pygame.sprite.Group(space, nyan)
    insFont = pygame.font.SysFont(None, 25)
    insLabels = []
    instructions = (
    "Nyan Cat.     Last score: %d" % score ,
    "Game is over  ",
    "Do you wish to play again?",
    "click to start, escape to quit..."
    )
    
    for line in instructions:
        tempLabel = insFont.render(line, 1, (255, 177, 0))
        insLabels.append(tempLabel)
 
    #handle if the user want to continue the game by clicking the mouse or just simply want to quit 
    keepGoing = True
    clock = pygame.time.Clock()
    pygame.mouse.set_visible(False)
    while keepGoing:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
                donePlaying = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                keepGoing = False
                donePlaying = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    keepGoing = False
                    donePlaying = True
    
        allSprites.update()
        allSprites.draw(screen)

        for i in range(len(insLabels)):
            screen.blit(insLabels[i], (80, 30*i))

        pygame.display.flip()
        
    nyan.sndNyan.stop()    
    pygame.mouse.set_visible(True)
    return donePlaying


def main():
    #checking if the user want to keep playing or quit the game 
    donePlaying = False

    score = 0
    while not donePlaying:
        
        donePlaying = instructions()
        score = gameEasy()
        donePlaying = end(score)
        
        
            


if __name__ == "__main__":
    main()