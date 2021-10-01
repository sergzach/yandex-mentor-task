"""
Tests for a module with task decisions.
"""

import pytest
from yandex_code_task import only_in_first_list, remove_nulls_from_list


@pytest.mark.parametrize(
	'first_list, second_list, result_set',
	(
		(
			[0, 2, 5, 6, 7],
			[2, 5, 7, 0],
			{6}
		),
		(
			[100, 120, 301, -98, 'one', 'one'],
			['one', 301, 'two'],
			{100, 120, -98}
		),
	)
)
def test_only_in_first_list(first_list, second_list, result_set):
	"""
	The test for only_in_first_list().

	:param List first_list: A first list.
	:param List second_list: A list which elements must not be in answer.
	:param Set result_set: A result of only_in_first_list().
	"""
	assert only_in_first_list(first_list, second_list) == result_set


@pytest.mark.parametrize(
	'source_list, result_list',
	(
		(
			[0, 1, 0, 0, 4, 5, 6, 7, 0, 8, -4, 0],
			[1, 4, 5, 6, 7, 8, -4]
		),
		(
			[0, 34, -24, 35, 45, -64, 0, 60, 100, -100, 0, 0, 0],
			[34, -24, 35, 45, -64, 60, 100, -100]
		),
	)
)
def test_remove_nulls_from_list(source_list, result_list):
	"""
	The test for remove_nulls_from_list().

	:param List source_list: A source list (probably with nulls).
	:param List result_list: A checking result list.
	"""
	assert remove_nulls_from_list(source_list) == result_list