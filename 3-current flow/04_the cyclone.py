height=int(input('What is your height: '))
credits=int(input('How much credits do you have: '))

if height >= 137 and credits >=10:
  print('Enjoy the ride!')

elif height < 137 and credits >= 10:
  print('You are not tall enough to ride')

elif height >= 137 and credits < 10:
  print('You dont have enough credits')

else:
  print('you dont meet either requirements')
