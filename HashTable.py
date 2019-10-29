class HashTable:
    def __init__(self, sz, stp):
        self.size = sz
        self.step = stp
        self.slots = [None] * self.size  # создает массив с size количеством слотов

    def hash_fun(self, value):  # в качестве value поступают строки!
        # всегда возвращает корректный индекс слота
        return sum(map(ord, value)) % self.size  # суммируем значения кодов символов строки, и потом их брать по модулю размера таблицы.

    # анограммы будут иметь такой же вес, Чтобы исправить это, следует использовать позицию символа в качестве веса
    def seek_slot(self, value):
        num = self.hash_fun(value)
        count = 0
        while None in self.slots:
            if self.slots[num] == None:
                return num
            if self.slots[num] != None:
                num += self.step
            if num > self.size - 1:  # находит индекс пустого слота для значения, или None
                num = count
                count += 1
        return None

    def put(self, value):
        num = self.seek_slot(value)
        if num != None:
            self.slots[num] = value
            return num
        else:  # записываем значение по хэш-функции
            return None

    def find(self, value):
        count = 0
        num = self.hash_fun(value)
        while value in self.slots:
            if self.slots[num] == value:
                return num
            if self.slots[num] != value:
                num += self.step
            if num > self.size - 1:  # находит индекс пустого слота для значения, или None
                num = count
                count += 1
        else:
            # находит индекс слота со значением, или None
            return None


ls = HashTable(13, 3)
print(ls.put("reet"))
print(ls.put("retq"))
print(ls.put("resdrt"))
print(ls.put("recvrt"))
print(ls.put("r'l;kuet"))
print(ls.put("renhyumet"))
print(ls.put("rdfet"))
print(ls.put("rdf;let"))
print(ls.put("reuut"))
print(ls.put("redt"))
print(ls.put("rdfet"))
print(ls.put("redt"))
print(ls.put("redtrre"))
print(ls.put("redttrtrre"))
print(ls.find("redt"))
