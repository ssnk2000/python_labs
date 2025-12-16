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