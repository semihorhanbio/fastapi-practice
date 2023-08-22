from pydantic import BaseModel, ValidationError
from datetime import date
from enum import Enum


class Gender(str, Enum):
    MALE = "MALE"
    FEMALE = "FEMALE"
    NON_BINARY = "NON_BINARY"


class Address(BaseModel):
    street_address: str
    postal_code: str
    city: str
    country: str


class Person(BaseModel):
    first_name: str
    last_name: str
    age: int
    gender: Gender
    birthdate: date
    interests: list[str]
    address: Address


try:
    person = Person(
        first_name="John",
        last_name="Doe",
        age=12,
        gender="MALE",
        birthdate="1991-01-01",
        interests=["travel", "sports"],
        address={
            "street_address": "12 Squirell Street",
            "postal_code": "424242",
            "city": "Woodtown",
            "country": "US",
        },
    )
    print(person)
except ValidationError as e:
    print(str(e))
