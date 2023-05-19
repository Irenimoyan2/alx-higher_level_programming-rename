#include <stdio.h>
#include <Python.h>

/**
 * print_python_list_info -  Entry Point
 * Description: Prints basic info about Python lists.
 * @p: A PyObject list.
 */

void print_python_list(PyObject *p)
{
	int_size_t size;
	int_size_t i;
	
	if (!PyList_Check(p))
	{
		printf("Invalid Python list object.\n");
		return;
	}
	
	size = PyList_Size(p);
	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);
	
	for (i = 0; i < size; i++)
	{
		printf("Element %ld: %s\n", i, Py_TYPE(PyList_GetItem(p, i))->tp_name);
	}
}

void print_python_bytes(PyObject *p)
{
	int_size_t size;
	int_size_t i;
	char *bytes;
	PyObject *byte_obj;
	
	if (!PyBytes_Check(p))
	{
		printf("Invalid Python bytes object.\n");
		return;
	}
	
	size = PyBytes_Size(p);
	bytes = PyBytes_AsString(p);
	
	printf("[.] bytes object info\n");
	printf("size: %ld\n", size);
	printf("trying string: %s\n", bytes);
	
	printf("first %ld bytes: ", (size + 1 < 10 ? size + 1 : 10));
	for (i = 0; i < size + 1 && i < 10; i++)
	{
		byte_obj = PyList_GetItem(p, i);
		printf("%02hhx", PyLong_AsLong(byte_obj));
		if (i + 1 < size + 1 && i + 1 < 10)
			printf(" ");
	}
	printf("\n");
}
