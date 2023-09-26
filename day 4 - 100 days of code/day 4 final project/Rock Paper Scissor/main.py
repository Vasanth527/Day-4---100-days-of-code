rock ='''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random
#Write your code below this line 👇

your_choice = int(input("what do you choose? type 0 for rock, 1 for paper or 2 for scissor\n"))

if your_choice >= 3 or your_choice < 0 :
  print("you entered a wrong number, you loose")

else:

  if your_choice == 0:
    print('''    
      _______
  ---'   ____)
        (_____)
        (_____)
        (____)
  ---.__(___)''')
  if your_choice == 1:
    print('''
      _______
  ---'   ____)____
            ______)
            _______)
           _______)
  ---.__________)''')
      
  if your_choice == 2:
    print('''    
      _______
  ---'   ____)____
            ______)
         __________)
        (____)
  ---.__(___)''')
      
  
  computer_choice = [0, 1, 2]
  choosing = random.choice(computer_choice)
  print("\ncomputer choose:\n")
  
  if choosing == 0:
    print('''    
      _______
  ---'   ____)
        (_____)
        (_____)
        (____)
  ---.__(___)''')
  if choosing == 1:
    print('''
      _______
  ---'   ____)____
            ______)
            _______)
           _______)
  ---.__________)''')
      
  if choosing == 2:
    print('''    
      _______
  ---'   ____)____
            ______)
         __________)
        (____)
  ---.__(___)''')
  
  
  if your_choice == 0 and choosing ==1 :
    print("\nYou loose")
    
  elif your_choice == 1 and choosing == 2 :
    print("\nYou loose")
    
  elif your_choice == 2 and choosing == 0:
    print("\nYou loose")
  elif your_choice == choosing :
    print("\nDraw") 
  else :
    print ("\nYou won")
    

    
       
     




