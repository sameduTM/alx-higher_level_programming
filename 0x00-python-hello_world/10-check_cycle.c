#include "lists.h"
/**
 * check_cycle - tests if singly linked list has a cycle
 * @list: list to test
 *
 * Return: 1 if list has a cycle, 0 if not
 */
int check_cycle(listint_t *list)
{
	listint_t *hdd = list;
	listint_t *ssd = list;

	if (!list)
		return (0);
	
	while (hdd && ssd && ssd->next)
	{
		hdd = hdd->next;
		ssd = ssd->next->next;
		if (hdd == ssd)
			return (1);
	}

	return (0);
}
