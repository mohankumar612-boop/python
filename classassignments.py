# Create a class and function, and list out the items in the list
class classassignments():
    def Subfields():
        aihas=["Machine Learning","Neural Networks","Vision","Robotics","Speech Processing","Natural Language Processing"]
        print("sub-fields in AI are:")
        for aival in aihas:
            print(aival)
    # Create a function that checks whether the given number is Odd or Even
#class OddEven():
    def OddEven():
        getval=int(input("Enter a number:"))
        if((getval%2)==1):
            print(getval,"is Odd Number")
        else:
            print(getval,"is Even Number")
# Create a function that tells elegibility of marriage for male and female according to their age limit like 21 for male and 18 for female
#class ElegiblityForMarriage():
    def Elegible():
        getgender=input("Your Gender:")
        getage=int(input("Your Age:"))
        if((getgender=="Male" and getage>=21) or (getgender=="Female" and getage>=18)):
            print("ELIGIBLE")
        else:
            print("NOT ELIGIBLE")
# calculate the percentage of your 10th mark
#class FindPercent():
    def percentage():
        getsub1=int(input("Subject1="))
        getsub2=int(input("Subject2="))
        getsub3=int(input("Subject3="))
        getsub4=int(input("Subject4="))
        getsub5=int(input("Subject5="))
        gettot=getsub1+getsub2+getsub3+getsub4+getsub5
        print("Total : ",gettot)
        getper=gettot/5
        print("Percentage : ",getper)
#print area and perimeter of triangle using class and functions
#class triangle():
    def triangle():
        getareaheight=int(input("Height:"))
        getareabreadth=int(input("Breadth:"))
        print("Area formula: (Height*Breadth)/2")
        getaretri=(getareaheight*getareabreadth)/2
        print("Area of Triangle: ",getaretri)
        getperiheight1=int(input("Height1:"))
        getperiheight2=int(input("Height2:"))
        getperibreadth=int(input("Breadth:"))
        print("Perimeter formula: Height1+Height2+Breadth")
        getpertri=getperiheight1+getperiheight2+getperibreadth
        print("Perimeter of Triangle:",getpertri)