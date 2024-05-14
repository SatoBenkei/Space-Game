import os
import random
import winsound
import time 
#Import the turtle module 
import turtle
# Required by MacOSX to show the Window
turtle.fd(0)
# Set the animation speed to Maximum
turtle.speed(0)
# Changes the background color
turtle.bgcolor("black")
# Change the title
turtle.title("SpaceWar")
# Change the background 
turtle.bgpic(r"C:\Users\felex\Documents\space_bckgrnd2.gif")
# Hide the default Turtle
turtle.ht()
# This saves memory
turtle.setundobuffer(1)
# This speed up drawing
turtle.tracer(3)

class Sprite(turtle.Turtle):
    def __init__(self, spriteshape, color, startx, starty):
        super().__init__()
        self.shape(spriteshape)
        self.color(color)
        self.penup()
        self.speed()
        self.goto(startx, starty)

    def move(self):
        self.fd(self.speed())
 # Boundary Detection
        if self.xcor() > 290:
            self.setx(290)
            self.lt(60)
            
        if self.xcor() < -290:
            self.setx(-290)
            self.lt(60)

        if self.ycor() > 290:
           self.sety(290)
           self.lt(60)
        
        if self.ycor() < -290:
            self.sety(-290)
            self.lt(60)

    def is_collision(self,other):
        if (self.xcor() >= (other.xcor()-20)) and \
         (self.xcor() <= (other.xcor()+20)) and \
         (self.ycor() >= (other.ycor()-20))and \
         (self.ycor() <= (other.ycor()+20)):
            return True
        else:
            return False
        
class Player(Sprite):
    def __init__(self, spriteshape, color, startx, starty,):
        super().__init__(spriteshape, color, startx, starty)
        self.shapesize(stretch_wid=0.6, stretch_len=1.1, outline=None)
        self.player_speed = 4
    
    def turn_left(self):
        self.lt(35)
    
    def turn_right(self):
        self.rt(35) 

    def accelerate(self):
        self.player_speed += 1 

    def decelerate(self):
        self.player_speed -= 1

    def move(self):
        self.fd(self.player_speed)
         # Boundary Detection
        if self.xcor() > 290:
            self.setx(290)
            self.lt(60)
            
        if self.xcor() < -290:
            self.setx(-290)
            self.lt(60)

        if self.ycor() > 290:
           self.sety(290)
           self.lt(60)
        
        if self.ycor() < -290:
            self.sety(-290)
            self.lt(60)

class Ally(Sprite):
    def __init__(self, spriteshape, color, startx, starty,):
        super().__init__(spriteshape, color, startx, starty)
        self.ally_speed = 8
        self.setheading(random.randint(0,360))

    def move(self):
        self.fd(self.ally_speed)

     # Boundary Detection
        if self.xcor() > 290:
            self.setx(290)
            self.lt(60)
            
        if self.xcor() < -290:
            self.setx(-290)
            self.lt(60)

        if self.ycor() > 290:
           self.sety(290)
           self.lt(60)
        
        if self.ycor() < -290:
            self.sety(-290)
            self.lt(60)
        
class Enemy(Sprite):
    def __init__(self, spriteshape, color, startx, starty,):
        super().__init__(spriteshape, color, startx, starty)
        self.enemy_speed = 6
        self.setheading(random.randint(0,360))
    
    def move(self):
        self.fd(self.enemy_speed)
    # Boundary Detection
        if self.xcor() > 290:
            self.setx(290)
            self.lt(60)
            
        if self.xcor() < -290:
            self.setx(-290)
            self.lt(60)

        if self.ycor() > 290:
           self.sety(290)
           self.lt(60)
        
        if self.ycor() < -290:
            self.sety(-290)
            self.lt(60)

class Missile (Sprite):
    def __init__(self, spriteshape, color, startx, starty,):
        super().__init__(spriteshape, color, startx, starty)
        self.shapesize(stretch_wid=0.2 , stretch_len=1.1, outline=None)
        self.missile_speed =20
        self.status = "ready"
        self.goto(-400, 400)

    def fire(self):
        if self.status =="ready":

            # Play missile sound effect
            laser_canon = r"C:\Users\felex\Downloads\laser_cannon.wav"
            winsound.PlaySound(laser_canon, winsound.SND_ASYNC)

            self.goto(player.xcor(), player.ycor())
            self.setheading(player.heading())
            self.status = "firing"

    def move(self):
        if self.status == "firing":
            self.fd(self.missile_speed)
    
         # Boundary Detection
        if self.xcor() < -290 or self.xcor() > 290 or \
           self.ycor() < -290 or self.ycor() > 290:
            self.goto(-1000, 1000)
            self.status ="ready"
    
class Particle(Sprite):
    def __init__(self, spriteshape, color, startx, starty,):
        super().__init__(spriteshape, color, startx, starty)
        self.shapesize(stretch_wid = 0.1 , stretch_len = 0.1, outline=None)
        self.particle_speed = 13
        self.status = "ready"
        self.frame = 0
    
    def explode(self):
        if self.status == "ready":
            self.goto(enemy.xcor(), enemy.ycor())
            self.setheading(enemy.heading())
            self.status = "firing"
            self.frame = 1


    def move(self):
        if self.status == "firing":
            self.fd(self.particle_speed)
            self.frame += 1

        if self.frame > 10:
            self.fd(self.particle_speed)
            self.goto(-400, 400)
            self.status = "ready"

class Game():
        def __init__(self):
            self.level = 1
            self.score = 0
            self.state = "playing"
            self.pen = turtle.Turtle()
            self.lives = 3

        # Draw border
        def draw_border(self):
            self.pen.speed(0)
            self.pen.color("white")
            self.pen.width(3)
            self.pen.penup()
            self.pen.goto(-300, 300)
            self.pen.pendown()
            for side in range(4):
                self.pen.fd(600)
                self.pen.rt(90)
            self.pen.penup()
            self.pen.ht()
            self.pen.pendown()

        def show_status(self):
            self.pen.undo()
            msg = "Score: %s" %(self.score)
            self.pen.penup()
            self.pen.goto(-300, 300)
            self.pen.write(msg, font=("Arial", 16, "normal"))

    

# Create Game Object
game = Game()

# Draw the game border
game.draw_border()

# Show game status
game.show_status()

# Create game components
player = Player("triangle", "white", 0,0)
# ally = Ally("square", "blue", 0,0)
# enemy = Enemy("circle", "red",0,-100)
missile = Missile("triangle","yellow",0,0)

enemies = []
for i in range (6):
    enemies.append(Enemy ("circle", "red", 0, -100))

allies = []
for i in range (4):
    allies.append(Ally("square", "blue", 0,0))

particles = []
for i in range (20):
    particles.append(Particle ("circle", "orange", 0, 0))

# Keyboard Bindings
turtle.onkey(player.turn_left,"Left")
turtle.onkey(player.turn_right,"Right")
turtle.onkey(player.accelerate,"Up")
turtle.onkey(player.decelerate,"Down")
turtle.onkey(missile.fire, "space")

turtle.listen()




# Main game loop
while True:
    turtle.update()
    time.sleep(0.04)

    player.move()
    missile.move()


    for enemy in enemies:
        enemy.move()
# Check for a collision with player
        if player.is_collision(enemy):
# Play explosion sound
            explosion = r"C:\Users\felex\Downloads\explosion.wav"
            winsound.PlaySound(explosion, winsound.SND_ASYNC)
            x = random.randint(-250, 250)
            y = random.randint(-250, 250)
            enemy.goto(x, y)
            missile.goto(-400, 400)
            game.score -= 100
            game.show_status()
# Explosion debris
            for particle in particles:
                particle.explode()
# Check for a collision between missile and enemy
        if missile.is_collision(enemy):
# Play explosion sound
            explosion = r"C:\Users\felex\Downloads\explosion.wav"
            winsound.PlaySound(explosion, winsound.SND_ASYNC)
            x = random.randint(-250, 250)
            y = random.randint(-250, 250)
            enemy.goto(x, y)
            missile.goto(-400, 400)
            missile.status = "ready"
# Increase the score
            game.score += 100
            game.show_status()
# Explosion debris
            for particle in particles:
                particle.explode()
                
    for ally in allies:
        ally.move()
 # Check for a collision between missile and ally
        if missile.is_collision(ally):
# Play explosion sound
            explosion = r"C:\Users\felex\Downloads\explosion.wav"
            winsound.PlaySound(explosion, winsound.SND_ASYNC)        
            x = random.randint(-250, 250)
            y = random.randint(-250, 250)
            ally.goto(x, y)
            missile.goto(-400, 400)
            missile.status = "ready"
# Decrease the score
            game.score -= 50
            game.show_status()
            for particle in particles:
                particle.explode()
                
    # for particle in particles:
    #     particle.move()

# delay = input("Press enter to finish. > ")
