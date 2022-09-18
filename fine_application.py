from datetime import date

from fines import fine_for
from loaned_item import LoanedItem


class FineApplication:
    def __init__(self, get_items, today, write_line):
        self.get_items = get_items
        self.today = today
        self.write_line = write_line

    def run(self):
        items = self.get_items()

        self.write_line(f"Today is: {self.today()}")
        self.write_line("")
        self.write_line("Fines due:")
        self.write_line("")

        self.write_line("Title,Due date,Fine")

        for item in items:
            fine = fine_for(item, self.today)

            self.write_line(f"{item.title},{item.due_date},{fine}")


def get_items():
    return [
        LoanedItem(
            title="Clean Code",
            author="Robert C. Martin",
            due_date=date(year=2022, month=9, day=1)
        ),
        LoanedItem(
            title="Test-Driven Development: By Example",
            author="Kent Beck",
            due_date=date(year=2022, month=10, day=5)
        )
    ]


if __name__ == "__main__":
    FineApplication(get_items, date.today, print).run()
