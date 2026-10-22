
class NumericList:
    def __init__(self, data):
        self.data = data 

    def get_min(self):
        current_min = self.data[0]
        for value in self.data[1:]:
            if value < current_min:
                current_min = value
        return current_min

    def get_max(self):
        current_max = self.data[0]
        for value in self.data[1:]:
            if value > current_max:
                current_max = value 
        return current_max

    def exists(self, n):
        found = False
        for value in self.data[:]:
            if value == n:
                found = True 
                break
        return found



list = NumericList([67, 12, 45, 89, 109, 23, 18, 10, 5, 102, 120, 77])
print(f"MIN: {list.get_min()}")
print(f"MAX: {list.get_max()}")
print(list.exists(23))