#we will now use for loop in a dictionary
#In order to indicate dictionary we use {}
#Dictionary does have key-value pairs.
IT={'Adarsh' : '08RE1A1201', 'Anudeep':'08RE1A1202','Anwesh':'08RE1A1203', 'Chaitanya':'08RE1A1204', 'Gurucharan':'08RE1A1205'};
for key in IT.keys():
    print("The roll number of "+ key +" is"+ ": "+"---> "  + "(" + IT[key] +")");
    
