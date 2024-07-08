class Add:
    def __init__(self):
        self.total = 0

    def __call__(self, num):
        if not isinstance(num, int):
            raise ValueError("Input must be an integer")
        self.total += num
        return self.total


add_instance = Add()
print(add_instance(5)) 
print(add_instance(10)) 
print(add_instance(7))  
