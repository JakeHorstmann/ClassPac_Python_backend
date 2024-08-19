from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/api/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)


@app.get("/api/users/", response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@app.get("/api/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user:
        return db_user
    raise HTTPException(status_code=404, detail="User not found")


@app.get("/api/classrooms/", response_model=list[schemas.Classroom])
def read_classrooms(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    classes = crud.get_classrooms(db, skip=skip, limit=limit)
    return classes

@app.get("/api/classrooms/{classroom_id}", response_model=schemas.Classroom)
def read_classroom(classroom_id: int, db: Session = Depends(get_db)):
    db_class = crud.get_classroom(db, classroom_id=classroom_id)
    if db_class:
        return db_class
    raise HTTPException(status_code=404, detail="Classroom not found")

@app.post("/api/classrooms/", response_model=schemas.ClassroomCreate)
def create_classroom(classroom: schemas.ClassroomCreate, db: Session = Depends(get_db)):
    db_classroom = crud.get_classroom_by_title(db, classroom_title=classroom.title)
    if db_classroom:
        raise HTTPException(status_code=400, detail="Classroom already exists")
    return crud.create_classroom(db=db, classroom=classroom)

@app.post("/api/classrooms/{classroom_id}/users/{user_id}")
def add_user_to_classroom(classroom_id: int, user_id: int, is_teacher: int, db: Session = Depends(get_db)):
    user = crud.get_user(db, user_id=user_id)
    classroom = crud.get_classroom(db, classroom_id=classroom_id)
    if not user:
        return HTTPException(status_code=404, detail="User not found")
    if not classroom:
        return HTTPException(status_code=404, detail="Classroom does not exist")
    association = crud.get_user_classroom_association(db, classroom_id=classroom_id, user_id=user_id)
    if association:
        return association
    return crud.add_user_to_classroom(
                db=db,
                classroom_id=classroom_id,
                user_id=user_id,
                is_teacher=is_teacher
            )