# Implmentation of Least Recently Used (LRU) cache
#
# Q.1 Basic implmentation if LRU.
# Q.2 Design Animal shelter class with adopt and drop functionalities.

# Reference:
# https://www.youtube.com/watch?v=R0GTqg3pJKg


class NodeType:
    def __init__(self, key=None, val=None):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None


#################### Q.1. Basic LRU implmentation #####################
class LRU:
    def __init__(self, capacity):
        self.capacity = capacity
        self.dictionary = dict()
        self.head = NodeType()
        self.tail = NodeType()
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):
        if key in self.dictionary:
            node = self.dictionary[key]
            self.delete(node)
            self.add(node)
            return node.val
        return -1

    def put(self, key, val):
        if key in self.dictionary:
            self.delete(self.dictionary[key])
        new_node = NodeType(key, val)
        self.add(new_node)
        self.dictionary[key] = new_node
        if len(self.dictionary) > self.capacity:
            deleting_node = self.head.next
            self.delete(deleting_node)
            del self.dictionary[deleting_node.key]
        return

    def delete(self, deleting_node):
        prev = deleting_node.prev
        next = deleting_node.next
        prev.next = next
        next.prev = prev

    def add(self, new_node):
        prev = self.tail.prev
        prev.next = new_node
        new_node.prev = prev
        self.tail.prev = new_node
        new_node.next = self.tail


#################### Q.2. Design Animal shelter #####################
class AnimalNode:
    def __init__(self, animal):
        self.animal = animal
        self.next = None
        self.prev = None


class AnimalShelter:
    def __init__(self):
        self.animals = {}
        self.head = AnimalNode(None)
        self.tail = AnimalNode(None)
        self.head.next = self.tail
        self.tail.prev = self.head

    def drop_off(self, animal_type):
        new_animal = AnimalNode(animal_type)
        self.add(new_animal)
        if animal_type in self.animals:
            self.animals[animal_type].insert(0, new_animal)
        else:
            self.animals[animal_type] = [new_animal]
        return

    def adopt(self, animal_type=None):
        if animal_type:
            if animal_type in self.animals and len(self.animals[animal_type]) > 0:
                adopting_animal = self.animals[animal_type].pop()
                self.delete(adopting_animal)
            else:
                return self.adopt()
        else:
            adopting_animal = self.head.next
            if adopting_animal.animal is not None and len(self.animals[adopting_animal.animal]) > 0:
                self.animals[adopting_animal.animal].pop()
                self.delete(adopting_animal)
            else:
                return -1
        return adopting_animal.animal

    def delete(self, deleting_node):
        prev = deleting_node.prev
        next = deleting_node.next
        prev.next = next
        next.prev = prev

    def add(self, new_node):
        prev = self.tail.prev
        prev.next = new_node
        new_node.prev = prev
        self.tail.prev = new_node
        new_node.next = self.tail


a = AnimalShelter()
a.drop_off("dog")
a.drop_off("cat")
a.drop_off("monkey")
a.drop_off("parrot")
a.drop_off("dog")
adopting = a.adopt("dog"); print (adopting) # "dog"
adopting = a.adopt("dog"); print (adopting) # "dog"
adopting = a.adopt("dog"); print (adopting) # this should return "cat" since no more dogs
adopting = a.adopt(); print (adopting) # "monkey"
adopting = a.adopt(); print (adopting) # "parrot"
adopting = a.adopt(); print (adopting) # -1 since no more animals
