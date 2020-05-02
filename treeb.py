
# NOTE: This is all a first draft of the code, and has yet to be run a single time.
#       Be warned. 

class NodeB:

    def __init__(self, b, array=[]):
        self.array = array
        self.b = b


    def _find_array_index(self, item, lower_vindex, upper_vindex):

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
            upper_vindex = virtual_center - 1

        else:
            lower_vindex = virtual_center 
        return self._find_array_index(item, upper_vindex, lower_vindex)

    
    def _split(self):
        print('s')
        promo_index = self.b  # round down when even 
        right_child = NodeB(self.b, array=self.array[promo_index+1:])  # sketch af
        promo_triple = self, self.array[promo_index], right_child 
        del self.array[promo_index:]  # never seen del before, neato
        return promo_triple


    def insert(self, item):

        def revirt(real_index):
            return (real_index - 1) // 2

        promotion = None
        insert_index = self._find_array_index(item, 0, revirt(len(self.array)))
        print(self.array)
        if self.array[insert_index] is not None:
            promotion = self.array[insert_index].insert(item)
        else:
            self.array.insert(insert_index, item)  # I could fix these double-inserts, 
            self.array.insert(insert_index, None)  # but it's not really worth the time
        if promotion is not None:
            self.array[insert_index] = promotion[0]
            self.array.insert(insert_index+1, promotion[2])
            self.array.insert(insert_index+1, promotion[1])
        print(self.array)
        if len(self.array) >= ((self.b * 2) + 1):
            return self._split()

    def val_order_traverse(self, outlist):
        for index, item in enumerate(self.array):
            if index % 2 is 0:
                if item is not None:
                    item.val_order_traverse(outlist)
            else:
                outlist.append(item)
        


class TreeB:

    def __init__(self, b=3, root=None):
        self.b = b
        self.root = root

    def insert(self, item):
        promotion = None
        if self.root is None:
            self.root = NodeB(b = self.b, array=[None, item, None])
        else:
            promotion = self.root.insert(item)
        if promotion is not None:
            self.root = NodeB(self.b, array=list(promotion))
    
    def value_order_traversal(self,node=None):
        retlist = []
        if node is None:
            node = self.root
        node.val_order_traverse(retlist)
        return retlist



if __name__ == "__main__":
    tree = TreeB()
    tree.insert(5)
    tree.insert(6)
    tree.insert(7)
    tree.insert(11)
    tree.insert(13)
    tree.insert(15)
    print(tree.value_order_traversal())














