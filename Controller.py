import View, Database

def main():
    choice = True
    file_tel = "tel.txt"
    with open(file_tel, "a", encoding="utf-8") as file: # Создается файл если его нет в папке
         file.write("")
         
    while choice:
        action=View.user_input()      
        if action == 1:
            str=View.input_man()
            Database.save_man_data(str)
        elif action == 2:
            show_data(file_tel)
            #input_data(file_tel)
        elif action == 3:
            edit_data(file_tel)
        elif action == 4:
            delete_data(file_tel)
        else:
            choice = False

    print("До свидания")   
  


               
            
main()