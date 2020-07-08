import ctypes


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
            self.array[arr_len - 1], self.array[arr_len] = self.array[arr_len], self.array[arr_len - 1]
            arr_len -= 1
        print(self.capacity)

    def delete(self, i):  # удаляем объект в позиции i
        self.__getitem__(i)  # проверяем в нужном ли диапазоне номер позиции i
        for j in range(i + 1, self.__len__()):# бегаем в нужном  диапазоне сдвигая значения вперед
            self.array[j - 1] = self.array[j]# сдвигаем значения вперед
        self.count = self.__len__() - 1# подрубаем на один с конца количество элементов в массиве
        size_buff_old = int((self.capacity/100)*50)
        size_buff_new = int(self.capacity / 1.5)
        if self.count <= size_buff_old :  # если новая длина массива меньше буфера на 50%.
            self.resize(size_buff_new)  # увеличиваем в 2 раза
        if self.capacity < 16:#сохраняем минимальную ёмкость 16 элементов.
            self.capacity = 16

        return self.array

#
