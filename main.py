import turtle
import random

print("Hello to the turtle Race Progeam!")

print("Do you want to modify the Appearence? or Direclty play the game?")
choice_1 = str(input("Enter M to modify, and D to directlty play: "))
choice_1 = choice_1.upper().strip()
if choice_1 == "M":
      print("Background Colour: ")
      print("Enter any colour or Hex value; For default white direclty press enter: ")
      choice_bgcolour = input()


      print("Enter colour of first player; For default colour green directly press enter: ")
      choice_color_p1 = input()

      print("Enter colour of second player; For default colour, blue directly press enter: ")
      choice_color_p2 = input()

      print("Enter shape of first player: Available options:  arrow, circle, turtle, square, classic, triangle, snake etc. For Default turtle directly press enter: ")
      choice_shape_p1 = input()

      print("Enter shape of second player: Available options: arrow, turtle, circle, square, triangle, classic, snake. For Default turtle directly press enter: ")
      choice_shape_p2 = input()

      

      if choice_bgcolour == "":
            turtle.bgcolor("white")
      else:
            turtle.bgcolor(choice_bgcolour)

      
      p1 = turtle.Turtle()
      if choice_color_p1 == "":
            p1.color("green")
      else:
            p1.color(choice_color_p1)

      
      p2 = turtle.Turtle()
      if choice_color_p2 == "":
            p2.color("blue")
      else:
            p2.color(choice_color_p2)

      
      if choice_shape_p1 == "":
            p1.shape("turtle")

      elif choice_shape_p1 == "snake":
            turtle.register_shape('snake_1.gif')
            p1.shape('snake_1.gif')
      else: 
            p1.shape(choice_shape_p1)

      
      
      if choice_color_p2 == "":
            p2.shape("turtle")
      elif choice_shape_p1 == "snake":
            turtle.register_shape('snake_1.gif')
            p2.shape('snake_1.gif')
      else:
            p2.shape(choice_shape_p2)

pn1 = str (input('Please enter name of Player 1: '))
pn1 = pn1.capitalize().strip()

pn2  = str (input('Please enter name of Player 2: '))
pn2 = pn2.capitalize().strip()



if choice_1 == "D":
      p1 = turtle.Turtle()
      p1.shape('turtle')
      p1.color('green')
p1.speed(2)

#Starting position for player 1      
p1.penup()
p1.goto(-200,100)


if choice_1 == "D":
      p2 = turtle.Turtle()
      p2.color('blue')
      p2.shape('turtle')
p2.speed(3)
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


die = [1,2,3,4,5,6] # 
result = ""

running = True
while running:
      if p1.pos() >= (160,20):  # pos() / position()
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
            print()
            if result == "pn1":
                  running = False
                  break

            p2_turn = input('Press "Enter" to roll the die')
            die_outcome3 = random.choice(die)
            print("The result of the die is : ",die_outcome3)
            die_outcome4 = die_outcome3 * 20
            print("The number of the steps will be", die_outcome4)
            p2.fd(die_outcome4)
            print()
            if result == "pn2":
                  running = False
                  break
turtle.mainloop()
