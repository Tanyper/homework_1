class DequeClass:
    def __init__(self):
        self.elems = []

    def is_empty(self):
        return self.elems == []

    def add_to_front(self, elem):
        self.elems.append(elem)

    def add_to_rear(self, elem):
        self.elems.insert(0, elem)

    def remove_from_front(self):
        return self.elems.pop()



def pal_checker(string):
    string = string.replace(" ", "")
    dc_obj = DequeClass()

    for i in string:
        dc_obj.add_to_rear(i)

    still_equal = True
   
    # Не доделала