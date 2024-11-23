print ("\n############### List Manipulation ###############")
l = [2, 4, 2, 7, 8]
print ("Orig List:")
print (l)

print ("\n############### Size / Length of the List ## ( len(list) ): ", len(l))

print ("\n############### Adding ##")
print ("--->    ( .append(n) ): add at the last of the list(adding 1,23,112,1,11) ( l.append(1) )")
l.append(1)
l.append(23)
l.append(112)
l.append(1)
l.append(11)
print (l)

print ("--->    ( .insert(a,b) ): add b at the a positon ( l.insert(2,77) )")
l.insert(2, 77)
print (l)

print ("\n############### Updating ##")
print ("--->    ( list[nth]=new_val ): updating the nth element with new_value ( l[7] = 25 ), updated value 23 to be 25")
l[7] = 25
print ("\nNow list is ::        ", l)

print ("\n############### Removing ##")
print ("--->    ( .remove(n) ): remove by the value, first occurance will be remove if multiple ( l.remove(1) )")
l.remove(1)
print (l)
print ("--->    ( del l[index] or del[start:end] ): deleting element by postion, will remove the value 4 ( del l[1] )")
del l[1]
print (l)
print ("--->    ( list.pop() ): consider list as a stack: remove the last element ( l.pop() )", l.pop())
print ("--->    ( list.pop(n) ): consider list as a stack: remove the element at index n( l.pop(6) )", l.pop(6))
print ("\nNow list is ::        ", l)

print ("\n############### Reading the element/ getting the index ##")
print ("--->    ( .index(n) ): checking index of 77 ( l.index(77) ): ", l.index(77))
print ("--->    ( l[n] ): value at nth index ( l[4] ): ", l[4], " __ ( l[-2] ): ", l[-2])

print ("\n############### slice ##")
print ("--->    ( list[start:end] ): sliced (start to end, end(th) elem will not be included) ( l[1:4] ): ", l[1:4])
print ("--->    ( list[:end] ): from 0th index to end ( l[:3] ): ", l[:3])
print ("--->    ( list[start:] ): from start to the last element ( l[3:] ): ", l[3:])
print ("--->    ( list[start:end:step] ): from start to the end every step's elem ( l[1:7:2] ): ", l[1:7:2])
print ("--->    ( list[::step] ): every second item starting from 0th index ( l[::2] ): ", l[::2])


print ("\n############### reversing the list ## ( l[::-1] )")
l22 = l[:]
l22.reverse()
print ("--->    ( l[::-1] ): reverse the list permanently ( l22.reverse) : ", l22)
print ("--->    ( l[::-1] ): temp reverse ( l[::-1] ): ", l)

print ("\nNow list is ::        ", l)

print ("\n############### counting the occurance of element ## .count(n)")
print ("1 is", l.count(1), "times in the list!!", "112 is", l.count(112), "times in the list!!", "2 is", l.count(2), "times in the list!!")

print ("\n############### sorting ##")
l3 = l.copy() # or list(l)
l3.sort()
print ("--->    ( .sort() ): sorting in ascending order ( l3.sort() ): ", l3)
l3.sort(reverse=True)
print ("--->    ( .sort() ): sorting in descending order ( l3.sort(reverse=True) ) ", l3)
print ("--->    ( sorted(list) ): temp sorting ascending ( sorted(l) ): ", sorted(l))
print ("--->    ( sorted(list) ): temp sorting descending ( sorted(l, reverse=True) ): ", sorted(l, reverse=True))

print ("\n############### Min/Max value in the List & sum of all values ##")
print ("--->    ( min(list) ): Min of the list: ", min(l))
print ("--->    ( max(list) ): Max of the list:", max(l))
print ("--->    ( sum(list) ): Sum of all the values in list:", sum(l))

print ("\nNow list is :: ", l)

print ("\n############### copying ##")
l11 = list(l)
print ("--->    ( l11 = list(l) ): ", l11)
l12 = l.copy()
print ("--->    ( l12 = l.copy() ): ", l12)
l13 = l[:]
print ("--->    ( l13 = l[:] ): ", l13)
l14 = l[2:5]
print ("--->    ( l14 = l[2:5] ) Copying sliced elem only : ", l14)

print ("\n############### the list with multiple data types ##")
l4 = [1, "abcd", "hey", 999999, 288.33, 'a', 77]
print ("--->    list of mixed datatype: ", l4)

print ("\n############### Common elements from the two lists (converting to set ( new_set = set(list) )) ##")
lset = set(l)
l4set = set(l4)
print ("--->    ( setlist1.intersection(setlist2) OR setlist1.intersection(setlist2) ): ( lset.intersection(l4set) )", lset.intersection(l4set))
print ("--->    ( setlist1 & setlist2 ): using set ( lset & l4set )", lset & l4set)
print ("Note: in both the method set will be returned so \"list(lset & l4set)\" or list(lset.intersection(l4set)) will give you the list")

print ("\n############### Adding/Merge two lists ##")
l5 = l + l4
print ("--->    new list: ", l5)
