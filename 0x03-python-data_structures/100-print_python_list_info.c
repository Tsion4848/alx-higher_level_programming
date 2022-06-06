#include <python.h>
#include <stdio.h>
/**
 * print_python_list_info(pyobject *p)
 * p: pointer to python structure
 *
 */
void print_python_list_info(PyObject *p)
{
	unsigned int i;

	printf("[*] Size of the python List = %lu\n", Py_Size(p));
	printf("[*] Allocated = %lu\n", ((pyListObject *)p)->allocated);

	for (i = 0; i < PyList_Size(p); i++)
		printf("Element %d: %s\n", i, Py_TYPE(PyList_GetItem(p, i))->tp_name);
}
