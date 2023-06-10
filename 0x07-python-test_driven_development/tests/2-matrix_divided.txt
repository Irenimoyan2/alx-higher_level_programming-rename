The ``2-matrix_divided.py`` module

==================================

Using ``matrix_divided``

Importing:
	>>> matrix_divided = __import__('2-matrix_divided').matrix_divided

list of list, all ints:
        >>> matrix = [[1, 2, 3], [4, 5, 6]]
	>>> print(matrix_divided(matrix, 3))
	[[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]

list of list, one -ve ints:
     	>>> matrix = [[1, -1, 3], [4, 5, 6]]
	>>> print(matrix_divided(matrix, 3))
	[[0.33, -0.33, 1.0], [1.33, 1.67, 2.0]]

list of list, one -ve list:
     	>>> matrix = [[-1, -2, -3], [4, 5, 6]]
	>>> print(matrix_divided(matrix, 3))
	[[-0.33, -0.67, -1.0], [1.33, 1.67, 2.0]]

list of list, +ve floats:
     	>>> matrix = [[1.5, 2.6, 3.4], [4, 5, 6]]
	>>> print(matrix_divided(matrix, 3))
	[[0.5, 0.87, 1.13], [1.33, 1.67, 2.0]]

list of list, +ve floats:
     	>>> matrix = [[-1.5, -2.4, -3.6], [-4.6, -5.6, -6.7]]
	>>> print(matrix_divided(matrix, 2))
	[[-0.75, -1.2, -1.8], [-2.3, -2.8, -3.35]]

list containing one non-list type, int:
     	>>> matrix = [[1.5, 2.6, 3.4], [4, 5, 6], 325]
     	>>> print(matrix_divided(matrix, 3))
	Traceback (most recent call last):
	...
	TypeError: matrix must be a matrix (list of lists) of integers/floats

list containing one non-int/float:
     	>>> matrix = [[1.5, 2.6, 3.4], [4, "string", 6]]
	>>> print(matrix_divided(matrix, 3))
	Traceback (most recent call last):
	...
	TypeError: matrix must be a matrix (list of lists) of integers/floats

list containing more than 2 lists of diff sizes:
     	>>> matrix = [[1, 2, 3], [4, 5, 6], [400, 401, 503, 500]]
	>>> print(matrix_divided(matrix, 3))
	Traceback (most recent call last):
	...
	TypeError: Each row of the matrix must have the same size

list containing more than 2 lists of same sizes:
     	>>> matrix = [[1, 2, 3], [4, 5, 6], [400, 401, 503]]
	>>> print(matrix_divided(matrix, 3))
	[[0.33, 0.67, 1.0], [1.33, 1.67, 2.0], [133.33, 133.67, 167.67]]

list containing more than 2 lists of diff sizes:(small)
     	>>> matrix = [[1, 2, 3], [4, 5, 6], [400, 401]]
	>>> print(matrix_divided(matrix, 3))
	Traceback (most recent call last):
	...
	TypeError: Each row of the matrix must have the same size

a negative divisor:
  	>>> matrix = [[1, 2, 3], [4, 5, 6]]
	>>> print(matrix_divided(matrix, -2))
	[[-0.5, -1.0, -1.5], [-2.0, -2.5, -3.0]]

a negative divisor float:
  	>>> print(matrix_divided(matrix, -2.5))
	[[-0.4, -0.8, -1.2], [-1.6, -2.0, -2.4]]

a positve divisor float:
  	>>> print(matrix_divided(matrix, 2.5))
	[[0.4, 0.8, 1.2], [1.6, 2.0, 2.4]]

div is 0:
	>>> print(matrix_divided(matrix, 0))
	Traceback (most recent call last):
	...
	ZeroDivisionError: division by zero

one arg, the first:
    	>>> print(matrix_divided(matrix))
	Traceback (most recent call last):
	...
	TypeError: matrix_divided() missing 1 required positional argument: 'div'

empty matrix:
	>>> matrix = []
	>>> print(matrix_divided(matrix, 2.5))
	[]

no arg at all:
       	>>> print(matrix_divided())
	Traceback (most recent call last):
	...
	TypeError: matrix_divided() missing 2 required positional arguments: 'matrix' and 'div'

list with diff types:
     	>>> matrix = ["string", 123, [123, "string"]]
	>>> print(matrix_divided(matrix, 2))
	Traceback (most recent call last):
	...
	TypeError: matrix must be a matrix (list of lists) of integers/floats
