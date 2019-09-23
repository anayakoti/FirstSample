#Let us write a complex iterator function to print the points
print("Here is how the tradition way of looping through the elements :");
print("");


Square=((25, 46), (12, 34,), (93, 94), (23, 27));
for iterator in Square:
    print(iterator);
print(">>>>>>>>>>>>>>>>>>>>");
#Lets use the next() to print all the values inside a complex tuple.
print("Here is how the tradition way of looping through the elements using iter() and next() :");
print("");

useAndThrow=iter(Square);
print(next(useAndThrow));
print(next(useAndThrow));
print(next(useAndThrow));
print(next(useAndThrow));



