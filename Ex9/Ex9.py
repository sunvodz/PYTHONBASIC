a = 10

#== , != , < , > , <= , >=

if a < 20:
  print('yes')
else:
  print('no')
  
# order = {'50':'beer','10':'water','20':'lemon'}

# select =  input("Select Order : ")
# if order[select] == 'beer':
#   print('Happy')
# elif order[select] == 'water':
#   print('Happy')
# elif order[select] == 'lemon':
#   print('Happy')

#or
# order = {'50':'beer','10':'water','20':'lemon'}

# select =  input("Select Order : ")
# if order[select] == 'beer' or order[select] == 'water' or order[select] == 'lemon':
#   print('Happy')

#and
b = 10
if a == 10 and b == 20:
  print('Happy')
else:
  print("Sad")
  
  
point = int(input("Enter your point : "))
if point >= 80:
  if point >= 100:
    print("Over Limit point is 100");
  else:
    print("Grade A")
elif point >= 75:
  print("Grade B+")
elif point >= 70:
  print("Grade B")
elif point >= 65:
  print("Grade C+")
elif point >= 60:
  print("Grade C")
elif point >= 55:
  print("Grade D+")
elif point >= 50:
  print("Grade D")
else:
  if point < 0:
    print("Please Enter number more 0")
  else:
    print("Grade F")
  
  
  


