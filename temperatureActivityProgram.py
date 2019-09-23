#Based on the temperature input given by the user, the activity is recommended.
print("Enter the temperature");
userInput=int(input());
if(userInput>=85):
   print("Swimming is better for you");
elif(userInput>=70):
   print("Cricket is better for you");
elif(userInput>=32):
   print("Squash is better for you");
elif(userInput>=0):
   print("Sit at home and play board games");
   
else:
    if(userInput<=0):
        print("Sit next to the fireplace, because it's fucking cold");

#***********End of the program"
        
