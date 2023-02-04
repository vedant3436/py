'''
Using the parallel-axis theorem, determine the moment of inertia of figure

diagram image : https://media.discordapp.net/attachments/810747684847091732/1069660049095528458/image.png

'''

#empty lists
arealist = []
aixi = []
aiyi = []
ixx = []
iyy = [] 

#function to calculate and store areas of rectangles
def area(l, b):
    arealist.append(l*b)

#function to calculate Ixx of rectangles
def sum_ixx(l, b):
    i_xx = (l*b*b*b)/12
    ixx.append(i_xx)

#function to calculate Iyy of rectangles
def sum_iyy(b, l):
    i_yy = (b*l*l*l)/12
    iyy.append(i_yy)

length_of_centre_rect = int(input("Enter the length of the central rectangle: "))
breadth_of_centre_rect = int(input("Enter the breadth of the central rectangle: "))    

len1 = int(input("Enter the Length of the rectangle on the left side: "))
bred1 = int(input("Enter the Breadth of the rectangle on the left side: "))

len2 = int(input("Enter the Length of the rectangle on the right side: "))
bred2 = int(input("Enter the Breadth of the rectangle on the right side: "))

area(length_of_centre_rect,breadth_of_centre_rect)
area(len1, bred1)
area(len2, bred2)

sum_ixx(length_of_centre_rect,breadth_of_centre_rect)
sum_ixx(len1, bred1)
sum_ixx(len2, bred2)

sum_iyy(breadth_of_centre_rect,length_of_centre_rect)
sum_iyy(bred1,len1)
sum_iyy(bred2,len2)

#calculations for centroids of the rectangles
x_rect1, y_rect1 = (length_of_centre_rect/2)+len1, ((bred1*3/4)-(breadth_of_centre_rect/2))+(breadth_of_centre_rect/2)
x_rect2, y_rect2 = len1/2, (bred2/2)+(bred1/2)
x_rect3, y_rect3 = (len1)+(length_of_centre_rect)+(len2/2), bred2/2

#to find AiXi and AiYi and X and Y centroid for overall figure
aixi.extend([arealist[0]*x_rect1,arealist[1]*x_rect2,arealist[2]*x_rect3])
aiyi.extend([arealist[0]*y_rect1,arealist[1]*y_rect2,arealist[2]*y_rect3])
x_bar, y_bar = (sum(aixi))/(sum(arealist)), (sum(aiyi))/(sum(arealist))

#to calculate Area*(Yi-Y)^2
a_x_x = (arealist[0]*((x_rect1-x_bar)*(x_rect1-x_bar)))+(arealist[1]*((x_rect2-x_bar)*(x_rect2-x_bar)))+(arealist[2]*((x_rect3-x_bar)*(x_rect3-x_bar)))
a_y_y = (arealist[0]*((y_rect1-y_bar)*(y_rect1-y_bar)))+(arealist[1]*((y_rect2-y_bar)*(y_rect2-y_bar)))+(arealist[2]*((y_rect3-y_bar)*(y_rect3-y_bar)))

print(f"Ixx is: {a_y_y+sum(ixx)} \nIyy is: {a_x_x+sum(iyy)}")


