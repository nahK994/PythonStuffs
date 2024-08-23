from pydantic import BaseModel, EmailStr, field_validator

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
print(base_user)
print(base_user.model_dump())
user = User(user=base_user, title="SE", age=18)
print(user)
print(user.model_dump())