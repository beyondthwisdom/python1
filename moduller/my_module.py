# my_module.py

# Değişkenler
greeting = "Hello, World!"

# Fonksiyonlar
def say_hello(name):
    return f"{greeting}, {name}!"

# Sınıflar
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def get_details(self):
        return f"Name: {self.name}, Age: {self.age}"
