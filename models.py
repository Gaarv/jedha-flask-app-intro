from datetime import datetime, date
from dataclasses import dataclass


@dataclass
class User:
    name: str
    surname: str
    address: str
    date_of_birth: str  # format is YYYY/MM/DD

    def age(self, at_date: str = None) -> int:
        dob = datetime.strptime(self.date_of_birth, "%Y/%m/%d")
        today = date.today() if at_date is None else datetime.strptime(at_date, "%Y/%m/%d")
        return today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
