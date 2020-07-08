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
 
