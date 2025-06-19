'''
    snack_types.py

    Contains different types of snacks with different entity symbols and
    types. They are all children of Snack class
'''
from snack import Snack

# Super snack giving more points for eating it
class SuperSnack(Snack):
    def __init__(self) -> None:
        self._entity: str = '#'
        self._type: str = 'super'

# Fake snack that does not give points when eaten
class FakeSnack(Snack):
    def __init__(self) -> None:
        self._entity: str = '*'
        self._type: str = 'fake'

class NormalSnack(Snack):
    def __init__(self) -> None:
        self._entity: str = '*'
        self._type: str = 'normal'