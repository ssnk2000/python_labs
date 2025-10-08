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

-----
-----
-----
## Лабораторная работа 2
-----
-----
### Задание 1
``` python
def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
    if not nums:
        raise ValueError("Список пуст")
    return (min(nums), max(nums))

def unique_sorted(nums: list[float | int]) -> list[float | int]:
    return sorted(set(nums))

def flatten(mat: list[list | tuple]) -> list:
    flat_list = []
    for row in mat:
        if not isinstance(row, (list, tuple)):
            raise TypeError("Строка не строка строк матрицы")
        flat_list.extend(row)
    return flat_list

print("min/max: ")
print(min_max([3, -1, 5, 5, 0]))
print(min_max([42]))
print(min_max([-5, -2, -9]))
# print(min_max([]))
print(min_max([1.5, 2, 2.0, -3.1]))

print("sort: ")
print(unique_sorted([3, 1, 2, 1, 3]))
print(unique_sorted([]))
print(unique_sorted([-1, -1, 0, 2, 2]))
print(unique_sorted([1.0, 1, 2.5, 2.5, 0]))

print("flatten: ")
print(flatten([[1, 2], [3, 4]]))
print(flatten([[1, 2], (3, 4, 5)]))
print(flatten([[1], [], [2, 3]]))
# print(flatten([[1, 2], "ab"]))
```
<img width="188" height="326" alt="Снимок экрана 2025-10-08 в 00 52 09" src="https://github.com/user-attachments/assets/7a3eb56a-99b3-4550-98c6-7358c850bfae" />


### Задание 2
``` python
def transpose(mat):
    if len(mat) == 0:
        return []
    row_length = len(mat[0])
    for row in mat:
        if len(row) != row_length:
            raise ValueError("Строки разной длины, матрица рваная")
    result = []
    for i in range(row_length):
        new_row = []
        for j in range(len(mat)):
            new_row.append(mat[j][i])
        result.append(new_row)
    return result


def row_sums(mat):
    if len(mat) == 0:
        return []
    row_length = len(mat[0])
    for row in mat:
        if len(row) != row_length:
            raise ValueError("Строки разной длины, матрица рваная")
    result = []
    for row in mat:
        total = 0
        for num in row:
            total += num
        result.append(total)
    return result


def col_sums(mat):
    if len(mat) == 0:
        return []
    row_length = len(mat[0])
    for row in mat:
        if len(row) != row_length:
            raise ValueError("Строки разной длины, матрица рваная")
    result = []
    for i in range(row_length):
        total = 0
        for j in range(len(mat)):
            total += mat[j][i]
        result.append(total)
    return result

print("transpose: ")
matrix1 = [[1, 2, 3]]
matrix2 = [[1], [2], [3]]
matrix3 = [[1, 2], [3, 4]]
matrix4 = []
matrix5 = [[1, 2], [3]]
print(transpose(matrix1))
print(transpose(matrix2))
print(transpose(matrix3))
print(transpose(matrix4))
print(transpose(matrix5))

print("row sums: ")
matrix6 = [[1, 2, 3], [4, 5, 6]]
matrix7 = [[-1, 1], [10, -10]]
matrix8 = [[0, 0], [0, 0]]
matrix9 = [[1, 2], [3]]
print(row_sums(matrix6))
print(row_sums(matrix7))
print(row_sums(matrix8))
print(row_sums(matrix9))

print("col sums: ")
print(col_sums(matrix6))
print(col_sums(matrix7))
print(col_sums(matrix8))
print(col_sums(matrix9))
```
<img width="139" height="296" alt="Снимок экрана 2025-10-08 в 02 18 15" src="https://github.com/user-attachments/assets/08e2b3ed-1482-414b-bd37-3618afc9fe40" />

### Задание 3
``` python
def format_record(rec: tuple[str, str, float]) -> str:
    fio_full, group, gpa = rec
    fio_clear = ' '.join(fio_full.strip().split())
    parts = fio_clear.split()
    surname = parts[0]
    initials = ''
    for name_part in parts[1:3]:
        initials += name_part[0].upper() + '.'
    fio_init = f"{surname} {initials}"
    gpa_ = f"{gpa:.2f}"
    return f"{fio_init}, гр. {group}, GPA {gpa_}"

print(format_record(("Иванов Иван Иванович", "BIVT-25", 4.6)))
print(format_record(("Петров Пётр", "IKBO-12", 5.0)))
print(format_record(("Петров Пётр Петрович", "IKBO-12", 5.0)))
print(format_record(("  Cидорова  анна   сергеевна ", "ABB-01", 3.234)))
```
<img width="309" height="96" alt="Снимок экрана 2025-10-08 в 03 00 25" src="https://github.com/user-attachments/assets/c5e16a18-2d01-447d-b0be-b267cd78da67" />
