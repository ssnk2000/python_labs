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