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