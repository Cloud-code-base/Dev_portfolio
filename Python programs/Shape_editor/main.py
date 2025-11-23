from Shape import Shape_, Cube, Sphere, Cylinder, Cone, newCube, newSphere, viewShapes, object_list
import time



def viewOptions():
    print("All shapes: ")
    viewShapes()

    print("\n")

    print("To view shape details enter 'view' followed by the shape's name")
    print("To remove a shape enter 'delete' followed by the shape's name")
    print("To revert to the menu entry, enter 'back' ")

    print("\n")

    viewUserInput = input("Enter a command: ")
    inputCommand = viewUserInput[:viewUserInput.find(" ")]
    inputArg = viewUserInput[viewUserInput.find(" ") + 1:] 

    if inputCommand == "view":

        for obj in object_list:
            if obj.name == inputArg:
                time.sleep(1)
                print("\n")
                print(f"Name: {obj.name}")
                print(f"Height: {obj.height}")
                print(f"Width: {obj.width}")
                print(f"Length: {obj.length}")
                print(f"Colour: {obj.colour}")
                print("\n")
            
            else:
                continue
            
            viewOptions()
            

    elif inputCommand == "delete":
        
        for obj in object_list:
            if obj.name == inputArg:

                object_list.remove(obj)

        viewOptions()

    elif inputCommand == "back":

        print("\n")
        time.sleep(2)

        startProgram()
    
    else:
        startProgram()

             


def startProgram():
    print("\n")
    userInput = input("Enter 'create' to create a shape, 'view' to view shapes or 'exit' to exit the program: ")

    if userInput == "create" or userInput == "CREATE" or userInput == "Create":
        
        userInputCreate = input("What shape would you like to create? enter 'cube' for a cube, 'sphere' for a sphere, 'cylinder' for a cylinder or 'cone' for a cone: ")
        
        if userInputCreate == "cube" or userInputCreate == "CUBE" or userInput == "Cube":

            name = input("Enter a name for the cube: ")
            colour = input("Enter a colour for the cube: ")
            side = int(input("Enter a single length for the cube: "))

            print("Shape created..")
            time.sleep(1)

            print("\n")
            newCube(name, side, side, side, colour)
            print("\n")

            startProgram()

        if userInputCreate == "sphere" or userInputCreate == "SPHERE" or userInput == "Sphere":

            name = input("Enter a name for the sphere: ")
            colour = input("Enter a colour for the sphere: ")
            radius = int(input("Enter a radius for the sphere: "))

            print("Shape created..")
            time.sleep(1)

            print("\n")
            newSphere(name, radius, colour)
            print("\n")

            
    elif userInput == "exit" or userInput == "EXIT" or userInput == "Exit":

        print("Exiting program...")
        time.sleep(1)
        

    elif userInput == "view" or userInput == "VIEW" or userInput == "View":

        if len(object_list) < 1:

            print("No Shapes stored")
        else:
            print("\n")

            viewOptions()
        
    else:
        print("\n")
        print("Exception - '" + userInput + "' is not valid")





print("\n")
print("------------------------")
print("Object Manipulator 1.0.0")
print("------------------------")

print("\n")
print("This program allows you to realise shapes and manipulate them using the command line")
print("\n")
print("What would you like to do?")





startProgram()
   
        

    






  
     

