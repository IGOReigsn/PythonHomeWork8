# Выбор действия
def user_input():
    print("Выберите одно из действий:")
    print("1 - Новая запись")
    print("2 - Отобразить список")
    print("3 - Изменить запись")
    print("4 - Удалить запись")
    print("5 - Найти")
    print("0 - Выход из программы")
    ask = int(input("Действие: "))
    return ask

# Вводит информацию для дальнейшего добавления
def input_man(filename):
    with open(filename, "r", encoding="utf-8") as data:
        tel_file = data.read()
    num = len(tel_file.split("\n"))
    with open(filename, "a", encoding="utf-8") as data: 
        fio = input("Введите ФИО: ")
        phone_number = input("Введите номер телефона: ")
    return (str(num)+" | "+fio+" | "+phone_number)
      

# Изменяет информацию
def edit_data(filename):
    print("\nПП | ФИО | Телефон")
    with open(filename, "r", encoding='utf-8') as data:
        tel_book = data.read()
    print(tel_book)
    print("")
    index_delete_data = int(input("Введите номер строки для редактирования: ")) - 1
    tel_book_lines = tel_book.split("\n")
    edit_tel_book_lines = tel_book_lines[index_delete_data]
    elements = edit_tel_book_lines.split(" | ")
    fio = input("Введите ФИО: ")
    phone = input("Введите номер телефона: ")
    num = elements[0]
    if len(fio) == 0:
        fio = elements[1]
    if len(phone) == 0:
        phone = elements[2]
    edited_line = f"{num} | {fio} | {phone}"
    tel_book_lines[index_delete_data] = edited_line
    print(f"Запись - {edit_tel_book_lines}, изменена на - {edited_line}\n")
    with open(filename, "w", encoding='utf-8') as f:
        f.write("\n".join(tel_book_lines))

# вводит информацию для удаления
def delete_data(filename):
    print("\nПП | ФИО | Телефон")
    with open(filename, "r", encoding="utf-8") as data:
        tel_book = data.read()
        print(tel_book)
    print("")
    index_delete_data = int(input("Введите номер строки для удаления: ")) - 1
    return index_delete_data

# вводит информацию для поиска
def find_data(filename):
    text_to_search=input("Образец для поиска: ")
    return text_to_search



        