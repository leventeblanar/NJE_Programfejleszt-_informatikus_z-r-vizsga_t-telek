# Régi osztály – nem tudjuk módosítani
class LegacyDataProvider:
    def get_data(self):
        return "Régi adat"

# Új rendszer ezt várja:
class NewSystem:
    def process(self, source):
        print("Feldolgozva:", source.fetch())

# Adapter osztály
class Adapter:
    def __init__(self, legacy):
        self.legacy = legacy

    def fetch(self):
        return self.legacy.get_data()

# Használat
legacy = LegacyDataProvider()
adapter = Adapter(legacy)
uj_rendszer = NewSystem()
uj_rendszer.process(adapter)