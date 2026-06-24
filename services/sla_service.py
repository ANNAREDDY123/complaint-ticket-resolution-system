from datetime import datetime


def check_sla(priority, created_at):

    hours = (
        datetime.utcnow() -
        created_at
    ).total_seconds() / 3600

    if priority == "High":

        return hours <= 24

    elif priority == "Medium":

        return hours <= 72

    elif priority == "Low":

        return hours <= 168

    return True
