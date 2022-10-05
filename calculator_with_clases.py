class Calculator:
    def __init__(self, name):
        self.name = name

    @classmethod
    def alternative_name_create(cls, alternative_name):
        return cls(alternative_name + 'Name')

    def say_my_name(self):
        print('Your name is ' + self.name)

    @staticmethod
    def add(self, a, b):
        return a + b

    @staticmethod
    def subs(self, a, b):
        return a - b


    def mult(self, a, b):
        print(a * b)


    def div(self, a, b):
        print(a / b)


if __name__ == '__main__':
    a = 3
    b = 1
    calc = Calculator('Artur')
    calc.say_my_name()
    print(calc.name)