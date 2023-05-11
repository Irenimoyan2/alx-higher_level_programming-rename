#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"

/**
 * check_cycle - Entry Point 
 * Description: Checks if a singly-linked list contains a cycle.
 * @list: Type list
 * Return: If there is no cycle - 0.
 *         If there is a cycle - 1
 */
int check_cycle(listint_t *head)
{
	int *p1, *p2;

	if (head == NULL)
		return (0);

	while (head != NULL)
	{
		p1 = (int *)&head;
		p2 = (int *)&head->next;
		if (head->next == NULL)
			return (0);

		if (*p1 - *p2 <= 0)
			return (1);

		head = head->next;
	}
	return (0);
}
