def calculate_happiness(A, B, Z):
    happiness = 0
    for i in Z:
        if i in A and i in B:
            happiness += 1
        elif i in B and i not in A:
            happiness -= 1
    return happiness


A = {2, 3}
B = {1, 5, 3}
Z = {3, 1}

# محاسبه میزان شادی
result = calculate_happiness(A, B, Z)
print(f"میزان شادی : {result}")