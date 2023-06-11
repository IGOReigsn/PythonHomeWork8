#Добавление новой строки в файл
def save_man_data(filename,str):
    with open(filename, "a", encoding="utf-8") as data:
        data.write(str+"\n")
    print(f"Добавлена запись : {str} \n")
    
# Распечатка файла    
def show_list(filename):
    print("\nПП | ФИО | Телефон")
    with open(filename, "r", encoding="utf-8") as data:
        print(data.read())
    print("")

# удаляет строку из файла            
def del_string(filename,index_delete_data):
    with open(filename, "r", encoding="utf-8") as data:
        tel_book = data.read()
    tel_book_lines = tel_book.split("\n")
    print(tel_book_lines)
    del_tel_book_lines = tel_book_lines[index_delete_data]
    tel_book_lines.pop(index_delete_data)
    print(f"Удалена запись: {del_tel_book_lines}\n")
    with open(filename, "w", encoding='utf-8') as data:
        data.write("\n".join(tel_book_lines))

# Результат поиска    
def find_result(filename,text):
    print("\nПП | ФИО | Телефон")
    with open(filename, "r", encoding="utf-8") as data:
        text_strings=data.readlines()
        for work_string in text_strings:
            if text.upper() in work_string.upper():
                print(work_string)
    print("")