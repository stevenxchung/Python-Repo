class Singleton:
    _value = None
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def get_value(self) -> str:
        res = self._value
        print(f'get_value(): {res}')
        return res

    def set_value(self, value: str):
        self._value = value


if __name__ == '__main__':
    s = Singleton()

    s.get_value()  # null

    s.set_value('a value string')
    s.get_value()  # 'a value string'

    s2 = Singleton()

    s2.get_value()  # 'a value string'
