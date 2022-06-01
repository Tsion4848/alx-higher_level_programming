#include "lists.h"
#include <stdlib.h>
/**
 * insert_node - inserts a number
 * @head: address of the head pointer
 * @number: the number to be inserted
 *
 * Return: inserted node or null
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head;
	listint_t nnode = malloc(sizeof(listint_t));

	if (!nnode)
		return (NULL);

	nnode-> = number;
	nnode->next = NULL;

	if (!node || nnode->n < node->)
	{
		nnode->next = node;
		return (*head = nnode);
	}

	while (node)
	{
		if (!node->next || nnode->n < nnode->next->n)
		{
			nnode->next = node->next;
			node->next = nnode;
			return (node);
		}
		node = node->next
	}
	return (NULL);
}
