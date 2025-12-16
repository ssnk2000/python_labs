import json
from numA import Student


def students_to_json(students, path):
    with open(path, "w", encoding="utf-8") as f:
        json.dump([s.to_dict() for s in students], f, ensure_ascii=False, indent=4)


def students_from_json(path) -> list[Student]:
    with open(path, "r", encoding="utf-8") as f:
       data  = json.load(f)

    result = []
    for d in data:
        result.append(Student.from_dict(d))

    return result


students = students_from_json("data/lab08/students_input.json")

for s in students:
    print(s)

students_to_json(students, "data/lab08/students_output.json")