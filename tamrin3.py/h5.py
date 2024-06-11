def count_characters(s):
    # شمارش تعداد هر کاراکتر در رشته
    counts = {}
    for char in s:
        counts[char] = counts.get(char, 0) + 1
    return counts

# رشته نمونه
sample_string = "www.google.com"
# شمارش و چاپ نتیجه
result = count_characters(sample_string.lower())  # تبدیل به حروف کوچک برای شمارش دقیق
print(result)