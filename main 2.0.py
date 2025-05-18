from datetime import datetime
from user import User

def validate_date(date_str):
    """Перевірка правильності формату дати."""
    try:
        return datetime.strptime(date_str, "%Y-%m-%d").date()
    except ValueError:
        print("Невірний формат дати. Використовуйте формат YYYY-MM-DD.")
        return None

def main():
    username = input("Введіть ваше ім'я: ")
    user = User(username)
    journal = user.create_journal()

    while True:
        print("\nМеню:")
        print("1. Додати запис")
        print("2. Редагувати запис")
        print("3. Видалити запис")
        print("4. Переглянути всі записи")
        print("5. Фільтрувати за категорією")
        print("6. Переглянути всі категорії")
        print("0. Вихід")

        choice = input("Оберіть опцію: ")

        if choice == "1":
            text = input("Введіть текст запису: ")
            date = input("Введіть дату (YYYY-MM-DD): ")
            category = input("Введіть категорію: ")

            date = validate_date(date)
            if date:
                journal.add_entry(text, date, category)

        elif choice == "2":
            journal.list_entries()
            try:
                index = int(input("Оберіть індекс запису для редагування: "))
                new_text = input("Новий текст (залиште порожнім, щоб не змінювати): ")
                new_date = input("Нова дата (залиште порожнім, щоб не змінювати): ")
                new_category = input("Нова категорія (залиште порожнім, щоб не змінювати): ")
                new_date = validate_date(new_date) if new_date else None
                journal.edit_entry(index, new_text or None, new_date or None, new_category or None)
            except ValueError:
                print("Некоректне введення.")

        elif choice == "3":
            journal.list_entries()
            try:
                index = int(input("Оберіть індекс запису для видалення: "))
                if 0 <= index < len(journal.entries):
                    journal.delete_entry(index)
                else:
                    print("Невірний індекс запису.")
            except ValueError:
                print("Некоректне введення.")

        elif choice == "4":
            journal.list_entries()

        elif choice == "5":
            category = input("Введіть категорію для фільтрації: ")
            journal.filter_by_category(category)
        elif choice == "6":

            journal.list_categories()

        elif choice == "0":
            print("До побачення!")
            break

        else:
            print("Невідома опція.")

if __name__ == "__main__":
    main()