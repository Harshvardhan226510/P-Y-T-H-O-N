import random

question=input('Question: ')

luck =random.randint(0,8)

if luck == 0:
  ans='Yes - definitely'
elif luck == 1:
  ans='It is decidedly so'
elif luck == 2:
  ans='Without a doubt'
elif luck == 3:
  ans='Reply hazy, try again'
elif luck == 4:
  ans='Ask again later'
elif luck == 5:
  ans='Better not tell you now '
elif luck == 6:
  ans='My sources say no'
elif luck == 7:
  ans='Outlook not so good'
elif luck == 8:
  ans='Very Doubtfull'
else:
  ans='Better luck next time'                 

print('Magic 8 Ball :' + ans)
