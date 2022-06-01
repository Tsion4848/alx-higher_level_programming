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
	listint_t *ptrp = list;

	while (list && ptr && ptr->next)
	{
		list = list->next;
		ptr = ptr->next->next;

		if (list == ptr)
		{
			list = ptrp;
			ptrp = ptr;
			while (1)
			{
				ptr = ptrp;
				while (ptr->next != list && ptr->next != ptrp)
				{
					ptr = ptr->next;
				}
				if (ptr->next == list)
					break;

				list = list->next;
			}
			return (1);
		}
	}

	return (0);
}
