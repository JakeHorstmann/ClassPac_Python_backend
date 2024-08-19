import os
from json import load
from sqlalchemy import insert
import time

FIXURES_DIR = os.path.join(os.path.dirname(__file__),"backend", "fixtures")
FIXTURE_FILES = ["users.json", "classrooms.json", "classroom_users.json"]

def get_json_as_dict(file):
    with open(file, "r") as f:
        data = load(f)
    return data

def load_all_data():
    from backend.database import SessionLocal, engine
    import backend.models as models
    models.Base.metadata.create_all(bind=engine)
    model_order = [models.User, models.Classroom, models.ClassroomUserAssociation]
    session = SessionLocal()
    for counter in range(len(FIXTURE_FILES)):
        filename = FIXTURE_FILES[counter]
        file = os.path.join(FIXURES_DIR, filename)
        data = list(get_json_as_dict(file).values())

        session.execute(
            insert(model_order[counter]),
            data
        )
        session.commit()

if __name__ == "__main__":
    run = input("This will wipe the database to reset it. Are you sure you want to do this? (Y/N) ").strip().lower()
    if run == "y":
        if os.path.isfile("database.db"):
            os.remove("database.db")
        load_all_data()
    elif run == "n":
        print("Operation aborted")
    else:
        print("Input not understood. Aborting")
