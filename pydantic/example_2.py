from typing import List
from pydantic import BaseModel, EmailStr
from pydantic.functional_validators import field_validator

class User(BaseModel):
    name: str
    email: EmailStr
    age: int

    @field_validator('age', mode='before')
    def validate_age(cls, value):
        if value < 0:
            raise ValueError('Age must be a positive integer')
        return value


class SoftwareEngineer(User):
    role: str = "Software Engineer"
    skills: List[str]

    @field_validator('skills')
    def uppercase_skills(cls, value):
        return [skill.upper() for skill in value]


class SQA(SoftwareEngineer):
    role: str = "Software Quality Assurance"


class DevOps(SoftwareEngineer):
    role: str = "DevOps Engineer"


class Manager(User):
    role: str = "Manager"
    team_size: int


def find_user_by_skill(users: List[User], skill: str) -> List[User]:
    result = []
    for user in users:
        if isinstance(user, SoftwareEngineer) and skill.upper() in user.skills:
            result.append(user)
    return result

if __name__ == "__main__":
    users = [
        SoftwareEngineer(name="Alice", email="alice@example.com", age=30, skills=["Python", "Django"]),
        SQA(name="Bob", email="bob@example.com", age=28, skills=["Testing", "Selenium"]),
        DevOps(name="Charlie", email="charlie@example.com", age=35, skills=["AWS", "Docker"]),
        Manager(name="David", email="david@example.com", age=40, team_size=10)
    ]

    skill_to_find = "python"
    found_users = find_user_by_skill(users, skill_to_find)

    for user in found_users:
        print(user)
