from pydantic import BaseModel, EmailStr, field_validator
from typing import List

class BaseUser(BaseModel):
    name: str
    email: EmailStr
    account_id: int

    @field_validator("account_id")
    def validate_data(cls, value):
        if value <= 0:
            raise ValueError(f"Account nunmber must be positive: {value}")
        return value


class User(BaseModel):
    user: BaseUser
    title: str
    age: int

    @field_validator("age")
    def validate(cls, value):
        if value < 18:
            raise ValueError("Age cannot be less than 18")
        return value


base_user = BaseUser(name="Shomi Khan", email="nkskl6@gmail.com", account_id=6489)
base_user2 = BaseUser(name="SKhan", email="shomipython@gmail.com", account_id=8964)

user = User(user=base_user, title="SE", age=18)
user2 = User(user=base_user2, title="HaHa", age=21)

users: List[User] = []
users.append(user)
users.append(user2)


print(f"User1 ==> {user.model_dump()}\n")
print(f"User2 ==> {user2.model_dump()}\n")
print(f"User list ==> {users}\n")
