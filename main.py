import turtle
import random

print("Welcome to the turtle Race Program!")

print("Do you want to modify the Appearence? or Direclty play the game?")
choice_1 = str (input("Enter M to modify, and D to directlty play: "))
choice_1 = choice_1.upper().strip()
if choice_1 == "M":
      print("Background Colour: \n")
      choice_bgcolour = input("Enter any colour or Hex value; For default white direclty press enter: \n")
      choice_color_p1 = input("Enter colour of first player; For default colour green directly press enter: \n")
      choice_color_p2 = input("Enter colour of second player; For default colour, blue directly press enter: \n")
      choice_shape_p1 = input("Enter shape of first player: Available options:  arrow, circle, turtle, square, classic, triangle, snake etc. For Default turtle directly press enter: \n")
      choice_shape_p2 = input("Enter shape of second player: Available options: arrow, turtle, circle, square, triangle, classic, snake. For Default turtle directly press enter: \n")

      choice_shape_p1 = choice_shape_p1.lower().strip()
      choice_shape_p2 = choice_shape_p2.lower().strip()
      
      if choice_bgcolour == "":
            turtle.bgcolor("white")
      else:
            turtle.bgcolor(choice_bgcolour)

      p1 = turtle.Turtle()
      if choice_color_p1 == "":
            p1.color("green")
      else:
            p1.color(choice_color_p1)

      if choice_shape_p1 == "":
            p1.shape("turtle")

      elif choice_shape_p1 == "snake":
            p1.shape('snake.gif')
      else: 
            p1.shape(choice_shape_p1)

      
      p2 = turtle.Turtle()
      if choice_color_p2 == "":
            p2.color("blue")
      else:
            p2.color(choice_color_p2)

      
      if choice_color_p2 == "":
            p2.shape("turtle")
      elif choice_shape_p2 == "snake":
            p2.shape('snake.gif')
      else:
            p2.shape(choice_shape_p2)
      
      

turtle.addshape('snake.gif')
game_over = turtle.Turtle()
game_over.hideturtle()

#Player Names
pn1 = str (input('Please enter name of Player 1: '))
pn1 = pn1.capitalize().strip()

pn2  = str (input('Please enter name of Player 2: '))
pn2 = pn2.capitalize().strip()



#Starting position for player 1      
p1.penup()
p1.goto(-200,100)

#If Not modifies and directly played:
if choice_1 == "D":
      p1 = turtle.Turtle()
      p1.shape('turtle')
      p1.color('green')
      p2 = turtle.Turtle()
      p2.color('blue')
      p2.shape('turtle')
p1.speed(1)
p2.speed(1)

      
#Starting position for player 2
p2.penup()
p2.goto(-200,-100)

# Making goal circle
p1.goto(200,60)
p1.pendown()
p1.circle(40)

# Bringing the player back.
p1.penup()
p1.rt(180)
p1.goto(-200,100)
p1.rt(180)

# Making goal circle
p2.goto(200,-140)

p2.pendown()
p2.circle(40)
p2.rt(180)

# Bringing the player back.
p2.penup()
p2.goto(-200,-100)
p2.rt(180)

go = turtle.Turtle()
go.hideturtle()


die = [1,2,3,4,5,6]
result = ""

#Mainloop of program:
running = True
while running:
      if p1.pos() >= (160,20): 
            print(pn1,"wins! ")
            result = "pn1"
            break
      elif p2.pos() >= (160,-200):
            print(pn2,"wins! ")
            result = "pn2"
            break
      else:
            p1_turn = input('Press "Enter" to roll the die')
            die_outcome1 = random.choice(die)
            print("The result of the die is :",die_outcome1)
            die_outcome2 = die_outcome1 * 20
            print("The number of the steps will be", die_outcome2)
            p1.fd(die_outcome2)
            if result == "pn1":
                  running = False # running becomes false and therefore while loop will end.
                  break # precautionary break just in case.

            p2_turn = input('Press "Enter" to roll the die')
            die_outcome3 = random.choice(die)
            print("The result of the die is : ",die_outcome3)
            die_outcome4 = die_outcome3 * 20
            print("The number of the steps will be", die_outcome4)
            p2.fd(die_outcome4)
            
            if result == "pn2":
                  game_over.write("GAME OVER", font=("Verdana", 15, "normal"))
                  running = False # running becomes false and therefore while loop will end.
                  break # precautionary break just in case.
turtle.mainloop()
