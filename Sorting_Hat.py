# Write code below 💖
#Sorting Hat problem
g = 0
r = 0
h = 0
s = 0
num1 = int(input("Q1) Do you like Dawn or Dusk?\n 1) Dawn \n 2) Dusk\n"))
if num1 == 1 :
  g += 1
  r += 1
elif num1 == 2 :
  h += 1
  s += 1
else :
  print("Wrong input")

num2 = int(input("Q2) When I'm dead, I want people to remember me as:\n 1) The Good\n 2) The Great\n 3) The Wise\n 4) The Bold \n"))
if num2 == 1 :
  h += 2
elif num2 == 2 :
  s =+ 2
elif num2 == 3 :
  r += 2
elif num2 == 4 :
  g += 2
else :
  print("wrong input")

num3 = int(input("Q3) Which kind of instrument most pleases your ear?\n 1) The violin\n 2) The trumpet\n 3) The piano\n 4) The drum\n"))
if num3 == 1 :
  s += 4
elif num3 == 2 :
  h += 4
elif num3 == 3 :
  r += 4
elif num3 == 4 :
  g += 4
else :
  print("Wrong input")
print("")
print('The score of Gryffindor is ', g)
print('The score of Slytherin is ', s)
print('The score of Ravenclaw is ', r)
print('The score of Hufflepuff is ', h)
print("")
if g > s :
  if g > r :
    if g > h :
      print("Gryffindor wins")
    else :
      print("Hufflepuff wins")
  else :
    if r > h :
      print("Ravenclaw wins")
    else :
      print("Hufflepuff wins")
else :
  if s > r :
    if s > h :
      print("Slytherin wins")
    else :
      print("Hufflepuff wins")
  else:
    if r > h :
      print("Ravenclaw wins")
    else :
      print("Hufflepuff wins")
    