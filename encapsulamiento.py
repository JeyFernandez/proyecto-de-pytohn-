class A:
    def __init__(self, a, b):
        self._a = a
        self._b = b
    def __eq__(self, other):
        return self._a == other._a