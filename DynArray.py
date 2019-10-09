import ctypes


# https://ru.stackoverflow.com/questions/651768/%D0%9A%D0%B0%D0%BA-%D0%BF%D1%80%D0%BE%D0%B2%D0%BE%D0%B4%D0%B8%D1%82%D1%8C-%D1%82%D0%B5%D1%81%D1%82-%D0%BA%D0%BE%D0%B4%D0%B0-%D0%BD%D0%B0-%D0%BF%D0%B0%D0%B9%D1%82%D0%BE%D0%BD
class DynArray:

    def __init__(self):
        self.count = 0  # count -- текущее количество элементов в массиве, , и
        self.capacity = 16  # capacity -- текущая ёмкость буфера (исходно 16 единиц)
        self.array = self.make_array(self.capacity)  # array  указатель на блок памяти нужной ёмкости,
        # хранящий элементы PyObject.

    def __len__(self):
        return self.count

    def make_array(self, new_capacity):
        return (new_capacity * ctypes.py_object)()

    def __getitem__(self, i):
        if i < 0 or i >= self.count:
            raise IndexError('Index is out of bounds')
        return self.array[i]

    def resize(self, new_capacity):
        new_array = self.make_array(new_capacity)
        for i in range(self.count):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity

    def append(self, itm):
        if self.count == self.capacity:
            self.resize(2 * self.capacity)
        self.array[self.count] = itm
        self.count += 1

    def insert(self, i, itm):  # добавляем объект itm в позицию i, начиная с 0
        if self.count == self.capacity:  # если новая длина массива может превысить размер буфера.
            self.resize(2 * self.capacity)  # увеличиваем в 2 раза
        if i == self.__len__():
            self.append(itm)
            return
        self.__getitem__(i)  # проверяем в нужном ли диапазоне номер позиции i
        self.append(itm)
        arr_len = self.__len__() - 1
        while arr_len > i:
            self.array[arr_len - 1], self.array[arr_len] = self.array[arr_len],self.array[arr_len - 1]
            arr_len -= 1


    def delete(self, i):  # удаляем объект в позиции i
        new_array = self.make_array(self.capacity)
        count = 0
        for j in range(self.__len__()):
            if j + count == self.__len__():# фиксируем выход диапазона за длинну массива
                self.array = new_array
                return
            if j != i:
                new_array[j] = self.array[j + count]
            if j == i:
                count += 1
                new_array[j] = self.array[j + count]



# При insert  ++++ Учтите, что новая длина массива может превысить размер буфера.
da = DynArray()
for j in range(1, 5):# заполняем массив значениями
    da.append(j)

da.insert(1, 2)
for i in da: # выводим массив значениями
    print(i, end = ', ')