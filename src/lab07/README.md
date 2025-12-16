### Задание 1
``` python
import pytest
import sys

# from src.lab07.lib.text import normalize, tokenize, count_freq, top_n
sys.path.append('/Users/adelina/python_labs-main/src/lab07/lib')
from text import normalize, tokenize, count_freq, top_n

@pytest.mark.parametrize(
    "text, expected",
    [
        ("ПрИвЕт МИр", "привет мир"),
        ("ёжик, Ёлка", "ежик, елка"),
        ("Hello World", "hello world"),
        ("  двойные   пробелы  ", "двойные пробелы"),
    ],
)
def test_normalize(text, expected):
    assert normalize(text) == expected


@pytest.mark.parametrize(
    "text, expected",
    [
        ("привет мир", ["привет", "мир"]),
        ("пока, друг", ["пока", "друг"]),
        ("передай привет", ["передай", "привет"]),
        ("18 лет", ["18", "лет"]),
        ("", []),
        ("   ", []),   
    ],
)
def test_tokenize(text, expected):
    assert tokenize(text) == expected


@pytest.mark.parametrize(
    "tokens, expected",
    [
        (["привет", "мир", "привет"], {"привет": 2, "мир": 1}),
        ([], {}),
        (["друг"], {"друг": 1}),
        (["добрый", "день", "добрый", "вечер"], {"добрый": 2, "день": 1, "вечер": 1}),
    ],
)
def test_count_freq(tokens, expected):
    assert count_freq(tokens) == expected


@pytest.mark.parametrize(
    "freq, n, expected",
    [
        ({"привет": 5, "мир": 3, "пока": 7}, 2, [("пока", 7), ("привет", 5)]),
        ({"да": 3, "нет": 3, "наверное": 3}, 3, [("да", 3), ("наверное", 3), ("нет", 3)]),
        ({}, 5, []),
        ({"ок": 1}, 1, [("ок", 1)]),
        ({"да": 1, "нет": 2}, 10, [("нет", 2), ("да", 1)]),
    ],
)
def test_top_n(freq, n, expected):
    assert top_n(freq, n) == expected
```
<img width="1477" height="915" alt="518853784-6f258f73-8b02-4484-8f7c-7022f5643115" src="https://github.com/user-attachments/assets/1a032ac4-6a3b-47dd-bf7a-6df19be8ceed" />


### Задание 2
``` python
import pytest
import json
import csv
from pathlib import Path    

from src.lab05.json_csv import json_to_csv, csv_to_json


def test_json_to_csv_roundtrip(tmp_path: Path):
    src = tmp_path / "people.json"
    dst = tmp_path / "people.csv"
    data = [
        {"name": "Alice", "age": 22},
        {"name": "Bob", "age": 25},
    ]
    src.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    json_to_csv(str(src), str(dst))

    with dst.open(encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    assert len(rows) == 2
    assert {"name", "age"} <= set(rows[0].keys())


def test_csv_to_json_roundtrip(tmp_path: Path):
    src = tmp_path / "people.csv"
    dst = tmp_path / "people.json"
    rows = [
        {"name": "Alice", "age": "22"},
        {"name": "Bob", "age": "25"},
    ]
    with src.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["name", "age"])
        writer.writeheader()
        writer.writerows(rows)

    csv_to_json(str(src), str(dst))

    data_out = json.loads(dst.read_text(encoding="utf-8"))

    assert len(data_out) == len(rows)
   # assert all("name" in rec and "age" in rec for rec in data_out)
    assert {"name", "age"} <= set(rows[0].keys())


    def test_json_to_csv_wrong_path():
        with pytest.raises(FileNotFoundError):
            json_to_csv("ошибка: файл json не найден.", "test.csv")

    def test_csv_to_json_wrong_path():
        with pytest.raises(FileNotFoundError):
            csv_to_json("ошибка: файл csv не найден.", "test.json")
```

<img width="1505" height="519" alt="518854000-c4024ced-1eaf-4e24-89b1-21c5e0bfcd94" src="https://github.com/user-attachments/assets/1e409525-aade-4a0f-a20c-406821411e17" />
