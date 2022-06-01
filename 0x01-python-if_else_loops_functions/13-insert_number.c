#include "lists.h"

/**
 * insert_node - inserts node in sorted list
 * @head: head pointer
 * @number: the number to be inserted
 *
 * Return: inserted node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head;
	listint_t *nnode = malloc(sizeof(listint_t));

	if (!nnode)
		return (NULL);

	nnode->n = number;
	nnode->next = NULL;

	if (!node || nnode->n < node->n)
	{
		nnode->next = node;
		return (*head = nnode);
	}

	while (node)
	{
		if (!node->next || nnode->n < node->next->n)
		{
			nnode->next = node->next;
			node->next = nnode;
			return (node);
		}
		node = node->next;
	}
	return (NULL);
}
