from random import randint

class NodeB:

    def __init__(self, b, array=[]):
        self.array = array
        self.b = b

    def _find_array_index(self, item, lower_vindex, upper_vindex):
        '''
        Returns the index of the child the item should belong to

        will be redone in due time
        '''
        # We'll just pretend this works exactly as intended 

        def devirt(virtual_index):
            return (virtual_index * 2) + 1

        virtual_center = (lower_vindex + upper_vindex) // 2
        center_item = self.array[devirt(virtual_center)]

        if center_item == item:
            return devirt(virtual_center), True  # I know, I know...

        if upper_vindex == lower_vindex:
            if center_item > item:
                return (devirt(virtual_center) - 1), False  # these may be a problem, we'll see.
            else:
                return (devirt(virtual_center) + 1), False  # ^

        if center_item > item:
            upper_vindex = virtual_center - 1
            if lower_vindex == virtual_center:
                return (devirt(virtual_center) - 1), False
        else:
            if lower_vindex == virtual_center:
                return (devirt(virtual_center) + 1), False
            lower_vindex = virtual_center 
        return self._find_array_index(item, lower_vindex, upper_vindex)
    
    def _split(self):
        promo_index = self.b  # round down when even 
        right_child = NodeB(self.b, array=self.array[promo_index+1:])  # sketch af
        promo_triple = self, self.array[promo_index], right_child 
        del self.array[promo_index:]  # never seen del before, neato
        return promo_triple

    def insert(self, item):

        def revirt(real_index):
            return (real_index - 1) // 2

        promotion = None
        insert_index = self._find_array_index(item, 0, revirt(len(self.array)))[0]
        if self.array[insert_index] is not None:
            promotion = self.array[insert_index].insert(item)
        else:
            self.array.insert(insert_index, item)  # I could fix these double-inserts,
            self.array.insert(insert_index, None)  # but it's not really worth the effort
        if promotion is not None:
            self.array[insert_index] = promotion[0]
            self.array.insert(insert_index+1, promotion[2])
            self.array.insert(insert_index+1, promotion[1])
        if len(self.array) >= ((self.b * 2) + 1):
            return self._split()

    def val_order_traverse(self, outlist):
        for index, item in enumerate(self.array):
            if index % 2 is 0:
                if item is not None:
                    item.val_order_traverse(outlist)
            else:
                outlist.append(item)

    def _structure_probe(self, outlist, depth):
        tlist = []
        vlen = (len(self.array)-1)//2
        for i in range(vlen):
            tlist.append(self.array[(2*i)+1])
        tstring = 'Depth ' + str(depth) + ': ' + str(tlist)
        outlist.append(tstring)
        for i in range(vlen+1):
            if self.array[2*i] is not None:
                self.array[2*i]._structure_probe(outlist, depth+1)

    def contains(self, item):
        return self.search(item, True)

    def search(self, item, yn=False):

        def revirt(real_index):
            return (real_index - 1) // 2

        result = self._find_array_index(item, 0, revirt(len(self.array)))

        if result is None:
            return False
        elif self.array[result[0]] is None:
            if yn is True:
                return True
            else:
                return self.array[result[0]]          
        elif result[1] is False:
            return self.array[result[0]].search(item, yn)
        elif result[1] is True:
            if yn is True:
                return True
            else:
                return self.array[result[0]]          


        # if type(result) is not tuple:
        #     if result is not None:
        #         return self.array[result].search(item, yn)
        #     else:
        #         return False
        # else:
        #     if yn is True:
        #         return True
        #     else:
        #         return result[0]


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

    def probe(self):
        if self.root is None:
            return 'Empty tree!'
        else:
            plist = []
            self.root._structure_probe(plist, 0)
            for string in plist:
                print(string)

    def contains(self, item):
        if self.root is not None:
            return self.root.search(item, True)
        else:
            return False

    def search(self, item):
        if self.root is not None:
            self.root.search(item)
        else:
            return False

if __name__ == "__main__":
    tree = TreeB(5)

    def _insert_b(b, l=10):
        tree = TreeB(b)
        test_list = []
        for _ in range(l):
            n = randint(0, 1000)
            if n not in test_list:
                test_list.append(n)
        # for item in test_list:
        #     tree.insert(item)
        return tree, test_list

    items = _insert_b(6, 15)[1]
    # for item in [5, 4, 6, 7, 11, 13, 15, 32, 3, 17]:
    #     tree.insert(item)
    for item in items:
        tree.insert(item)
    

    print(tree.value_order_traversal())
    tree.probe()
    print(tree.search(11))














