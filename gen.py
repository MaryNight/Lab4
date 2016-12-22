import random


# Генератор вычленения полей из массива словарей
# Пример:
# goods = [
#    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
#    {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'}
# ]
# field(goods, 'title') должен выдавать 'Ковер', 'Диван для отдыха'
# field(goods, 'title', 'price') должен выдавать {'title': 'Ковер', 'price': 2000}, {'title': 'Диван для отдыха', 'price': 5300}

def field(items, *args):
    assert len(args) > 0
    # Необходимо реализовать генератор
    for elem in items:
        r = {}
        for arg in args:
            if arg in elem:
                if len(args) == 1:
                    yield elem[arg]
                else:
                    if elem[arg] is not None:
                        r[arg] = elem[arg]
        if len(r) > 0 and len(args) > 1:
            yield r


# Генератор списка случайных чисел
# Пример:
# gen_random(1, 3, 5) должен выдать примерно 2, 2, 3, 2, 1
# Hint: реализация занимает 2 строки
def gen_random(begin, end, num_count):
    # Необходимо реализовать генератор
    for i in range(num_count):
        yield random.randint(begin, end)

def gen(begin, end, num_count):
    # Необходимо реализовать генератор
    isFirst = True
    for i in range(num_count):
        if (isFirst):
            yield begin
        else:
            yield end
        isFirst = not isFirst