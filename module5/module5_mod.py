class Numbers:

    def __init__(self):
        self.nums = []

    def add_number(self, num):
        self.nums.append(num)

    def find_index(self, num):
        return self.nums.index(num) + 1 if num in self.nums else -1
