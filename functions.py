#this is to find the perimeter of a circle pi x radius
def get_circle_perimeter(r):
  perimeter = 3.14*r
  return perimeter
#this is to find the perimeter of a circle pi x radius squared
def get_circle_area(r):
  area = 3.14*r*r
  return area
#this is to find the perimeter of a triangle 0.5 x length x height
def get_triangle_area(l,h):
  area=0.5*l*h
  return area
#this is to find the perimeter of a triangle length1 + length2 + height
def get_triangle_perimeter(l1,l2,h):
  perimeter=l1 +l2 + h
  return perimeter
#this is to find the perimeter of a square length x height
def get_rec_square_area(l,b):
  area = l * b
  return area
#this is to find the perimeter of a square 2 x (length x height)
def get_rec_square_perimeter(l,h):
  perimeter = 2*(l+h)
  return perimeter
#this is to find the perimeter of a parrallelogram length x base
def get_rec_parallelogram_area(l,b):
  area = l * b
  return area
#this is to find the perimeter of a parrallelogram 2 x (length x height)
def get_rec_parallelogram_perimeter(l,h):
  perimeter = 2*(l+h)
  return perimeter