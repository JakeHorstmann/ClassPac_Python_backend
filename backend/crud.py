from sqlalchemy.orm import Session

from . import models, schemas


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(email=user.email, first_name=user.first_name, last_name=user.last_name)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_classroom(db: Session, classroom_id: int):
    return db.query(models.Classroom).filter(models.Classroom.id == classroom_id).first()

def get_classroom_by_title(db: Session, classroom_title: str):
    return db.query(models.Classroom).filter(models.Classroom.title == classroom_title).first()

def get_classrooms(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Classroom).offset(skip).limit(limit).all()

def create_classroom(db: Session, classroom: schemas.ClassroomCreate):
    db_classroom = models.Classroom(**classroom.model_dump())
    db.add(db_classroom)
    db.commit()
    db.refresh(db_classroom)
    return db_classroom

def add_user_to_classroom(db: Session, classroom_id: int, user_id: int, is_teacher: int):
    association = models.ClassroomUserAssociation(
        classroom_id=classroom_id,
        user_id=user_id,
        is_teacher=is_teacher
    )
    db.add(association)
    db.commit()
    db.refresh(association)
    return association

def get_user_classroom_association(db: Session, classroom_id: int, user_id: int):
    return db.query(models.ClassroomUserAssociation).filter(
        models.ClassroomUserAssociation.classroom_id == classroom_id,
        models.ClassroomUserAssociation.user_id == user_id
        ).first()