from datetime import date

from fines import fine_for
from loaned_item import LoanedItem


class FineApplication:
    def __init__(self, get_items, today, write):
        self.get_items = get_items
        self.today = today
        self.write = write

    def run(self):
        items = self.get_items()

        self.write(f"Today is: {self.today()}")
        self.write("")
        self.write("Fines due:")
        self.write("")

        self.write("Title,Due date,Fine")

        for item in items:
            fine = fine_for(item, self.today)

            self.write(f"{item.title},{item.due_date},{fine}")


if __name__ == "__main__":
    items = [
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

    print(f"Today is: {date.today()}")
    print()
    print("Fines due: ")
    print()

    print("Title,Due date,Fine")

    for item in items:
        fine = fine_for(item, date.today)

        print(f"{item.title},{item.due_date},{fine}")
