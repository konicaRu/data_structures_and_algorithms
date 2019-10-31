class BloomFilter:

    def __init__(self, f_len):
        self.filter_len = f_len
        self.slot = [0] * f_len  # создаём битовый массив длиной f_len ...

    def hash1(self, str1):
        res1 = 0  # 17
        for c in str1:
            code = ord(c)
            res1 = ((res1 * 17) + code) % self.filter_len
        return res1  # реализация ...

    def hash2(self, str1):  # 223    # ...
        res2 = 0  # 17
        for c in str1:
            code = ord(c)
            res2 = ((res2 * 223) + code) % self.filter_len
        return res2

    def add(self, str1):  # добавляем строку str1 в фильтр
        self.slot[self.hash1(str1)] = 1
        self.slot[self.hash2(str1)] = 1

    def is_value(self, str1):  # проверка, имеется ли строка str1 в фильтре
        if self.slot[self.hash1(str1)] == 1 and self.slot[self.hash2(str1)] == 1:
            return True
        else:
            return False


gt = BloomFilter(32)
gt.add("0123456789")
gt.add("1234567890")
gt.add("2345678901")
gt.add("3456789012")
gt.add("4567890123")
gt.add("5678901234")
gt.add("6789012345")
gt.add("7890123456")
gt.add("8901234567")
gt.add("9012345678")
print(gt.is_value("7890э123456"))
