# https://www.shortcutfoo.com/app/dojos/python-strings/cheatsheet
print ("\n############### String Manipulation ###############")
print ("Information:")
print ("- Python string are immutable. Means python string cannot be changed in-place")
print ("\n\n\n\n")


s = "Hello World!"
print ("Orig string: \"" + s + "\"")
print ("\n############### Size/Length of the string ## ( len(s) ): ", len(s))


print ("\n############### Cases ##")
print ("--->    ( s.captalize() ): capitalize the string (similar to title style):", s.capitalize())
print ("--->    ( s.lower() ): convert all chars of string to lower case:", s.lower())
print ("--->    ( s.upper() ): convert all chars of string to upper case:", s.upper())
print ("--->    ( s.swapcase() ): swap case ( s.swapcase() ):", s.swapcase())
print ("--->    ( s.titlecase() ): title case ( s.title() ):", s.swapcase())
print ("--->    ( s.islower() ): return true if s is lowercase:", s.islower())
print ("--->    ( s.isupper() ): return true if s is uppercase:", s.isupper())
print ("--->    ( s.istitle() ): return true if s is titlecase:", s.istitle())


print ("\n############### Sequence/checking ##")
print ("--->    ( min(s) ): smallest alphabetical char in the string (space if it exist):", min(s))
print ("--->    ( max(s) ): largest alphabetical char in the string:", max(s))
print ("--->    ( s.count('h') ): count char in a string:", s.count('h'))
print ("--->    ( s.isspace() ): return true if s only contains whitespace chars:", s.isspace())
print ("--->    ( s.isalpha() ): return true if s is alphabetic(not included spac and other special char):", s.isalpha())
print ("--->    ( s.isdigit() ): return true if s is digit:", s.isdigit())
print ("--->    ( s.isalnum() ): return true if s is alphanumeric:", s.isalnum())


print ("\n############### Spliting/Joining ##")
print ("--->    ( s.join('123') ): return s joined by iterable '123', ex, 'hello' => '1hello2hello3':", s.join('123'))
s2 = " How are you?"
s3 = s + s2
print ("--->    ( s3 = s + s2 ): string concatenation:", s3)
print ("--->    ( s.strip() ): remove leading and trailing whitespace from s:", s.strip())
print ("--->    ( s.replace(\" \", \"\") ): remove all the whitespace from s:", s.replace(" ", ""))
print ("--->    ( s.strip(\"Hello\") ): remove first and last \"hello\" chars from s if multiple occurance of \"hello\":", s.strip("Hello"))
print ("--->    ( s.lstrip(\"Hello\") ): remove first \"hello\" chars from s if multiple occurance of \"hello\":",  s.lstrip("Hello"))
print ("--->    ( s.rstrip(\"World\") ): remove last \"hello\" chars from s if multiple occurance of \"hello\":", s.rstrip("World"))
print ("--->    ( s3.split(" ", 2) ): Return list of s split by sep(space here) with leftmost maxsplits(3) performed:", s3.split(" ", 2))
print ("--->    ( s3.split(\"!\") ): another example:", s3.split("!"))
print ("--->    ( s.split() ): Return list of s split by space:", s3.split())


print ("\n############### Find/Search ##")
print ("--->    ( s in s3 ): return true if s3 contains s:", (s in s3) )
print ("--->    ( s not in s3 ): return true if s3 does not contain s ( \"abcd\" not in s3 )", ("abcd" not in s3) )
print ("--->    ( s3.find(s) ): find and return lowest index of s in s3, If substring doesn't exist inside the string, it returns -1:", s3.find(s) )
print ("--->    ( s3.replace(s2, \"whats, up?\") ): replace s2 with \"whats, up?\" in s3:", s3.replace(s2, " Whats, up?") )
print ("--->    ( s3.replace(s2, \"whats, up?\", count) ): replace s2 with \"whats, up?\" in s3 at most count times:", s3.replace(s2, " Whats, up?", 1) )
print ("--->    ( s.rfind(substring [,start [,end]]) ): return true if s3 contains s, or -1 if does not exist ( s.rfind('h') ):", s.rfind('h'))
