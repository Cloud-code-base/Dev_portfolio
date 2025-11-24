from Shape import Shape_, Cube, newCube, viewShapes, object_list
import time

def createCube():
    try: 
        name = input("Enter a name for the cube: ")
        colour = input("Enter a colour for the cube: ")
        side = int(input("Enter a single length for the cube: "))

        print("Shape created..")
        time.sleep(1)

        print("\n")
        newCube(name, side, side, side, colour)
        print("\n")

        startProgram()
        
    except ValueError as e:
        print(e)
        print("Please enter an integer value for the side length")
        createCube()




def viewOptions():
    print("All shapes: ")
    viewShapes()

    print("\n")

    print("To view cube details enter 'view' followed by the cube's name")
    print("To remove a cube enter 'delete' followed by the cube's name")
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
        
                print("Cube '" + obj.name + "' deleted")
                print("\n")

        

        viewOptions()

    elif inputCommand == "back":

        print("\n")
        time.sleep(2)

        startProgram()
    
    else:
        startProgram()

             


def startProgram():
    print("\n")
    userInput = input("Enter 'create' to create a cube, 'view' to view cubes or 'exit' to exit the program: ")

    if userInput == "create" or userInput == "CREATE" or userInput == "Create":

        createCube()

            
    elif userInput == "exit" or userInput == "EXIT" or userInput == "Exit":

        print("Exiting program...")

        
        time.sleep(1)
        exit(1)
        

    elif userInput == "view" or userInput == "VIEW" or userInput == "View":

        if len(object_list) < 1:

            print("\n")
            print("No cubes stored")
            startProgram()
        else:
            print("\n")
            viewOptions()
        
    else:
        print("\n")
        print("Exception - '" + userInput + "' is not valid")

        startProgram()





print("\n")
print("------------------------")
print("Object Manipulator 1.0.0")
print("------------------------")

print("\n")
print("This program allows you to realise shapes and manipulate them using the command line")
print("\n")
print("What would you like to do?")





startProgram()
   
        

    






  
     

