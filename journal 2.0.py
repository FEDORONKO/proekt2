from journal_entry import JournalEntry
from tag import Tag

class Journal:
    """
    Клас представляє щоденник з методами додавання, редагування, видалення і пошуку записів.
    """
    def __init__(self, user):
        self.user = user
        self.entries = []
        self.categories = set()

    def add_entry(self, text, date, category):
        if not text.strip():
            print("Запис не може бути порожнім.")
            return
        if category in self.categories:
            print("Така категорія вже існує. Категорії мають бути унікальними.")
            return

        entry = JournalEntry(text, date, category)
        self.entries.append(entry)
        self.categories.add(category)
        print("Запис додано успішно.")

    def edit_entry(self, index, new_text=None, new_date=None, new_category=None):
        if 0 <= index < len(self.entries):
            entry = self.entries[index]
            if new_text:
                entry.text = new_text
            if new_date:
                entry.date = new_date
            if new_category and new_category not in self.categories:
                self.categories.discard(entry.tag.name)  # Видаляємо стару категорію
                entry.tag.name = new_category  # Оновлюємо категорію
                self.categories.add(new_category)
            print("Запис оновлено.")
        else:
            print("Невірний індекс запису.")

    def delete_entry(self, index):
        if 0 <= index < len(self.entries):
            removed = self.entries.pop(index)

            if removed.tag:
                self.categories.discard(removed.tag.name)
            print("Запис видалено.")
        else:
            print("Невірний індекс запису.")

    def list_entries(self):
        for i, entry in enumerate(self.entries):
            print(f"[{i}] {entry}")

    def filter_by_category(self, category):
        results = [e for e in self.entries if e.tag.name == category]
        if results:
            for entry in results:
                print(entry)
        else:
            print("Записів з такою категорією не знайдено.")

    def list_categories(self):
        if self.categories:
            print("Категорії:")
            for category in self.categories:
                print(f"- {category}")
        else:
            print("Категорії ще не створено.")