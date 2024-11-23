print ("\n############### Dictionary ###############")
print ("Information:")
print ("- A dictionary is a set of key:value pairs. it is kind of a hashmap")
print ("- All keys in a dictionary must be unique.")
print ("\n\n\n\n")


d1 = {'a':1, 'b':23, 'c':"eggs"}
print (d1)

print ("\n############### Size / Length of the Dictionary ## ( len(d1) ):\n", len(d1))


print ("\n############### Adding key:value in the dictionary ##")
d1['d'] = "new_addition"
print ("--->    ( d1['d'] ) = \"new_addition\": now the dict is:    ", d1)

d1.update({'e':'e'})
print ("--->    ( d1.update({'e':'e'}) ): now the dict is:    ", d1)

d1.update(dict(f="trial"))
print ("--->    ( d1.update(dict('f'=\"trial\"))) ): now the dict is:   ", d1)

d1.update(g=0)
print ("--->    ( d1.update('g'=0) ): now the dict is:  ", d1)
d1.update(g=1111)
print ("--->    ( d1.update('g'=1111) ): now the dict is:   ", d1)


print ("\n############### Removing key:value from the dictionary ##")
del d1['g']
print ("--->    ( del d1['g'] ): now the dict is:   ", d1)
del d1['d']
print ("--->    ( del d1['d'] ): now the dict is:   ", d1)


print ("\n############### Find / Search ##")
print ("--->    ( dict[key] ): get the value of key, if does not exist then this will give error ( d1['a'] ):   ", d1['a'])
print ("--->    ( d1['s'] ): will give the error since key 's' is not in the dict")
print ("--->    ( dict.get(key) ): get the value of key, if does not exist then None will be returned ( d1.get('f') ):  ", d1.get('f'))
print ("--->    ( d1.get('s') ):    ", d1.get('s'))
print ("--->    ( d1.keys() ): to get all the keys:    ", d1.keys())
print ("--->    ( d1.values() ): to get all the values:    ", d1.values())
print ("--->    ( d1.items() ): to get all the key:value pair in the list format:   ", d1.items())
print ("--->    ( list(d1.items()) ): convert dict to list of tuples:    ", list(d1.items()))
print ("--->    ( key in dict ): to check if key is in the dict or not ( 'e' in d1 ):   ", ('e' in d1))
