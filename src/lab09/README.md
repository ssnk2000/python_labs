### Задание 1
``` python
import csv
from pathlib import Path
import sys

sys.path.append('/Users/adelina/python_labs/src/lab08')
from numA import Student

class Group:
    HEADER = ["fio", "birthdate", "group", "gpa"]

    def __init__(self, storage_path):
        self.path = Path(storage_path)
        self._ensure_storage_exists()

    def _ensure_storage_exists(self):
        if not self.path.exists() or self.path.stat().st_size == 0:
            with self.path.open("w", encoding="utf-8", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(self.HEADER)

    def _read_all(self):
        rows = []
        with self.path.open("r", encoding="utf-8", newline="") as f:
            reader = csv.DictReader(f)
            if reader.fieldnames != self.HEADER:
                raise ValueError()
            for row in reader:

                try:
                    row['gpa'] = float(row['gpa'])
                except (ValueError, TypeError):
                    raise ValueError(f"Invalid GPA value: {row['gpa']}")
                
                Student(**row)  
                rows.append(row)
        return rows

    def _write_all(self, rows):
        with self.path.open("w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=self.HEADER)
            writer.writeheader()
            writer.writerows(rows)

    def is_empty(self):
        return len(self._read_all()) == 0

    def list(self):
        rows = self._read_all()
        return [Student(**r) for r in rows]

    def add(self, student):
        rows = self._read_all()
        rows.append({
            "fio": student.fio,
            "birthdate": student.birthdate,
            "group": student.group,
            "gpa": str(student.gpa)
        })
        self._write_all(rows)

    def find(self, substr):
        substr = substr.lower()
        rows = self._read_all()
        return [Student(**r) for r in rows if substr in r["fio"].lower()]

    def remove(self, fio):
        rows = self._read_all()
        new_rows = [r for r in rows if r["fio"] != fio]
        self._write_all(new_rows)

    def update(self, fio, **fields):
        rows = self._read_all()
        for r in rows:
            if r["fio"] == fio:
                for k, v in fields.items():
                    if k in self.HEADER:
                        r[k] = v
                Student(**r)  
        self._write_all(rows)

    def stats(self):
        rows = self._read_all()
        if not rows:
            return {"count": 0, "average_gpa": 0, "top_5_students": []}
        gpas = [float(r["gpa"]) for r in rows]
        sorted_rows = sorted(rows, key=lambda x: float(x["gpa"]), reverse=True)
        return {
            "count": len(rows),
            "average_gpa": round(sum(gpas) / len(gpas), 2),
            "top_5_students": sorted_rows[:5]
        }

if __name__ == "__main__":
    import os
    
    project_root = "/Users/adelina/python_labs"
    os.chdir(project_root)
    csv_path = "data/lab09/students.csv"
    os.makedirs("data/lab09", exist_ok=True)
    if os.path.exists(csv_path):
        os.remove(csv_path)
    
    group = Group(csv_path)


    group.add(Student("Иванов Иван", "2007-10-31", "БИВТ-25-1", 4.5))
    group.add(Student("Викторова Виктория", "2006-07-13", "БИВТ-25-2", 3.0))
    group.add(Student("Васильев Василий", "2005-02-06", "БИВТ-25-3", 4.5))
    
    print("Список студентов:")
    for s in group.list():
        print(f"    {s}")
    
    print("Поиск студента: Иванов")
    for s in group.find("Иванов"):
        print(f"    {s}")
    
    print("Обновление данных студента: Викторова Виктория, gpa=3.0 -> gpa=4.0")
    group.update("Викторова Виктория", gpa=4.0)
    print(f"    Результат:\n        {group.find('Викторова')[0]}")
    
    print("Удаление студента из списка: Васильев Василий")
    group.remove("Васильев Василий")
    print(f"    Кол-во оставшихся студентов: {len(group.list())}")
    
    print(f"Файл со списком: {csv_path}")
```
<img width="385" height="88" alt="Снимок экрана 2025-12-17 в 12 38 10" src="https://github.com/user-attachments/assets/c95c35e2-922b-4845-8342-e4b1f0c11281" />
![2025-12-17 12 38 02](https://github.com/user-attachments/assets/36021e3e-8e70-4cf2-88b0-20f862f5c4ff)
