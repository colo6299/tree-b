
# NOTE: This is all a first draft of the code, and has yet to be run a single time.
#       Be warned. 

class NodeB:

    def __init__(self, b, array=[]):
        self.array = array
        self.b = b


    def _find_array_index(self, item, upper_vindex, lower_vindex):

        def devirt(virtual_index):
            return (virtual_index * 2) + 1

        virtual_center = (lower_vindex + upper_vindex) // 2
        center_item = self.array[devirt(virtual_center)]

        if center_item == item:
            raise ValueError

        if upper_vindex == lower_vindex:
            if center_item > item:
                return devirt(virtual_center) - 1  # these may be a problem, we'll see.
            else:
                return devirt(virtual_center) + 1  # ^

        if center_item > item:
            upper_vindex = virtual_center 
        else:
            lower_vindex = virtual_center + 1
        return self._find_array_index(item, upper_vindex, lower_vindex)

    
    def _split(self):
        promo_index = self.b  # round down when even 
        right_child = NodeB(self.b, array=[None].extend(self.array[promo_index:]))  # sketch af
        promo_triple = self, self.array[promo_index], right_child
        return promo_triple


    def insert(self, item):
        insert_index = self._find_array_index(item, 0, len(self.array))
        if self.array[insert_index] is not None:
            promotion = self.array[insert_index].insert(item)
        else:
            self.array.insert(insert_index, item)  # I could fix these double-inserts, 
            self.array.insert(insert_index, None)  # but it's not really worth the time
        if promotion is not None:
            self.array[insert_index] = promotion[0]
            self.array.insert(insert_index+1, promotion[2])
            self.array.insert(insert_index+1, promotion[1])
        if len(self.array) >= ((self.b * 2) + 1):
            return self._split()
        


class TreeB:

    def __init__(self, b=2, root=None):
        self.b = b
        self.root = root

    def insert(self, item):
        if self.root is None:
            self.root = NodeB(b = self.b, array=[None, item, None])
        else:
            self.root.insert(item)
    



if __name__ == "__main__":
    tree = TreeB()
    tree.insert(5)














