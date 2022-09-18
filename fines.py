def fine_for(item, today):
    days_overdue = (today() - item.due_date).days

    fine = 1 * days_overdue if days_overdue >= 1 else 0

    return fine
