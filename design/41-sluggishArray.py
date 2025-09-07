class SluggishArray:
    def __init__(self, data):
        self.data = data
        self.functions = []

    def map(self, func):
        self.functions.append(func)
        return self

    def apply_functions(self, num):
        for f in self.functions:
            new_num = f(num)
        return new_num

    def get_index_of(self, value):
        for i,v in enumerate(self.data):
            if self.apply_functions(v)==value:
                return i
        return -1


s = SluggishArray([4,5,6])
s.map(lambda x: x+1)
print(s.get_index_of(7))