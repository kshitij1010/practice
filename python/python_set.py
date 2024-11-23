
print ("\n############### Set ###############")
print ("Information:")
print ("- Sets can't contain duplicates")
print ("- Sets are unordered")
print ("- In order to find an element in a set, a hash lookup is used (which is why sets are unordered).")
print ("  This makes __contains__ (in operator) a lot more efficient for sets than lists.")
print ("- Sets can only contain hashable items (see #3). If you try: set(([1],[2])) you'll get a TypeError.")
print ("- In practical applications,")
print ("  lists are very nice to sort and have order")
print ("  while sets are nice to use when you don't want duplicates and don't care about order.")
print ("\n\n\n\n")

set1 = {2, 4, 2, 7, 8}
set2 = {1, 5, 3, 8, 0}
print ("set1:", set1)
print ("set2:", set2)

print ("\n############### Size / Length of the Set ## ( len(set1) ): ", len(set1))

print ("\n############### Adding / Removing ##")
set1.add(-7)
set1.add(-25)
print ("--->    ( set.add(n) ): add n in the set , here adding -7 and -25 ( set1.add(-7) ):", set1)
set1.remove(-7)
print ("--->    ( set.remove(n) ): remove -7 from the set ( set1.remove(-7) ):", set1)



print ("\n############### Union of two sets ##: ( set1 | set2 )", ( set1 | set2 ))

print ("\n############### Common elements from the two sets ##")
print ("--->    ( setlist1.intersection(setlist2) OR setlist1.intersection(setlist2) ): ( set1.intersection(set2) )", set1.intersection(set2))
print ("--->    ( setlist1 & setlist2 ): using set ( set1 & set2 )", set1 & set2)

print ("\n############### Set diff ##")
print ("set1:", set1)
print ("set2:", set2)
print ("--->    ( set1 - set2 ): returns the set of elements of set1 which is not in set2):", set1 - set2)
print ("--->    ( set1 ^ set2 ): returns the set of elements of which are not common:", set1 ^ set2)
