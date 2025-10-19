# Parent Class
class Animal():
    def __init__(self,name):
        self.alive = True
        self.name = name

    def moves(self):
        print(f"{self.name} is Moving")

# Child Class
class Dragon(Animal):
    def __init__(self,name):
        super().__init__(name)
    
    def breathes(self):
        print("Breathing Fire!!")

toothless = Dragon("dragon")
print(f"Is Dragon Alive? {toothless.alive}")
toothless.moves()
toothless.breathes()
