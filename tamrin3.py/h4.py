from collections import Counter
import re

def find_most_common_words(paragraph):
    # پاک‌سازی متن و جداسازی کلمات
    words = re.findall(r'\w+', paragraph.lower())
    # شمارش تکرار هر کلمه
    word_counts = Counter(words)
    # پیدا کردن بیشترین تعداد تکرار
    max_count = max(word_counts.values())
    # استخراج کلماتی که بیشترین تکرار را دارند
    most_common_words = [word for word, count in word_counts.items() if count == max_count]
    return most_common_words, max_count

# مثال استفاده از تابع
paragraph_input = " نشان می‌دهد که کد چگونه کار می‌کند. ."
most_common_words, count = find_most_common_words(paragraph_input)
print(f'کلماتی که بیشترین تکرار را دارند: {most_common_words} با تعداد تکرار: {count}')
