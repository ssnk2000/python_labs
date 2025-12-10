### Задание 1
``` python
import argparse
import sys
from pathlib import Path

sys.path.append('/Users/adelina/python_labs/src/lab06/lib')
from text import normalize, tokenize, count_freq, top_n

def stats(path, n):
    with open(path, 'r') as text:
        textST = text.read()
        textST = top_n(count_freq(tokenize(normalize(textST))), n)
        print(textST)
        input()

def cat(path, n):
    with open(path,'r') as text:
        catText = text.read()
        catText_normalize = normalize(catText)
        catText_tokenize = tokenize(catText_normalize)
    for i in range(len(catText_tokenize)):
        print(i+1, catText_tokenize[i])

def main():
    parser = argparse.ArgumentParser(description="CLI‑утилиты лабораторной №6")
    subparsers = parser.add_subparsers(dest="command")

    # подкоманда cat
    cat_parser = subparsers.add_parser("cat", help="Вывести содержимое файла")
    cat_parser.add_argument("--input", required=True)
    cat_parser.add_argument("-n", action="store_true", help="Нумеровать строки")

    # подкоманда stats
    stats_parser = subparsers.add_parser("stats", help="Частоты слов")
    stats_parser.add_argument("--input", required=True)
    stats_parser.add_argument("--top", type=int, default=5)

    args = parser.parse_args()

    if args.command == "cat":
        """ Реализация команды cat """
        cat(args.input,args.n)
    elif args.command == "stats":
        """ Реализация команды stats """
        stats(args.input,args.top)

input()
main()
```
<img width="833" height="213" alt="Снимок экрана 2025-12-02 в 11 41 26" src="https://github.com/user-attachments/assets/231fd34a-5918-4d09-8b0d-435b49240110" />


### Задание 2
``` python
import argparse
import sys


sys.path.append('/Users/adelina/python_labs/src/lab05')
from json_csv import json_to_csv, csv_to_json
from csv_xlsx import csv_to_xlsx


def main():
    parser = argparse.ArgumentParser(description="Конвертеры данных")
    sub = parser.add_subparsers(dest="cmd")

    p1 = sub.add_parser("json2csv")
    p1.add_argument("--in", dest="input", required=True)
    p1.add_argument("--out", dest="output", required=True)

    p2 = sub.add_parser("csv2json")
    p2.add_argument("--in", dest="input", required=True)
    p2.add_argument("--out", dest="output", required=True)

    p3 = sub.add_parser("csv2xlsx")
    p3.add_argument("--in", dest="input", required=True)
    p3.add_argument("--out", dest="output", required=True)

    args = parser.parse_args()

    """
        Вызываем код в зависимости от аргументов.
    """

    if args.cmd == "json2csv":
        json_to_csv(args.input, args.output)
        print("Completed")

    if args.cmd == "csv2json":
        csv_to_json(args.input, args.output)
        print("Completed")

    if args.cmd == "csv2xlsx":
        csv_to_xlsx(args.input, args.output)
        print("Completed")

main()
```
<img width="749" height="650" alt="Снимок экрана 2025-12-02 в 12 00 07" src="https://github.com/user-attachments/assets/68bc1fbb-115a-45f8-a6c9-a46bcbf772a4" />

<img width="929" height="602" alt="Снимок экрана 2025-12-02 в 12 04 38" src="https://github.com/user-attachments/assets/8b59eb39-0221-49fb-b07c-a95627d2e532" />

<img width="718" height="481" alt="Снимок экрана 2025-12-02 в 12 14 35" src="https://github.com/user-attachments/assets/13c64309-7362-4ca7-a434-d54e9e847a28" />
