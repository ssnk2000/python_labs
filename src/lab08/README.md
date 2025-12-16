### Задание 1
``` python
from datetime import datetime, date
from dataclasses import dataclass
from typing import Dict, Any

@dataclass
class Student:
    fio: str
    birthdate: str
    group: str 
    gpa: float

    def __post_init__(self):
        try:
            datetime.strptime(self.birthdate, "%Y-%m-%d")
        except ValueError:
            raise ValueError(f"Неверный формат даты. Ожидается YYYY-MM-DD")
        
        if not (0 <= self.gpa <= 5):
            raise ValueError(f"GPA должен быть в диапазоне от 0.0 до 5.0")
        
    def age(self) -> int:
        birth = datetime.strptime(self.birthdate, "%Y-%m-%d").date()
        today = date.today()
        years = today.year - birth.year
        if (today.month, today.day) < (birth.month, birth.day):
            years -= 1
        return years
    
    def to_dict(self) -> dict:
        return {
            "fio": self.fio,
            "birthdate": self.birthdate,
            "group": self.group,
            "gpa": self.gpa
        }
    

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Student":
        return cls(**data)
    
    def __str__(self):
        return f"студент: {self.fio}, группа: {self.group}, возраст: {self.age()}, GPA: {self.gpa}"
```


### Задание 2
``` python
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
```
![2025-12-16 23 05 05](https://github.com/user-attachments/assets/6911f881-9520-43d4-ac59-6e510f75a00d)
<img width="383" height="502" alt="Снимок экрана 2025-12-16 в 23 06 25" src="https://github.com/user-attachments/assets/47166548-a985-48dc-bebf-96e2cb1faf7b" />
<img width="384" height="506" alt="Снимок экрана 2025-12-16 в 23 07 31" src="https://github.com/user-attachments/assets/0354eb73-e423-4589-ab53-4660085b3f93" />
