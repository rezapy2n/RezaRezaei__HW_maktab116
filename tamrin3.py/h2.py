def sed(pattern_string, replacement_string, file_input, file_output):
    try:
        # خواندن محتویات فایل ورودی
        with open(file_input, 'r') as file:
            content = file.read()
        
        # جایگزینی الگو با رشته جدید
        content = content.replace(pattern_string, replacement_string)
        
        # نوشتن محتویات جدید به فایل خروجی
        with open(file_output, 'w') as file:
            file.write(content)
            
    except FileNotFoundError:
        print(f"خطا: فایل '{file_input}' یافت نشد.")
    except IOError as e:
        print(f"خطای ورودی/خروجی: {e}")
    except Exception as e:
        print(f"یک خطای غیرمنتظره رخ داد: {e}")

# مثال استفاده از تابع
sed('pattern_string', 'replacement_string', 'input.txt', 'output.txt')