#include <stdio.h>
#include <Python.h>

/**
 * print_python_list_info -  Entry Point
 * Description: Prints basic info about Python lists.
 * @p: A PyObject list.
 */

void print_python_list_info(PyObject *p)
{
	int size, alloc, i;
	PyObject *item;
	
	size = PyList_Size(p);
	alloc = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", alloc);
	
	for (i = 0; i < size; i++)
	{
		printf("Element %d: ", i);

		item = PyList_GetItem(p, i);
		printf("%s\n", Py_TYPE(item)->tp_name);
	}
}
