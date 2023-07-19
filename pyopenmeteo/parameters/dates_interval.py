from pydantic import root_validator, BaseModel
from datetime import date


class DatesInterval(BaseModel):
    start: date
    end: date

    @root_validator
    def validate_interval(cls, values):
        start, end = values.get("start"), values.get("end")
        if end < start:
            raise ValueError(
                f"Incorrect dates passed to class DatesInterval constructor! "
                f"Latter date cannot preceed the former date as is the case now with "
                f"start date {start.strftime('%Y-%m-%d')} and end date {end.strftime('%Y-%m-%d')}"
            )
        return values
