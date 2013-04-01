class Queue(object):
    """A Queue is an ordered set
       The only methods available are insert() and remove()
       Queue is a FIFO data structure"""

    def __init__(self):
        """Create an empty set"""
        self.vals = []

    def insert(self, e):
        """Adds an item to the end of the Queue"""
        self.vals.append(e)

    def remove(self):
        """Removes the first item in the Queue"""
        try:
            self.vals.pop(0)
        except:
            raise ValueError()
