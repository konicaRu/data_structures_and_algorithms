class NativeDictionary:
    def __init__(self, sz):
        self.size = sz
        self.slots = [None] * self.size
        self.values = [None] * self.size

    def hash_fun(self, key):
        return sum(map(ord, key)) % self.size

    def is_key(self, key):
        num = self.hash_fun(key)
        if num in self.slots:
            return True
        else:
            return False

    def put(self, key, value):
        num = self.hash_fun(key)
        self.slots[num] = num
        self.values[num] = value

    def get(self, key):
        num = self.hash_fun(key)
        if num in self.slots:
            return self.values[num]
        else:
            return None

fb = NativeDictionary(13)
fb.put('rama','a')
fb.put('rawma','kj')
fb.put('ramfa','ru')
fb.put('rama','c')
print(fb.is_key('rawma'))
print(fb.is_key('rawwema'))
print(fb.get('rama'))
print(fb.get('rapoima'))
