#Let 's write a program to test what my name is
answer = 'anudeep';
print("Guess my name?");
response = input();
if (response == answer):
  print("You have guessed it right");
 
else:
  print("Try one more time");
  response = input();
  if (response == answer):
  print("You have guesses it right");
  else:
  print("You have last chance to guess it right");
  response = input();
  if (response == answer):
  print("You have guessed it right");
  else :
  print("Your out of chances to guess my name. My name is:" + answer);
# ** ** ** ** ** ** ** ** ** ** * End of of the Program ** ** ** ** ** 