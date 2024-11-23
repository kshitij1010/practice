print ("\n############### Tuple ###############")
print ("Information:")
print ("- A tuple is like a list, except you can't change the values in a tuple once it's defined.")
print ("- Therefore, Tuples are immutable.")
print ("- Tuples are good for storing information that shouldn't be changed throughout the life of a program. ")
print ("Note: You can overwrite an entire tuple, but you can't change the individual elements in a tuple")
print ("\n\n\n\n")


days = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")


print ("\n############### __Days_Tuple__ printing tuple ##")
print (days)

print ("\n############### printing nth elem ##")
print ("first day (days[0]): ", days[0], " _______________ last day (days[6]):", days[6])


print ("\n\n\n\n")
a = (1000, 2000, 3000)
print ("\n############### __Numbers_Tuple__ ( a = (1000, 2000, 3000) ) printing a ##")
print (a)

print ("overwriting an entire tuple \"a\"")
a = (1111, 2222, 3333)
print ("\n############### overwritten tuple ( a = (1111, 2222, 3333) ) printing a ##")
print (a)


# A tuple consists of a number of values separated by commas. They are useful for ordered pairs and returning several
# values from a function.
# creation: emptyTuple = ()
#           singleItemTuple = (“spam”,)
#           thistuple = 12, 89, ‘a’
#           thistuple = (12, 89, ‘a’)
# accessing:
#           thistuple[0] (output: 12)
