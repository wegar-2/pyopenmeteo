import pydantic as pdc


class GpsPosition(pdc.BaseModel):
    latitude: float
    longitude: float
    name: str

    @pdc.validator("latitude")
    def validate_latitude(cls, value):
        if value > 90 or value < -90:
            raise ValueError(
                f"Invalid latitude passed to class {cls.__class__.__name__}; "
                f"only values between -90 and 90 are allowed! Received value {value:.2f}"
            )
        return round(value, 2)

    @pdc.validator("longitude")
    def validate_longitude(cls, value):
        if value > 180 or value < -180:
            raise ValueError(
                f"Invalid longitude passed to class {cls.__class__.__name__}; "
                f"only values between -180 and 180 are allowed! Received value {value:.2f}"
            )
        return round(value, 2)

    @pdc.validator("name")
    def validate_name(cls, value):
        if not isinstance(value, str):
            raise ValueError("Value of the parameter name is not a string! ")
        return value
