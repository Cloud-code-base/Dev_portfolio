


class Shape_():

   

    def __init__(self, name, height = 200, width = 200, length = 200, colour = "grey"):
        super().__init__()

        self.name = name
        self.height = height
        self.width = width
        self.length = length
        self.colour = colour

    
    def displayShape(self):
        print("Name: " + self.name)
        print("Height: " + str(self.height))
        print("Width: " + str(self.width))
        print("Length: " + str(self.length))
        print("Colour: " + str(self.colour))



class Cube(Shape_):
    def __init__(self, name, height = 200, width = 200, length = 200, colour = "grey"):
        super().__init__(name, height, width, length, colour)

object_list = []

def newCube(name, height, width, length, colour):

    length = height = width

    cube = Cube(name, height, width, length, colour)

    object_list.append(cube)

    cube.displayShape()


def viewShapes():

    for obj in object_list:
        print(f"{obj.name}")



    


    
