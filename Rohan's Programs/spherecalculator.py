import math

def create_sa(radius):
    sa=4*math.pi*(radius**2)
    print("The surface area is",sa)

def create_v(radius):
    v=4/3*math.pi*(radius**3)
    print("The volume is",v)

def main():
    x=eval(input("Enter radius: "))
    create_sa(x)
    create_v(x)
main()