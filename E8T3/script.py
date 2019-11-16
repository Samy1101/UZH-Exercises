# The signatures of this class and its public methods are required for the automated
# grading to work. You must not change the names or the list of parameters. You may
# introduce private/protected utility methods though.


class Fridge:

    def __init__(self):
        self.__items = []
        self.__idx = 0

    def store(self, item):
        self.__items.append(item)

    def take(self, item):
        if item in self.__items:
            idx = self.__items.index(item)
            taken = self.__items.pop(idx)
            return taken

        raise Warning("The requestied item is not stored in the fridge")

    def find(self, name):
        items = sorted(self.__items)

        for idx, val in enumerate(items):
            if name in val:
                return val
        return None

    def take_before(self, date):
        item_list = []

        for idx, val in enumerate(self.__items):
            if date > val[0]:
                item_list.append(val)
                self.__items.remove(val)

        return item_list

    def __iter__(self):
        items = sorted(self.__items)
        return iter(items)

    def __next__(self):
        try:
            item = self.__items[self.__idx]
        except IndexError:
            raise StopIteration()
        self.__idx += 1
        return item

    def __len__(self):
        return len(self.__items)

    # To implement the required functionality, you will also have to implement several
    # of the special functions that typically include a double underscore.


# You can play around with your implementation in the body of the following 'if'.
# The contained statements will be ignored while evaluating your solution.
if __name__ == '__main__':
    l = ["a", "b", "c"]
    for i in l:
        l.remove(i)

    f = Fridge()
    f.store((191127, "Butter"))
    f.store((191117, "Milk"))

    print("Items in the fridge:")
    for i in f:
        print("- {} ({})".format(i[1], i[0]))


    i = f.take((191127, "Butter"))
    print("Removed {}, {} items left".format(i, len(f)))
