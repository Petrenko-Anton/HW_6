import sqlite3
import init_db


def execute_query(sql: str) -> list:
    with sqlite3.connect("MyDB.sqlite") as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()


def main():
    help_str = """demo SQLite база "Інститут". Введіть цифру для виконання дії:
    0. Ініціалізація бази і перезаповнення данними
    Запити:
    1. Знайти 5 студентів із найбільшим середнім балом з усіх предметів.
    2. Знайти студента із найвищим середнім балом з певного предмета.
    3. Знайти середній бал у групах з певного предмета.
    4. Знайти середній бал на потоці (по всій таблиці оцінок).
    5. Знайти, які курси читає певний викладач.
    6. Знайти список студентів у певній групі.
    7. Знайти оцінки студентів в окремій групі з певного предмета.
    8. Знайти середній бал, який ставить певний викладач зі своїх предметів.
    9. Знайти список курсів, які відвідує студент.
    10. Список курсів, які певному студенту читає певний викладач.
    11. Середній бал, який певний викладач ставить певному студентові.
    12. Оцінки студентів у певній групі з певного предмета на останньому занятті.    
    13. ВИХІД
    14. Інструкції
    """
    print(help_str)
    while True:
        answer = input(">>>")
        if answer == "14":
            print(help_str)
        elif answer == "13":
            break
        elif answer == "0":
            init_db.init_db()
        elif 1 >= int(answer) >= 12:
            filename = f"query_{answer}.sql"
            with open(filename, "r") as f:
                sql = f.read()
            print(execute_query(sql))
    else:
        print("Невірно введена команда")


if __name__ == "__main__":
    main()
