### Задание 1
``` python
from pathlib import Path
import csv
from typing import Iterable, Sequence

def read_text(path: str | Path, encoding: str = "utf-8") -> str:

    """
    Открыть файл на чтение в указанной кодировке и вернуть содержимое как одну строку.
    Если файл не найден — FileNotFoundError.
    Если кодировка не подходит — UnicodeDecodeError.
    path: путь к файлу.
    encoding: кодировка файла (по умолчанию "utf-8")
        изменить кодировку: encoding="cp1251"
    """

    p = Path(path)
    # FileNotFoundError и UnicodeDecodeError пусть «всплывают» — это нормально
    return p.read_text(encoding=encoding)

def write_csv(rows: Iterable[Sequence], path: str | Path, header: tuple[str, ...] | None = None) -> None:

    """
    Создать/перезаписать CSV с разделителем ','.
    header будет записан первой строкой.
    Проверка на одинаковую длину строк (иначе ValueError).
    """

    p = Path(path)
    rows = list(rows)

    if rows:
        row_length = len(rows[0])
        for row in rows:
            if len(row) != row_length:
                raise ValueError("Все строки должны иметь одинаковую длину.")
    
    with p.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if header is not None:
            w.writerow(header)
        for r in rows:
            w.writerow(r)

def ensure_parent_dir(path: str | Path) -> None:
    """Создать родительские директории, если их нет."""
    Path(path).parent.mkdir(parents=True, exist_ok=True)

if __name__ == "__main__":
    
    from num1 import read_text, write_csv
    write_csv([("word", "count"), ("test", 3)], "data/result.csv")
    try:
        txt = read_text("data/lab04/input.txt")
        print("Файл успешно прочитан")
    except FileNotFoundError:
        print("Файл input.txt не найден")
    except UnicodeDecodeError:
        print("Ошибка кодировки при чтении файла")
```
<img width="318" height="131" alt="Снимок экрана 2025-11-18 в 22 28 49" src="https://github.com/user-attachments/assets/85c8a5ae-fed5-48c7-bcdf-892842a71e86" />

<img width="394" height="119" alt="Снимок экрана 2025-11-18 в 22 31 05" src="https://github.com/user-attachments/assets/e8caafa6-d5c4-4ebf-af5d-98e715b2d6a1" />

<img width="251" height="126" alt="Снимок экрана 2025-11-18 в 22 55 02" src="https://github.com/user-attachments/assets/16ee3635-f6b7-4613-87da-cc151462fc21" />

### Задание 2
``` python
import argparse
import sys
from pathlib import Path

from num1 import read_text, write_csv
from lib.text import normalize, tokenize, count_freq, top_n

def create_report(input_path: str, output_path: str, encoding: str = "utf-8") -> None:

    """
    Читает входной файл data/lab04/input.txt
    Нормализует, токенизирует и считает частоты слов, используя функции из ЛР3 (lib/text.py)
    Сохраняет data/report.csv c колонками: word,count (отсортированными: count ↓, слово ↑)
    В консоль печатает:
        - кол-во всех слов
        - кол-во уникальных слов
        - топ-5 слов

    Примеры запуска:
        python src/lab04/text_report.py
        python src/lab04/text_report.py --in data/lab04/input.txt --out data/output.csv
        python src/lab04/text_report.py --in data/lab04/input.txt --encoding cp1251

    Если data/input.txt не существует → print() и sys.exit(1)
    Пустой вход → report.csv будет содержать только заголовок.
    Нестандартная кодировка → укажите, как передать --encoding cp1251.
    """

    try:
        text = read_text(input_path, encoding)
    except FileNotFoundError:
        print(f"Ошибка: файл {input_path} не найден.")
        sys.exit(1)
    except UnicodeDecodeError as e:
        print(f"Ошибка: укажите другую кодировку.")
        sys.exit(1)

    normalized_text = normalize(text)
    tokens = tokenize(normalized_text)
    freq = count_freq(tokens)
    total_words = len(tokens)
    unique_words = len(set(tokens))
    top5 = top_n(freq, 5)

    sorted_data = sorted(freq.items(), key=lambda item: (-item[1], item[0]))
    header = ("word", "count")

    write_csv(sorted_data, output_path, header)
    print(f"Всего слов: {total_words}")
    print(f"Уникальных слов: {unique_words}")
    print("Топ-5:")
    for word, count in top5:
        print(f"{word}: {count}")

def main():
    parser = argparse.ArgumentParser(description="Отчёт о частоте слов из текстового файла.")
    parser.add_argument("--in", dest="input_file", help="Путь к входному текстовому файлу.", default="data/lab04/input.txt")
    parser.add_argument("--out", dest="output_file", help="Путь к выходному CSV файлу.", default="data/lab04/report.csv")
    parser.add_argument("--encoding", default="utf-8", )
    args = parser.parse_args()
    create_report(args.input_file, args.output_file, args.encoding)

if __name__ == "__main__":
    main()
```
<img width="889" height="104" alt="Снимок экрана 2025-11-19 в 11 05 22" src="https://github.com/user-attachments/assets/6f165912-78e6-4ef0-9aed-96d708f76167" />
