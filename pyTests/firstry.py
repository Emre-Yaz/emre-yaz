def SquareOf_Num(a):
    return a*a
list_numbers = (5, 10, 15, 20)
result = map(SquareOf_Num, list_numbers)
print(result)
#map object to a set conversion
Square_numbers = set(result)
print(Square_numbers)


