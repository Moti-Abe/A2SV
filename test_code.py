class person:
    def __init__(self, name):
        self.name = name
    
    def greet(self):
        print("Hello" , self.name)

p1 = person("Moti")
p1.greet()