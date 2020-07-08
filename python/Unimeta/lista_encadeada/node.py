class Node:
    def __init__(self, value):
        self.value = value
        self.previous = None
        self.next = None

    def __repr__(self):
        return f'{str(self.previous)} ← {str(self.value)} → {str(self.next)}'