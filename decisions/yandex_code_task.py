"""
A module with task decisions to be a mentor at Yandex.Praktikum.
"""

def only_in_first_list(first_list, second_list):
	"""
	Returns a set with elements only in the first list but not in the second.

	:param List first_list: A first list.
	:param List second_list: A second list.
	"""
	return set(first_list) - set(second_list)


def remove_nulls_from_list(l):
	"""
	A function deletes nulls from a list using only O(1) additional memory.

	:param List l: A source list.
	"""
	pos = 0
	len_l = len(l)
	for i in range(len_l):
		if l[i] != 0:
			l[pos] = l[i]
			pos += 1
	for i in range(0, len_l - pos):
		l.pop()
	return l


