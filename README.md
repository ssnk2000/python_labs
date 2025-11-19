# ssnk2000
-----
## Лабораторная работа 1
-----
-----
### Задание 1
``` python
name = input('Имя: ')
age = int(input('Возраст: '))
print(f'Привет, {name}! Через год тебе будет {age+1}.')
```
<img width="447" height="224" alt="Снимок экрана 2025-09-30 в 21 00 25" src="https://github.com/user-attachments/assets/9ff630c6-f91a-47c6-bc37-5585d2181219" />

### Задание 2
``` python
n1 = input('n1: ').replace(',','.')
n2 = input('n2: ').replace(',','.')
n1 = float(n1)
n2 = float(n2)
summa = n1 + n2
avgg = summa/2
print(f'sum={summa:.2f}; avg={avgg:.2f}')
```
<img width="377" height="150" alt="Снимок экрана 2025-09-30 в 23 01 45" src="https://github.com/user-attachments/assets/90a744ed-e8f1-483c-88e0-d9b2b1d33e5d" />

### Задание 3
``` python
price = float(input('price='))
discount = float(input('discount='))
vat = float(input('vat='))
base = price * (1 - discount/100)
vat_amount = base * (vat/100)
total = base + vat_amount
print(f'База после скидки: {base:.2f} ₽')
print(f'НДС:               {vat_amount:.2f} ₽')
print(f'Итого к оплате:    {total:.2f} ₽')
```
<img width="421" height="211" alt="Снимок экрана 2025-09-30 в 23 06 25" src="https://github.com/user-attachments/assets/85293c26-74f9-467c-8576-adf5453bc4e2" />

### Задание 4
``` python
m = int(input('Минуты: '))
hours = m//60
minutes = m%60
print(f'{hours}:{minutes:02d}')
```
<img width="321" height="128" alt="Снимок экрана 2025-09-30 в 23 10 31" src="https://github.com/user-attachments/assets/b12d1488-85b1-4aa7-9c1f-89aac62baadb" />


### Задание 5
``` python
def probel(fio):
    delprob = ' '.join(fio.split())
    f_i_o = delprob.split()
    init = ''.join(part[0].upper() for part in f_i_o)
    l = len(delprob)
    return init + '.',l
fio = input('ФИО: ')
init,l = probel(fio)
print('Инициалы: ',init)
print('Длина (символов): ',l)
```
<img width="365" height="159" alt="Снимок экрана 2025-09-30 в 23 13 29" src="https://github.com/user-attachments/assets/1afe8bce-a723-48a3-91e0-0878dac56a2e" />


----------------------------

## Лабораторная работа 4
-----
-----
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
<img width="318" height="131" alt="Снимок экрана 2025-11-18 в 22 28 49" src="https://github.com/user-attachments/assets/9741098a-eaaa-4e06-b2a5-7a21896494ce" />

<img width="394" height="119" alt="Снимок экрана 2025-11-18 в 22 31 05" src="https://github.com/user-attachments/assets/1b99217f-7248-4520-b6eb-8e60abfbc9b1" />

<img width="251" height="126" alt="Снимок экрана 2025-11-18 в 22 55 02" src="https://github.com/user-attachments/assets/0c7675a5-8f63-4191-a078-b0c2696dfaca" />


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
<img width="889" height="104" alt="Снимок экрана 2025-11-19 в 11 05 22" src="https://github.com/user-attachments/assets/169a3681-a3df-4b02-b506-72d55831fab3" />
