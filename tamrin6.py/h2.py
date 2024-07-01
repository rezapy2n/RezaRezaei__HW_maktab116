class User:
    user_count = 0  

    def __init__(self, username: str, password: str, phone_number: str = None) -> None:
        self.username = username
        self.password = self._validate_password(password)
        self.phone_number = phone_number
        self.id = User.user_count
        User.user_count += 1

    def _validate_password(self, password: str) -> str:
     
        if len(password) < 4:
            raise ValueError("password (4 karakter)")
        return password

    def __str__(self) -> str:
      
        return f"name karbari : {self.username},  shomare telephone: {self.phone_number}, shenase: {self.id}"

    @staticmethod
    def change_password(old_password: str, new_password: str, confirm_password: str) -> None:
     
        if old_password != User.current_user.password:
            print("error :gozar vage feli nadorost ast")
        elif new_password != confirm_password:
            print("error : gozar vage haye gadid tatabogh nadarad")
        else:
            User.current_user.password = new_password
            print("gozar vazhe taghir yaft")


users = {}  

while True:
    print("\n name karbari")
    print("1. sabt name")
    print("2. vorod")
    print("3. taghir gozar vage")
    print("4. khorog")
    choice = input("adad ra vared konid: ")

    if choice == "1":
        username = input("name kkarbari : ")
        password = input("gozar vage: ")
        phone_number = input("shomare telephon (ekhtiari) ")
        users[username] = User(username, password, phone_number)
        print(f"karbar {username} ba moafaghiat igad shod")

    elif choice == "2":
        username = input("name karbari: ")
        password = input("gozar vage: ")
        if username in users and users[username].password == password:
            User.current_user = users[username]
            print("vorod moafagh amiz")
            print("1. namyeh etellaat karbari")
            print("2. virayesh etelaat")
            print("3.  taghir gozar vage")
            print("4. khorog")
            inner_choice = input("adad ra vared konid : ")
            if inner_choice == "1":
                print(User.current_user)
            elif inner_choice == "2":
                new_username = input("name karbari gadid : ")
                if new_username in users:
                    print("error: name karbari tekrari ast")
                else:
                    User.current_user.username = new_username
                    print("name karbari taghir yaft")
            elif inner_choice == "3":
                old_pass = input("gozar wazhe feli : ")
                new_pass