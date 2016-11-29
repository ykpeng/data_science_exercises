def powerSet(items):
    N = len(items)
    # enumerate the 2**N possible combinations
    for i in xrange(2**N):
        combo = []
        print "i: " + '{0:08b}'.format(i)
        for j in xrange(N):
            # test bit jth of integer i
            print "j: " + str(j)
            print "i >> j: " + '{0:08b}'.format(i >> j)
            if (i >> j) % 2 == 1:
                combo.append(items[j])
        print combo
        yield combo

def yieldAllCombos(items):
    """
        Generates all combinations of N items into two bags, whereby each
        item is in one or zero bags.

        Yields a tuple, (bag1, bag2), where each bag is represented as a list
        of which item(s) are in each bag.
    """
    N = len(items)
    # enumerate the 2**N possible combinations
    for i in range(3**N):
        bag1 = []
        bag2 = []
        for j in range(N):
            # test bit jth of integer i
            if (i // (3**j)) % 3 == 1:
                bag1.append(items[j])
            elif (i // (3**j)) % 3 == 2:
                bag2.append(items[j])
        yield (bag1, bag2)

items = [1,2,3,4]
generator = yieldAllCombos(items)
generator.next()
generator.next()
generator.next()
generator.next()
generator.next()
generator.next()
generator.next()
generator.next()
