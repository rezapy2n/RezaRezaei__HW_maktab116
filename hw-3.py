def count_digits_letters(s):
    digit_count = sum(c.isdigit() for c in s)
    letter_count = sum(c.isalpha() for c in s)
    return digit_count, letter_count

user_input = input("python 3.2 ")

digits, letters = count_digits_letters(user_input)
print(f"Digits: {digits}")
print(f"Letters: {letters}")