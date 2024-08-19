from pydantic import BaseModel


class ClassroomBase(BaseModel):
    title: str
    description: str | None = None

class UserBase(BaseModel):
    email: str
    first_name: str
    last_name: str

class ClassroomUserBase(UserBase):
    is_teacher: bool

class ClassroomCreate(ClassroomBase):
    pass


class Classroom(BaseModel):
    id: int
    title: str
    description: str | None = None

    users: list[ClassroomUserBase] = []

class ClassroomUserData(BaseModel):
    classroom_id: int

class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    first_name: str
    last_name: str
    email: str
    classrooms: list[ClassroomUserData] = []
