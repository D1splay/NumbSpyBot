import os
import platform
import subprocess

def показать_меню():
    ascii_art = """
      _   _                 _    ____              ____        _   
     | \ | |_   _ _ __ ___ | |__/ ___| _ __  _   _| __ )  ___ | |_ 
     |  \| | | | | '_ ` _ \| '_ \___ \| '_ \| | | |  _ \ / _ \| __|
     | |\  | |_| | | | | | | |_) |__) | |_) | |_| | |_) | (_) | |_ 
     |_| \_|\__,_|_| |_| |_|_.__/____/| .__/ \__, |____/ \___/ \__|
                                      |_|    |___/                 
    """

    print(ascii_art)
    print("Инструмент социальной инженерии                  Автор: Kel`w\n")
    print("1) Запуск бота")
    print("2) Очистка обработанных пользователей")
    print("3) Очистка токена бота")
    print("4) Перезапись токена бота")
    print("5) Изменить фразы")
    print("6) Очистка базы с номерами")
    print("0) Выход")

def запустить_бота():
    os.system("python bot.py")
    exit()

def очистить_файл(filename, message):
    confirm = input(f"{message} (y/n): ").lower()
    if confirm == 'y':
        with open(filename, 'w') as file:
            file.truncate()
        print(f"{filename} очищен.")
    else:
        print("Операция отменена.")

def перезаписать_токен():
    token = input("Введите новый токен бота: ")
    with open('token.txt', 'w') as file:
        file.write(token)
    print("Токен успешно перезаписан.")

def изменить_фразы():
    clear_screen()
    if platform.system() == "Windows":
        os.system("notepad msg.txt")
    else:
        editor_command = os.getenv('EDITOR', 'nano')
        try:
            if platform.system() == "Darwin":  # macOS
                subprocess.run(["open", "msg.txt"])
            elif platform.system() == "Linux":
                subprocess.run([editor_command, 'msg.txt'])
        except FileNotFoundError:
            print("Не удалось открыть текстовый редактор. Убедитесь, что переменная окружения EDITOR указывает на верный путь к редактору.")
        except Exception as e:
            print(f"Произошла ошибка: {e}")

def clear_screen():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

if __name__ == "__main__":
    while True:
        clear_screen()
        показать_меню()
        choice = input("Выберите функцию (введите цифру): ")

        if choice == '1':
            запустить_бота()
            break
        elif choice == '2':
            очистить_файл('processed_users.txt', "Вы уверены, что хотите очистить обработанных пользователей?")
        elif choice == '3':
            очистить_файл('token.txt', "Вы уверены, что хотите очистить токен бота?")
        elif choice == '4':
            перезаписать_токен()
            break
        elif choice == '5':
            изменить_фразы()
        elif choice == '6':
            очистить_файл('data.txt', "Вы уверены, что хотите очистить базу с номерами?")
        elif choice == '0':
            exit()
        else:
            print("Некорректный выбор. Попробуйте снова.")
