
class Transform:
    
    def scale(obj, scaleFactor):
        obj.width = obj.width * scaleFactor
        obj.height = obj.height * scaleFactor
        obj.length = obj.length * scaleFactor

        obj.displayShape()