class DoubleLinkedNode:
    def __init__(self, key = None, val = None, left=None, right=None):
        self.key = key
        self.val = val
        self.left = left 
        self.right = right

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.most, self.least = DoubleLinkedNode(), DoubleLinkedNode()
        self._connectNodes(self.most, self.least)
        self.ref = {}
        self.capacity = capacity
        
        
    def _connectNodes(self, first, second):
        first.right = second
        second.left = first
    
    
    def _putNodeToMost(self, curr_node):
        self._connectNodes(curr_node.left, curr_node.right)
        self._connectNodes(curr_node, self.most.right)
        self._connectNodes(self.most, curr_node)
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.ref:
            curr_node = self.ref[key]
            self._putNodeToMost(curr_node)
            return self.ref[key].val
        else:
            return -1
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.ref:
            curr_node = self.ref[key]
            self._putNodeToMost(curr_node)
            self.ref[key].val = value
        else:
            new_node = DoubleLinkedNode(key, value, None, None)
            self.ref[key] = new_node
            self._connectNodes(new_node, self.most.right)
            self._connectNodes(self.most, new_node)
            
            if len(self.ref) > self.capacity:
                least_node = self.least.left
                self._connectNodes(least_node.left, self.least)
                self.ref.pop(least_node.key)
                
                
            
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
