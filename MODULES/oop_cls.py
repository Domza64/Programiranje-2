class Animal:

    def __init__(self, animal, name):
        self._animal = animal
        self._name = name

    def __str__(self):
        return f"Animal: {self._animal} | Name: {self._name}"

    def move(self):
        print(f"{self.__class__} is moving!")

    def make_sound(self):
        print("There is no specific sound for animal - subclassess will define that.")


class Tiger(Animal):
    def __init__(self, animal, name, years):
        super().__init__(animal, name)
        self._years = years

    def __str__(self):
        repr_super = super().__str__()
        repr_tiger_spec = f" | years old: {self._years}"
        return repr_super + repr_tiger_spec

    def make_sound(self):
        print("Tiger specific sound...")


class Eagle(Animal):
    def __init__(self, animal, name, live_in):
        super().__init__(animal, name)
        self._live_in = live_in

    def __str__(self):
        repr_super = super().__str__()
        repr_eagle_spec = f" | years old: {self._years}"
        return repr_super + repr_eagle_spec

    def fly(self):
        print("Flying...")
        
    def make_sound(self):
        print("Eagle specific sound...")


class Toy:

    def __init__(self, price):
        self._price = price

    def __str__(self):
        return f"Price is: {self._price}"

    def make_sound():
        print("Some toy sound...")


class RubberTiger(Toy, Tiger):
    def __init__(self, animal, name, years, price, store_name):
        Tiger.__init__(self, animal, name, years)
        Toy.__init__(self, price)
        self._store = store_name

    def say_hello_specific(self):
        print("Can not say anything")

    def __str__(self):
        return f"{self._store} | {self._price} € | {self._name}"