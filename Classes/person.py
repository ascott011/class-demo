#test
class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def greeting(self) -> str:
        #returns a string that greets the person's name
        return f'Hello, my name is {self.name}, and I am {self.age} years old.'
    
    def have_birthday(self) -> None:
        #increase the person's age by one year
        self.age += 1
        print(f'Happy birthday. {self.name}! You are now {self.age}.')

def main():
    Alex = Person('Alex', 33)
    Ronny = Person('Ronny', 98)

    #call their methods
    print(Alex.greeting())
    print(Ronny.greeting())

    #birthday for Ronny
    Ronny.have_birthday()
    print(Ronny.have_birthday())

if __name__ == "__main__":
    main()