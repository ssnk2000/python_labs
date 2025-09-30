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