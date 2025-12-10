class MyName:
    """Опис класу / Документація
    """
    total_names = 0 # Class Variable

    def __init__(self, name=None) -> None:
        """Ініціалізація класу
        """
        if name is not None:
            if not name.isalpha():
                raise ValueError("Ім'я може містити лише літери!")
            
            self.name = name.capitalize()
        else:
            self.name = self.anonymous_user().name 

        MyName.total_names += 1 # modify class variable
        self.my_id = self.total_names

    @property
    def whoami(self) -> str: 
        """Class property"""
        return f"My name is {self.name}"
    
    @property
    def my_email(self) -> str:
        """Class property"""
        return self.create_email()
    

    @property
    def full_name(self) -> str:
        """Повертає повну інформацію про користувача"""
        return f"User #{self.my_id}: {self.name} ({self.my_email})"


    def create_email(self, domain="itcollege.lviv.ua") -> str:
        """Instance method"""
        return f"{self.name}@{domain}"


    def save_to_file(self, filename="OOP\\lab_3\\solo_work\\users.txt"):
        """Записує дані користувача у файл"""
        with open(filename, "a", encoding="utf-8") as file:
            file.write(self.full_name + "\n")
        return (f"Дані для {self.name} успішно збережено у {filename}")

    @classmethod
    def anonymous_user(cls):
        """Class method"""
        return cls("Anonymous")
    
    @staticmethod
    def say_hello(message="Hello to everyone!") -> str:
        """Static method"""
        return f"You say: {message}"
    
    def name_length(self) -> int:
        return len(self.name)


print("Розпочинаємо створювати обєкти!")

names = ("Bohdan", "Marta", "markiyan", None)
all_names = {name: MyName(name) for name in names}

for name, me in all_names.items():
    print(f"""{">*<"*20}
This is object: {me} 
This is object attribute: {me.name} / {me.my_id}
This is {type(MyName.whoami)}: {me.whoami} / {me.my_email}
This is {type(me.create_email)} call: {me.create_email()}
This is static {type(MyName.say_hello)} with defaults: {me.say_hello("Привіт, викладачу!")} 
This is class variable {type(MyName.total_names)}: from class {MyName.total_names} / from object {me.total_names}
This is instance method {type(me.name_length)} call: Довжина імені: {me.name_length()}
This is {type(me.full_name)} call: {me.full_name}
This is saving to file method call: {type(me.save_to_file)} call: {me.save_to_file()}
""")
print(f"We are done. We create {me.total_names} names! ??? Why {MyName.total_names}?")
