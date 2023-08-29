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

    def name_dict(self):
        return self.model_dump(include={"first_name", "last_name"})


person = Person(
    first_name="John",
    last_name="Doe",
    age=32,
    gender=Gender.MALE,
    birthdate="1991-01-01",
    interests=["travel", "sports"],
    address={
        "street_address": "12 Squirell Street",
        "postal_code": "424242",
        "city": "Woodtown",
        "country": "US",
    },
)

person_dict = person.model_dump()
print(person_dict["first_name"])  # "John"
print(person_dict["address"]["street_address"])  # "12 Squirell Street"

person_include = person.model_dump(include={"first_name", "last_name"})
print(person_include)  # {"first_name": "John", "last_name": "Doe"}
person_exclude = person.model_dump(exclude={"birthdate", "interests"})
print(person_exclude)

person_nested_include = person.model_dump(
    include={
        "first_name": ...,
        "last_name": ...,
        "address": {"city", "country"},
    }
)
# {"first_name": "John", "last_name": "Doe", "address": {"city":"Woodtown", "country": "US"}}
print(person_nested_include)


class PostBase(BaseModel):
    title: str
    content: str


class PostCreate(PostBase):
    pass


class PostRead(PostBase):
    id: int


class Post(PostBase):
    id: int
    nb_views: int = 0


class PostPartialUpdate(BaseModel):
    title: str | None = None
    content: str | None = None


from fastapi import FastAPI, status, HTTPException

app = FastAPI()
db = {}


@app.post("/posts", status_code=status.HTTP_201_CREATED, response_model=PostRead)
async def create_post(post_create: PostCreate):
    new_id = max(db.posts.keys() or (0,)) + 1
    post = Post(id=new_id, **post_create.model_dump())
    db.posts[new_id] = post
    return post


@app.patch("/posts/{id}", response_model=PostRead)
async def partial_update(id: int, post_update: PostPartialUpdate):
    try:
        post_db = db.posts[id]
        updated_fields = post_update.model_dump(exclude_unset=True)
        updated_post = post_db.copy(update=updated_fields)
        db.posts[id] = updated_post
        return updated_post
    except KeyError:
        raise HTTPException(status.HTTP_404_NOT_FOUND)
