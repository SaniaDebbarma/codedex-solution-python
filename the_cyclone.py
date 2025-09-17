# hunger = 11
# anger = 3
# if hunger > 4 and anger > 1:
#   print('Hangry')
# else:
#   print('angry')


height = int(input('What is your height (cm)? '))
credits = int(input('How many credits do you have? '))

if height >= 137 and credits >= 10:
  print('Enjoy the ride')
elif credits < 10 and height >= 137:
  print("You don't have enough credits to ride.")
elif height <= 137 and credits >=10:
  print("You are not tall enough to ride.")
else:
  print("You are not tall enough for this ride, nor do you have enough credits.")
