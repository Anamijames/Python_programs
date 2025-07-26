#Magic 8 ball program
import random

question = input("Question: ")

rand_no = random.randint(1,9)

if rand_no == 1 :
  print('Magic 8 Ball: Yes - definitely.')
elif rand_no == 2 :
  print('Magic 8 Ball: It is decidedly so.')
elif rand_no == 3 :
  print('Magic 8 Ball: Without a doubt.')
elif rand_no == 4 :
  print('Magic 8 Ball: Ask again later.')
elif rand_no == 5 :
  print('Magic 8 Ball: Better not tell you now.')
elif rand_no == 6 :
  print('Magic 8 Ball: My sources say no.')
elif rand_no == 7 :
  print('Magic 8 Ball: Outlook not so good.')
elif rand_no == 8 :
  print('Magic 8 Ball: Very doubtful')
else :
  print('Magic 8 Ball: Reply hazy, try again.')
