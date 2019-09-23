#list Comprehensions

set=[1,7,8,9];
en=0;
en= [x for x in set if x%2==0];
print(en);
print(">>>>>>>>>>>>>>>>>>>>>>>>>");

#List Comprehension another example


RandomNumbers=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20];
oddnumbers=[x for x in RandomNumbers if x%3==0];
print(oddnumbers);
print(">>>>>>>>>>>>>>>>>>>>>>>>>");

names=["ANUDEEP", "SAI", "SRIKANTH", "RAVI"];
names=[word.lower() for word in names];
print(names);




    


    

