from datetime import date
import unittest

from fine_application import FineApplication
from loaned_item import LoanedItem


def get_items():
    return [
        LoanedItem(
            title="Growing Object Oriented Software Guided By Tests",
            author="Nat Pryce and Steve Freeman",
            due_date=date(year=2022, month=10, day=14)
        )
    ]


def today():
    return date(year=2022, month=10, day=1)


def write(line):
    write._output += f"{line}\n"

write._output = ""

class TestFineApplication(unittest.TestCase):
    def test_it_produces_a_report_of_the_fines_due(self):
        FineApplication(get_items, today, write).run()

        self.assertEqual(
            write._output,
            """Today is: 2022-10-01
            |
            |Fines due:
            |
            |Title,Due date,Fine
            |Growing Object Oriented Software Guided By Tests,2022-10-14,0
            |""".replace("            |", "")
        )


if __name__ == "__main__":
    unittest.main()
