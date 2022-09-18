from datetime import date
import unittest

from fines import fine_for
from loaned_item import LoanedItem


def today():
    return date(year=2022, month=9, day=17)


class TestFineFor(unittest.TestCase):
    def test_the_fine_is_zero_if_the_due_date_is_today(self):
        item = LoanedItem(
            title="Refactoring",
            author="Martin Fowler",
            due_date=date(year=2022, month=9, day=17)
        )

        fine = fine_for(item, today)

        self.assertEqual(fine, 0)

    def test_the_fine_is_zero_if_the_due_date_is_after_today(self):
        item = LoanedItem(
            title="97 Things Every Programmer Should Know",
            author="Kevlin Henney",
            due_date=date(year=2022, month=9, day=18)
        )

        fine = fine_for(item, today)

        self.assertEqual(fine, 0)

    def test_the_fine_is_one_for_each_day_overdue(self):
        item = LoanedItem(
            title="Working Effectively with Legacy Code",
            author="Michael Feathers",
            due_date=date(year=2022, month=9, day=15)
        )

        fine = fine_for(item, today)

        self.assertEqual(fine, 2)


if __name__ == "__main__":
    unittest.main()
