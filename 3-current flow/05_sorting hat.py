gryffindor=0
ravenclaw=0
hufflepuff=0
slytherin=0

print('Q1) Do you like dawn or dusk')
print('1) Dawn')
print('2) Dusk')

ans=int(input('Enter 1-2\n'))

if ans == 1:
  gryffindor += 1
  ravenclaw += 1

elif ans == 2:
  hufflepuff += 1
  slytherin +=1

else:
  print('Wrong input')

print('Q2) When I am dead, I want people to remember me as: ')
print('1) The Good ')
print('2) The Great ')
print('3) The Wise ')
print('4) The Bold ')

ans=int(input('Enter 1-4\n'))

if ans == 1:
  hufflepuff +=2

elif ans == 2:
  slytherin +=2

elif ans == 3:
  ravenclaw +=2

elif ans == 4:
  gryffindor +=2

else:
  print('Wrong input')

print('Q3) Which kind of instrument most pleases your ear? ')
print('1) The violin')
print('2) The trumpet')
print('3) The piano')
print('4) The drum')

ans=int(input('Enter 1-4\n'))

if ans == 1:
  slytherin +=4

elif ans == 2:
  hufflepuff +=4

elif ans == 3:
  ravenclaw +=4

elif ans == 4:
  gryffindor +=4

else:
  print('Wrong input')  

print('Gryffindor :',gryffindor)
print('Ravenclaw :',ravenclaw)
print('Hufflepuff :',hufflepuff)
print('Slytherin :',slytherin)
