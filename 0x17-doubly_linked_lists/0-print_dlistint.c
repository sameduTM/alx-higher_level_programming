#include <stdio.h>
#include "lists.h"
/**
 * print_dlistint - Prints all element of doubly list
 * @h: Pointer to head of doubly list
 *
 * Return: Number of nodes in list
 */
size_t print_dlistint(const dlistint_t *h)
{
	size_t node_count = 0;

	while (h != NULL)
	{
		printf("%d\n", h->n);
		h = h->next;
		node_count++;
	}

	return (node_count);
}
