class MemoryBank:
    def __init__(self):
        self.memories = {
            "M1": None,
            "M2": None,
            "M3": None,
            "M4": None,
            "M5": None
        }

    def store(self, name, value):
        if name not in self.memories:
            raise ValueError("Mémoire invalide")
        self.memories[name] = value

    def read(self, name):
        if name not in self.memories:
            raise ValueError("Mémoire invalide")
        return self.memories[name]

    def clear(self, name):
        if name not in self.memories:
            raise ValueError("Mémoire invalide")
        self.memories[name] = None

    def clear_all(self):
        for key in self.memories:
            self.memories[key] = None

    def list_all(self):
        return dict(self.memories)
