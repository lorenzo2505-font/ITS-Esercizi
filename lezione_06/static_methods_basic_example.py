class Math:
    PI:float = 3.14 # Public class attribute
    @staticmethod
    def circle_area(radius:float) -> float: # Static Method
        return Math.PI * radius * radius
    

print(Math.PI) # Output: 3.14

print(Math.circle_area(5)) # Output: 78.5

