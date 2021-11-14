INTERVALS = (
    ("Год", 31536000),
    ("Мес", 2592000),
    ("Нед", 604800),
    ("Дн", 86400),
    ("Час", 3600),
    ("Мин", 60),
    ("Сек", 1),
)


def display_time(seconds,granularity):
    result = []

    for name, count in INTERVALS:
        value = seconds // count
        if value:
            seconds -= value * count
            if value == 1:
                name = name.rstrip('s')
            result.append("{} {}".format(value, name))
    return ' '.join(result[:granularity])


duration = int(input("Введите промежуток времени - "))
print(display_time(duration, 7))
