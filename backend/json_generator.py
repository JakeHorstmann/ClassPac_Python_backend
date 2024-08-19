import os
from json import dump

def generate_user_json():
    first_names = ["Jake", "Dan", "Elizabeth", "Alex", "Kate"]
    last_names = ["Smith", "Rocker", "Flowers", "Trebeck", "Lynch"]
    first_last = zip(first_names, last_names)

    emails = [f"{fn}{ln[0]}@gmail.com" for fn, ln in first_last]

    json = {}
    for user in range(len(first_names)):
        json_obj = {
            "email":emails[user],
            "first_name":first_names[user],
            "last_name":last_names[user]
        }
        json[str(user + 1)] = json_obj

    return json

def generate_classroom_json():
    classroom_titles = ["Intro to Python", "Intermediate Fly Fishing", "Quantum Physics",]
    classroom_descriptions = ["Learn Python through introductary projects based on real world applications",
                              "Learn advanced fly fishing techniques on the river",
                              "Discover how quantum particles behave",]

    json = {}
    for classroom in range(len(classroom_titles)):
        json_obj = {
            "title":classroom_titles[classroom],
            "description":classroom_descriptions[classroom]
        }
        json[str(classroom + 1)] = json_obj
    
    return json

def generate_classroom_user_json():
    classroom_ids = [1, 2, 3]
    user_ids = [[1,2,3,4,5], [1,4,5], [1,2]]
    teacher_ids = [4, 5, -1]

    json = {}
    counter = 1
    for relationship in range(len(classroom_ids)):
        classroom = classroom_ids[relationship]
        users = user_ids[relationship]
        teacher = teacher_ids[relationship]
        for user in users:
            json_obj = {
                "classroom_id":classroom,
                "user_id":user,
                "is_teacher":user == teacher
            }
            json[str(counter)] = json_obj
            counter += 1

    return json

def generate_json_fixtures():
    user_json = generate_user_json()
    classroom_json = generate_classroom_json()
    classroom_user_json = generate_classroom_user_json()

    ROOT_DIR = os.path.dirname(__file__)
    FIXTURES_DIR = os.path.join(ROOT_DIR, "fixtures")

    output_files = ["users.json", "classrooms.json", "classroom_users.json"]
    json = [user_json, classroom_json, classroom_user_json]

    for i in range(len(output_files)):
        filename = output_files[i]
        json_data = json[i]
        with open(os.path.join(FIXTURES_DIR, filename), "w") as file:
            dump(json_data, file, indent=4)
    
generate_json_fixtures()
