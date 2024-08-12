class Pet:
    def __init__(self, name="", pet_type="", age=0):
        self.__name = name
        self.__type = pet_type
        self.__age = age

    def set_name(self, name):
        self.__name = name

    def set_type(self, pet_type):
        self.__type = pet_type

    def set_age(self, age):
        self.__age = age

    def get_name(self):
        return self.__name

    def get_type(self):
        return self.__type

    def get_age(self):
        return self.__age

def main():
    # Create a Pet object
    animal = Pet()

    # Get values for a pet
    input_name = input("Enter a pet name: ")
    animal.set_name(input_name)

    input_type = input("Enter a pet type: ")
    animal.set_type(input_type)

    input_age = int(input("Enter a pet age: "))
    animal.set_age(input_age)

    # Show values for this pet
    print(f"The pet name is {animal.get_name()}")
    print(f"The pet type is {animal.get_type()}")
    print(f"The pet age is {animal.get_age()}")

if __name__ == "__main__":
    main()
