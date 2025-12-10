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