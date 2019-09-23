#In this Program we are printing odd numbers within a range

numbers=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20];
print("In the range  of numbers from 1 to 20 these are the divisible by 3 :");
    

for oddnumbers in range(0,len(numbers),3):
#In the above loop we have the range it must start till the length of numbers
    #pus '3' is add each with 3
    #This will add every number in a list with 3 and print the odd numbers for us
    print(oddnumbers);
print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>");
print("These are the numbers that are divisible by 5 within numbers from 1 to 20 :");
#Lets print all the numbers that are divisible by 5
for fives in range(0,len(numbers),5):
    
    print(fives);
    
    
