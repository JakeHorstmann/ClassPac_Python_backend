from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.associationproxy import association_proxy

from backend.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    first_name = Column(String(32))
    last_name = Column(String(32))
    email = Column(String(256), unique=True, index=True)
    password = Column(String(128))

    classrooms = relationship("ClassroomUserAssociation",  back_populates="user")


class Classroom(Base):
    __tablename__ = "classrooms"

    id = Column(Integer, primary_key=True)
    title = Column(String(100), index=True)
    description = Column(String(250), index=True)

    users = relationship("ClassroomUserAssociation", back_populates="classroom")


class ClassroomUserAssociation(Base):
    __tablename__ = "classroom_users"

    user_id = Column("user_id", ForeignKey("users.id"), primary_key=True)
    classroom_id = Column("classroom_id", ForeignKey("classrooms.id"), primary_key=True)
    is_teacher = Column("is_teacher", Boolean, nullable=False)

    user = relationship("User", back_populates="classrooms")
    classroom = relationship("Classroom", back_populates="users")

    # proxies
    title = association_proxy(target_collection='classroom', attr='title')
    description = association_proxy(target_collection='classroom', attr='description')
    first_name = association_proxy(target_collection='user', attr='first_name')
    last_name = association_proxy(target_collection='user', attr='last_name')
    email = association_proxy(target_collection='user', attr='email')

