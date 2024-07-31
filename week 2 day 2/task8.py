import cmath
def finding_height():
    print("Since we know that tan = perpendicular/base so")
    degrees=30
    radians = degrees * (cmath.pi / 180)
    tan_value=cmath.tan(radians)
    height=43*tan_value
    
    print("The value of the height is:",height)
    
finding_height()
    
    
    