from datetime import date

from fines import fine_for
from loaned_item import LoanedItem


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
    print(f"{item.title},{item.due_date},{fine_for(item)}")
