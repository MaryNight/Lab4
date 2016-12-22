# Итератор для удаления дубликатов
import types

class Unique(object):
    IGNORE_CASE = False
    ITEMS = []
    PASSED = []

    def __init__(self, items, **kwargs):
        # Нужно реализовать конструктор
        # В качестве ключевого аргумента, конструктор должен принимать bool-параметр ignore_case,
        # в зависимости от значения которого будут считаться одинаковые строки в разном регистре
        # Например: ignore_case = True, Aбв и АБВ разные строки
        #           ignore_case = False, Aбв и АБВ одинаковые строки, одна из них удалится
        # По-умолчанию ignore_case = False
        if 'ignore_case' in kwargs.keys():
            self.IGNORE_CASE = kwargs['ignore_case']
        if not isinstance(items, types.GeneratorType):
            self.ITEMS = iter(items)
        else:
            self.ITEMS = items

    def __next__(self):
        # Нужно реализовать __next__    
        while True:
            val = next(self.ITEMS)
            val2 = val
            if self.IGNORE_CASE:
                val2 = val2.lower()
            if val2 not in self.PASSED:
                self.PASSED.append(val2)
                return val

    def __iter__(self):
        del self.PASSED[:]
        return self

