# Design class to include following methods considering perfomance as main priority
# class RandomSet {
#     bool insertKey(int k)
#     bool removeKey(int k)
#     # returns a random key that is in the set
#     # has to be actually random, no fair returning just the first element every time
#     int getRandomKey()
# }

import random

class RandomSet():
    def __init__(self):
        self.index_to_num = dict()
        self.num_to_index = dict()
        self.size = 0
        
        
    def insertKey(self, k):
        if k in self.num_to_index:
            return False
        self.size += 1
        self.index_to_num[self.size] = k
        self.num_to_index[k] = self.size
        return True
    
    
    def removeKey(self, k):
        if k not in self.num_to_index:
            return False
        
        index = self.num_to_index[k]
        del self.num_to_index[k]
        if index in self.index_to_num:
            del self.index_to_num[index]

        return True
        
        
        
    def getRandomKey(self):
        if self.size <= 0:
            raise Exception("Empty set!!!")
            
        rand = -1
        while rand not in self.index_to_num: 
            rand = random.randint(0, self.size)
        
        return self.index_to_num[rand]
    
        
rs = RandomSet()

print (rs.insertKey(10))
print (rs.insertKey(20))
print (rs.insertKey(294039534))
print (rs.removeKey(20))
print (rs.insertKey(10))
print (rs.insertKey(22))
print (rs.insertKey(55))
print (rs.insertKey(2999))
print (rs.insertKey(1111))

for i in range(100):
    print (rs.getRandomKey())
