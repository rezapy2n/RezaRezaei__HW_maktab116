def is_armstrong_number(num):
   
    temp = num
    order = len(str(num))
    total = 0
    while temp > 0:
        digit = temp % 10
        total += digit ** order
        temp //= 10
    return total == num

def next_armstrong_number():
    
    num = 1
    while True:
        if is_armstrong_number(num):
            yield num
        num += 1


generator = next_armstrong_number()
for _ in range(10):
    print(next(generator))
