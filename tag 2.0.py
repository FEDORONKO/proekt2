class Tag:
    """Клас, що представляє тег для категоризації записів щоденника."""
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Тег: {self.name}"