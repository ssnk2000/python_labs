import sys
from lib.text import normalize, tokenize, count_freq, top_n

def main():
    text = sys.stdin.read()

    text = normalize(text=text)
    tokens = tokenize(text=text)
    freq = count_freq(tokens)
    top_5 = top_n(freq, 5)

    print(f"Всего слов: {len(tokens)}")
    print(f"Уникальных слов: {len(set(tokens))}")
    print("Топ-5:")
    for word, count in top_5:
        print(f"{word}:{count}")

if __name__ == "__main__":
    main()