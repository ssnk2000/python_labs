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
