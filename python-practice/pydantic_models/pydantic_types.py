from pydantic import BaseModel, EmailStr, HttpUrl, ValidationError


class User(BaseModel):
    email: EmailStr
    website: HttpUrl


# invalid email
try:
    User(email="jdoe", website="https://www.example.com")
except ValidationError as e:
    print(e)

# Invalid URL
try:
    User(email="jdoe@example.com", website="jdoe")
except ValidationError as e:
    print(str(e))

# Valid
user = User(email="jdoe@example.com", website="https://www.example.com")
print(user)
