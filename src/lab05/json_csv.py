from pathlib import Path
import json
import csv

def json_to_csv(json_path: str, csv_path: str) -> None:
    """
    Преобразует JSON-файл в CSV.
    Поддерживает список словарей [{...}, {...}], заполняет отсутствующие поля пустыми строками.
    Кодировка UTF-8. Порядок колонок — как в первом объекте или алфавитный (указать в README).
    """
    json_file = Path(json_path)
    csv_file = Path(csv_path)

    if not json_file.exists():
        raise FileNotFoundError(f"JSON-файл не найден: {json_path}")
    
    with json_file.open('r', encoding='utf-8') as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError as e:
            raise ValueError(f"Ошибка чтения JSON-файла (неверный формат или пустой): {e}")
    
    for item in data:
        if not isinstance(item, dict):
            raise ValueError("Все элементы JSON должны быть словарями.")
    if not data or not isinstance(data, list):
        raise ValueError("JSON-файл пустой.")  
    
    first_keys = list(data[0].keys())
    all_unique_keys = set(first_keys)
    for item in data:
        all_unique_keys.update(item.keys())
    add_keys = sorted([k for k in all_unique_keys if k not in first_keys])
    fieldnames = first_keys + add_keys
    
    with csv_file.open('w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for item in data:
            row = {key: item.get(key, "") for key in fieldnames}
            writer.writerow(row)

json_to_csv(f"src/lab05/samples/people.json", f"src/lab05/out/people_from_json.csv")



def csv_to_json(csv_path: str, json_path: str) -> None:
    """
    Преобразует CSV в JSON (список словарей).
    Заголовок обязателен, значения сохраняются как строки.
    json.dump(..., ensure_ascii=False, indent=2)
    """
    csv_file = Path(csv_path)
    json_file = Path(json_path)

    if not csv_file.exists():
        raise FileNotFoundError(f"CSV-файл не найден: {csv_path}")
    
    with csv_file.open('r', newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        if not reader.fieldnames:
            raise ValueError("CSV-файл пуст или отсутствует заголовок.")
        json_data = list(reader)
    if not json_data:
       raise ValueError("CSV-файл пустой.")

    with json_file.open('w', encoding='utf-8') as f:
        json.dump(json_data, f, ensure_ascii=False, indent=2)
        
csv_to_json(f"src/lab05/samples/people.csv", f"src/lab05/out/people_from_csv.json")