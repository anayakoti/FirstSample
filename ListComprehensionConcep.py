#List Comprehensions
#This is a normal way of doing For Loop
grades=[23,45,66,79];
for i in grades:
    
    print(i+5);
#List comprehension
grades=[grade+5 for grade in grades];
print(grades);

#List comprehension

lister=[20, 30, 45, 66];
lister=[i+2 for i in lister];
print(str(lister));
    
