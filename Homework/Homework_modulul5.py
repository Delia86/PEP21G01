""" Homework 5 - needs to be presented before exam day"""

# We want to create class for an object that behaves like a triangle, that has flexible sides and angles.
# Because of approximations in python the triangle will get distorted after some of the changes so this is not a
# perfect model

# 30P
#  - class constructor can receive 3 arguments for angles (with default value of 60) and 3 arguments for sides (with
# default value of 1)
# class variables for sides will be called A, B, C
# class variables for angles will be called AB, BC, CA (indicating sides)

# 30P
# - class implements method to modify_angle:
#   - modify_angle method takes two argument:
#       - "angle" and can be one of 3 string values 'AB', 'BC', 'CA'
#       - "degrees" that can be a positive or negative and represents the amount by which the angle will be modified
# If as a result of the change any of the angles will be outside interval (0, 180) then method should raise an exception
# When an angel is modifies you will need to recalculate the opposing side which can be done using the following
# example: angle AB is changed then C = (A**2 + B**2 - 2*A*B*cos(AB))**(1/2)
# Because angles in a triangle must sum up to 180 degrees unmodified angles need to be recalculated after we have
# recalculated the opposite side using the following example:
# angle AB is changed then BC = arccos((B**2+ C**2 - A**2) / 2*B*C), CA = arccos((C**2+ A**2 - B**2) / 2*C*A),


# 30P
# - class implements method to modify_side:
#   - modify_side method takes two argument:
#       - "side" and can be one of 3 string values 'A', 'B', 'C'
#       - "meters" that can be a positive or negative and represents the amount by which the side will be modified
# If as a result of the change sum of the unmodified sides is less than or equal to the changed side then method should
# throw an exception
# If as a result of the change side will be less than or equal to 0 then method should raise a different exception
# When a side is modified by some value all other sides need to be modified by the fraction of the change to maintain
# the same triangle angles. For example, if A increase by +1 then B = ((A+1)/A)*B and C = ((A+1)/A)*C


# 10P
# Create an object from your class with default constructor values and modify angle AB by +30 degrees and side A by +1.5

from math import cos, acos


class Triangle():

    def __init__(self, angle1=60, angle2=60, angle3=60, side1=1, side2=1, side3=1):
        self.AB = angle1
        self.BC = angle2
        self.CA = angle3
        self.A = side1
        self.B = side2
        self.C = side3

    def modify_angle(self,angle, degrees):
        self.angle = angle

    if self.angle == 'AB':
        self.AB = self.AB + degrees
    if self.AB <= 0 or self.AB >= 180:
        raise Exception

    def modify_side(self, side, meters):
        self.side = side

        if self.side=='A'
            self.A=self.A+meters
            self.B=((self.A+1)/self.A)*self.B
            self.C = ((self.A + 1) / self.A) * self.C
            if(self.A+self.B<self.C)or(self.B+self.C<self.A)or(self.C+self.A<self.B):
                raise Exception
            elif(self.A<=0) or (self.B<=0)or(self.C<=0):
                raise Exception ('Lenght should be  greater than zero')




triangle = Triangle(60, 60, 60, 1, 1, 1)
triangle.modify_angle()
triangle.modify_side()
