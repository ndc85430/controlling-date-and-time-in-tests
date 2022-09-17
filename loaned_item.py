from dataclasses import dataclass
from datetime import date


@dataclass
class LoanedItem:
    title: str
    author: str
    due_date: date
