from datetime import datetime
from tag import Tag

class JournalEntry:
    """Клас, що представляє запис щоденника."""

    def __init__(self, text, date=None, category=None):
        if not text.strip():
            raise ValueError("Текст запису не може бути порожнім")

        self.text = text
        self.date = date if date else datetime.now().date()

        if category:
            # Якщо передано об'єкт Tag — використовуємо його
            if isinstance(category, Tag):
                self.tag = category
            else:
                self.tag = Tag(category)
        else:
            self.tag = None

    def __str__(self):
        tag_str = self.tag.name if self.tag else "Без категорії"
        return f"[{self.date}] ({tag_str}) {self.text}"