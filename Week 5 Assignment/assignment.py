# Assignment 1: Design Your Own Class! 🏗️
class Music:
    def __init__(self, title, artist, genre, duration):
        self.title = title  
        self.artist = artist  
        self.genre = genre 
        self.duration = duration  
    
    def playMusic(self):
        return f"Playing '{self.title}' by {self.artist}..."

    def describe(self):
        return f"'{self.title}' by {self.artist}, Genre: {self.genre}, Duration: {self.duration} minutes."


class ClassicalMusic(Music):
    def __init__(self, title, artist, duration, composer, orchestra):

        super().__init__(title, artist, "Classical", duration)
        self.composer = composer  
        self.orchestra = orchestra  
    
    def describe(self):
        return (f"'{self.title}' by {self.artist}, composed by {self.composer}, "
                f"performed by {self.orchestra}, Duration: {self.duration} minutes.")


class PopMusic(Music):
    def __init__(self, title, artist, duration, album, release_year, studio):

        super().__init__(title, artist, "Pop", duration)
        self.album = album  
        self.release_year = release_year  
        self.__studio = studio 

    def describe(self):
        return (f"'{self.title}' by {self.artist} from the album '{self.album}' "
                f"(Released: {self.release_year}), Genre: Pop, Duration: {self.duration} minutes.")

    # Getter method for the private studio attribute
    def get_studio(self):
        return self.__studio

    # Setter method for the private studio attribute
    def set_studio(self, studio):
        self.__studio = studio


# Test objects
song1 = ClassicalMusic("Symphony No. 9", "Beethoven", 70, "Ludwig van Beethoven", "Vienna Philharmonic")
song2 = PopMusic("Blinding Lights", "The Weeknd", 3.5, "After Hours", 2020, "MXM Studios")

# Testing methods
print(song1.describe())
print(song1.playMusic())
print(song2.describe())
print(song2.playMusic())

# Access studio attribute using the getter
print(f"Recorded at: {song2.get_studio()}")

# Modify studio attribute using the setter
song2.set_studio("Jungle City Studios")
print(f"Updated recording studio: {song2.get_studio()}")


# Activity 2: Polymorphism Challenge! 🎭
class Vehicle:
    def __init__(self, name="Generic Vehicle"):
        self.name = name

    def move(self):
        return f"{self.name}: Moving!"

class Car(Vehicle):
    def __init__(self, name="Car"):
        super().__init__(name)

    def move(self):
        return f"{self.name}: Driving!"

class Plane(Vehicle):
    def __init__(self, name="Plane"):
        super().__init__(name)

    def move(self):
        return f"{self.name}: Flying!"

class Boat(Vehicle):
    def __init__(self, name="Boat"):
        super().__init__(name)

    def move(self):
        return f"{self.name}: Sailing!"

class Bike(Vehicle):
    def __init__(self, name="Bike"):
        super().__init__(name)

    def move(self):
        return f"{self.name}: Cycling!"


# Test objects
vehicles = [
    Car(name="Toyota"),
    Plane(),
    Boat(),
    Bike(name="Mountain Bike"),
]

for vehicle in vehicles:
    print(vehicle.move())
