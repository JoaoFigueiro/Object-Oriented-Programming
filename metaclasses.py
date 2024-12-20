from datetime import datetime


def get_instantiation_time(self):
    return self.instantiation_time


class My_Meta(type):
    classes_instantiated = []
    def __new__(mcs, name, bases, dictionary):

        if 'get_instantiation_time' not in dictionary:
            dictionary['get_instantiation_time'] = get_instantiation_time

        dictionary['instantiation_time'] = datetime.now()

        obj = super().__new__(mcs, name, bases, dictionary)
        mcs.classes_instantiated.append(name)

        return obj

class LegacyClass(metaclass=My_Meta):
    pass


a = LegacyClass()
print(a.get_instantiation_time())
