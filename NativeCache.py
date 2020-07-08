class NativeCache:
    def __init__(self, sz):
        self.size = sz
        self.slots = [None] * self.size
        self.values = [None] * self.size
        self.hits = [0] * self.size

    def hash_fun(self, key):
        return sum(map(ord, key)) % self.size

    def seek_slot(self, key):
        num = self.hash_fun(key)
        count = 0
        step_find = 3
        while True:
            if None not in  self.slots:
                num_del = self.hits.index(min(self.hits))
                self.hits[num_del] = 0
                self.slots[num_del] = None
                self.values[num_del] = None
            if self.slots[num] == None:
                return num
            if self.slots[num] != None:
                num += step_find
            if num > self.size - 1:  # находит индекс пустого слота для значения, или None
                num = count
                count += 1

    def put(self, key, value):
        num = self.seek_slot(key)
        self.slots[num] = key
        self.values[num] = value
        self.hits[num] += 1

cash = NativeCache(7)
cash.put('1','a')
cash.put('2','b')
cash.put('3','c')
cash.put('4','d')
cash.put('5','e')
cash.put('1','f')
cash.put('2','j')
cash.put('8','j')
 
