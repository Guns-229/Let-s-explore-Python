import gc


def test():
    if "t" not in locals():
        t = []
    t.append(t)

class Utils():
    def __init__(self, threshold=[10,2,2], debug=True):
        self.threshold = threshold
        self.debug = debug

    def check(self):
        #return self.debug_cycles() # uncomment to just debug cycles
        l0, l1, l2 = gc.get_count()
        if self.debug:
            print('gc_check called:', l0, l1, l2)
        if l0 > self.threshold[0]:
            num = gc.collect(0)
            if self.debug:
                print('collecting gen 0, found: %d unreachable' % num)
            if l1 > self.threshold[1]:
                num = gc.collect(1)
                if self.debug:
                    print('collecting gen 1, found: %d unreachable' % num)
                if l2 > self.threshold[2]:
                    num = gc.collect(2)
                    if self.debug:
                        print('collecting gen 2, found: %d unreachable' % num)


utils = Utils()
for _ in range(200):
    test()
    if _ % 100 == 0:
        print("Cleaning requested")
        gc.collect()
print(gc.get_count())
print(gc.get_stats())
utils.check()
