from pydantic import BaseModel

class Member(BaseModel):
    fullname: str
    birthdate: str
    hometown: str
