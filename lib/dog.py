# lib/dog.py

approved_breeds = ["Mastiff", "Chihuahua", "Corgi", "Shar Pei", "Beagle", "French Bulldog", "Pug", "Pointer"]

class Dog:
    def __init__(self, name="Mutt", breed="Mutt"):
        self._name = None
        self._breed = None
        self.name = name
        self.breed = breed

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 25:
            self._name = value
        else:
            print("Name must be string between 1 and 25 characters.")
            self._name = None

    @property
    def breed(self):
        return self._breed

    @breed.setter
    def breed(self, value):
        if self._name is not None:  # Only validate breed if name is valid
            if value in approved_breeds:
                self._breed = value
            else:
                print("Breed must be in list of approved breeds.")
                self._breed = None
        else:
            self._breed = None
