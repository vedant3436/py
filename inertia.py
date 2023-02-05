'''
Using the parallel-axis theorem, determine the product of inertia of the area shown with respect to the centroidal x and y axes

diagram image : https://media.discordapp.net/attachments/810747684847091732/1069660049095528458/image.png

'''

length_of_centre_rect = int(input("Enter the length of the central rectangle: "))
breadth_of_centre_rect = int(input("Enter the breadth of the central rectangle: "))

#empty list for collection of values of Ixx of different rectangles
ixx = []

#function to calculate Ixx of rectangle
def Ixx(l, b):
    area = l*b
    perp_distx = b/2-(b*(1/4))-(breadth_of_centre_rect/2)
    perp_disty = l/2+(length_of_centre_rect/2)
    I_xx = area*(perp_distx*perp_disty)
    ixx.append(I_xx)


len1 = int(input("Enter the Length of the rectangle on the left side: "))
bred1 = int(input("Enter the Breadth of the rectangle on the left side: "))

len2 = int(input("Enter the Length of the rectangle on the right side: "))
bred2 = int(input("Enter the Breadth of the rectangle on the right side: "))

Ixx(len1, bred1)
Ixx(len2, bred2)

print(ixx)

print(f"{(-1)*sum(ixx)} is the product of inertia.")
