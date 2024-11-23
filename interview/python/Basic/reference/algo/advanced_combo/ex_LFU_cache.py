from collections import defaultdict, OrderedDict

class Node:
    def __init__(self, key=None, val=None, count=1):
        self.key = key
        self.val = val
        self.count = count


class LFU:
    def __init__(self, capacity):
        self.capacity = capacity
        self.key2node = dict()
        self.count2node = defaultdict(OrderedDict)
        self.min_freq = None

    def get(self, key):
        if key not in self.key2node:
            return -1

        node = self.key2node[key]
        del self.count2node[node.count][key]

        if not self.count2node[node.count]:
            del self.count2node[node.count]

        node.count += 1
        self.count2node[node.count][key] = node

        if not self.count2node[self.min_freq]:
            self.min_freq += 1

        return node.val

    def put(self, key, val):
        if not self.capacity:
            return

        if key in self.key2node:
            self.key2node[key].val = val
            self.get(key)
            return

        if len(self.key2node) == self.capacity:
            # pop the least frequent item
            k, n = self.count2node[self.min_freq].popitem(last=False)
            del self.key2node[k]

        new_node = Node(key, val, 1)
        self.key2node[key] = new_node
        self.count2node[1][key] = new_node
        self.min_freq = 1

        return
