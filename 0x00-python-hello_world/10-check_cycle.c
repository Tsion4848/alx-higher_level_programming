#include "lists.h"
/**
 * check_cycle - linked list cycle checker
 * @list: pointer to the structure
 *
 * Return: 0 if no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *ptr = list;

	if (list == NULL)
	{
		return (0);
	}

	while (list)
	{
		if (list->next == NULL)
			return (0);
		list = list->next;
		
		if (ptr->next == NULL || ptr->next->next == NULL)
			return (0);
		ptr = ptr->next;
		ptr = ptr->next;
		if (list == ptr)
			return (1);
	}
	return (0);
}
