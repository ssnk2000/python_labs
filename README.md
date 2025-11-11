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



--------------------------------------
## Лабораторная работа 3
-----
-----
### Задание 1
``` python
import re

def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    if casefold:
        text = text.casefold()

    if yo2e:
        text = text.replace('ё', 'е')
        text = text.replace('Ё', 'Е')

    text = re.sub(r'\t\r\n', ' ', text)
    text = re.sub(r'\s+', ' ', text).strip()

    return text


def tokenize(text: str) -> list[str]:
    return re.findall(r'\w+(?:-\w+)*', text)


def count_freq(tokens: list[str]) -> dict[str, int]:
    freq = {}
    for token in tokens:
        if token in freq:
            freq[token] += 1
        else:
            freq[token] = 1

    return freq


def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    sorted_freq = sorted(freq.items(), key=lambda item: (-item[1], item[0]))

    return sorted_freq[:n]
```
<img width="691" height="528" alt="Снимок экрана 2025-11-11 в 21 21 40" src="https://github.com/user-attachments/assets/9b3b4136-2fd5-4d31-a950-325b5f701619" />


### Задание 2
``` python
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
```
<img width="240" height="165" alt="Снимок экрана 2025-11-11 в 21 57 33" src="https://github.com/user-attachments/assets/efa7e372-b202-46d9-9e35-bdd38040310e" />
