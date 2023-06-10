The ``0-add_integer.py`` module

===============================

Using ``add_integer``


Import:
	>>> add_integer = __import__('0-add_integer').add_integer

Testing

	>>> add_integer(1, 2)
	3
	>>> add_integer(11, -2)
	9
	>>> add_integer(-3, -2)
	-5
	>>> add_integer(2.4, 4)
	6
	>>> add_integer(2.4, -4)
	-2
	>>> add_integer(-2.4, -4)
	-6
	>>> add_integer(3.0, 2.5)
	5
	>>> add_integer(-3.0, 2.5)
	-1
	>>> add_integer(-3.0, -2.5)
	-5
	>>> add_integer("wefw", -2.5)
	Traceback (most recent call last):
	...
	TypeError: a must be an integer
	>>> add_integer(0)
	98
	>>> add_integer(9)
	107
	>>> add_integer()
	Traceback (most recent call last):
	...
       	TypeError: add_integer() missing 1 required positional argument: 'a'
