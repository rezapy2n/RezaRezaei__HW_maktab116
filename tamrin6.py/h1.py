class Date:
    def __init__(self, date_str: str) -> None:
        self.date_str = date_str

    @classmethod
    def from_string(cls, date_str: str) -> 'Date':
   
        return cls(date_str)

    @staticmethod
    def is_valid_date(date_str: str) -> bool:
       
        return True  

    def to_shamsi(self) -> str:
        
        return "تاریخ شمسی"

    def to_ghamari(self) -> str:
        
        return "تاریخ قمری"


date1 = Date.from_string('11-09-2021')

if date1.is_valid_date():
    
    print(f"تاریخ معتبر: {date1.to_shamsi()} - {date1.to_ghamari()}")
else:
    print("تاریخ نامعتبر!")

date2 = Date.from_string('54-32-2')
if date2.is_valid_date():
    print(f"تاریخ معتبر: {date2.to_shamsi()} - {date2.to_ghamari()}")
else:
    print("تاریخ نامعتبر!")
