import View, Database

def main():
    choice = True
    file_tel = "tel.txt"
    with open(file_tel, "a", encoding="utf-8") as file: # Создается файл если его нет в папке
         file.write("")
         
    while choice:
        action=View.user_input()      
        if action == 1:#Новый
            str=View.input_man(file_tel)
            Database.save_man_data(file_tel,str)
        elif action == 2:# Вывод
            Database.show_list(file_tel)
        elif action == 3:# Изменить
            View.edit_data(file_tel)
        elif action == 4:# Удалить
            del_str=View.delete_data(file_tel)
            Database.del_string(file_tel,del_str)
        elif action == 5:# Найти
            text_search=View.find_data(file_tel)
            Database.find_result(file_tel,text_search)
        else:
            choice = False
    print("Работа окончена")   
                 
            
main()