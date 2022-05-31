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
	listint_t *ptr2 = list;

	if (list == NULL)
	{
		return (0);
	}

	ptr2 = ptr2->next;

	while (ptr != NULL && ptr2 != NULL && ptr2->next != NULL)
	{
		if (ptr == ptr2)
		{
			return (1);
		}
		ptr2 = ptr2->next->next;
		ptr = ptr->next;
	}
	return (0);
}
