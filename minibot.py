# BOT CREATED FOR PROJECT
# VERSION 1.0
# LICENSED GNU GPL

import random
import time
from time import sleep

def welcome():
    print("""
    ██╗░░██╗███████╗██╗░░░░░██╗░░░░░░█████╗░
    ██║░░██║██╔════╝██║░░░░░██║░░░░░██╔══██╗
    ███████║█████╗░░██║░░░░░██║░░░░░██║░░██║
    ██╔══██║██╔══╝░░██║░░░░░██║░░░░░██║░░██║
    ██║░░██║███████╗███████╗███████╗╚█████╔╝
    ╚═╝░░╚═╝╚══════╝╚══════╝╚══════╝░╚════╝░
    """)
global rus
global eng

def javaprint(x):
    a = """public class Main {
        public static void main(String... a) {
            System.out.print("{0}")
    }
}""".format(x)
    print("######################################")
    print(a)

def javainput_rus(x, y):
    if y == "int":
        b = """
    import java.util.Scanner;

    public class Main {
        public static void main(String... a) {
            {0} abc;
            Scanner sc = new Scanner(System.in); //"cp866");
            System.out.print("Ваш текст...");
            abc = sc.nextInt();
            // Условия дальше сами....
        }
    }
}
        """.format(y)
        print(b)
    if y == "String":
        c = """

    import java.util.Scanner;

    public class Main {
        public static void main(String... a) {
            {0} abc;
            Scanner sc = new Scanner(System.in); //"cp866");
            System.out.print("Ваш текст...");
            abc = sc.nextLine();
            // Условия дальше сами....
        }
    }
}
        """.format(y)
        print("######################################")
        print(c)

def javainput_eng(x, y):
    if y == "int":
        b = """
    import java.util.Scanner;

    public class Main {
        public static void main(String... a) {
            {0} abc;
            Scanner sc = new Scanner(System.in); //"cp866");
            System.out.print("Your text...");
            abc = sc.nextInt();
            // Then yourself....
        }
    }
}
        """.format(y)
        print(b)
    if y == "String":
        c = """

    import java.util.Scanner;

    public class Main {
        public static void main(String... a) {
            {0} abc;
            Scanner sc = new Scanner(System.in); //"cp866");
            System.out.print("Your text...");
            abc = sc.nextLine();
            // Then yourself....
        }
    }
}
        """.format(y)
        print("######################################")
        print(c)


def javainputandprint_rus(x, y, z):
    if x == "int":
        c = """
    import java.util.Scanner;

    public class Main {
        public static void main(String... a) {
            {0} abc;
            Scanner sc = new Scanner(System.in); //'cp866');
            System.out.print('{1}');
            System.out.print('{2}');
            abc = sc.nextInt();
            // Условия дальше сами....
        }
    }
}
        """.format(x, z, y)
        print("######################################")
        print(c)
    if x == "String":
        d = """

import java.util.Scanner;

public class Main {
    public static void main(String... a) {
        {0} abc;
        Scanner sc = new Scanner(System.in); //"cp866");
        System.out.print('{1}');
        System.out.print("{2}");
        abc = sc.nextLine();
        // Условия дальше сами....
        }
    }
}
        """.format(x, z, y)
        print("######################################")
        print(d)

def javainputandprint_eng(x, y, z):
    if x == "int":
        c = """
    import java.util.Scanner;

    public class Main {
        public static void main(String... a) {
            {0} abc;
            Scanner sc = new Scanner(System.in); //'cp866');
            System.out.print('{1}');
            System.out.print('{2}');
            abc = sc.nextInt();
            // Then yourself....
        }
    }
}
        """.format(x, z, y)
        print("######################################")
        print(c)
    if x == "String":
        d = """

import java.util.Scanner;

public class Main {
    public static void main(String... a) {
        {0} abc;
        Scanner sc = new Scanner(System.in); //"cp866");
        System.out.print('{1}');
        System.out.print("{2}");
        abc = sc.nextLine();
        // Then yourself....
        }
    }
}
        """.format(x, z, y)
        print("######################################")
        print(d)

def eng():
    welcome()
    print('Hello, I am PosReady bot. Select number please:')
    vote = int(input("1 - Generation random number. \n2 - Question. \n3 - Generation random password. \n4 - calculator. \n5 - My history\n6 - Java\n7 - Exit"))
    while vote != 8:
        if vote == 1:
            print("Please, wait...")
            time.sleep(7)
            print("Generated number:", random.randint(0, 500))
        if vote == 2:
            shar = input("Write the question:")
            if shar != '':
                print(f"Ball: {random.choice(answers_eng)}")
            else:
                print("You pressed Enter please, retry...")
        if vote == 3:
            choice = int(input("Before you start what length of password will be? \n1 - on numbers. \n2 - on letters (english)"))
            if choice == 1:
                length = int(input('Enter the length password:'))
                password = ''
                for i in range(length):
                    password = password + str(random.randint(0, 500))
                print(password)
                
            if choice == 2:
                length = int(input('Enter the length password:'))
                password = ''
                for i in range(length):
                    password = password + str(random.choice(alpheng))
                print(password)
        if vote == 4:
            score1 = int(input('Write the number:'))
            score2 = input('Write operator (+ or - or * or /. if want to stop calculator, write there stop):')
            cost = score1
            while score2 != 'stop':
                if score2 == '+':
                    score1 = int(input('Write the number:'))
                    cost += score1
                    score2 = input('Write operator (+ or - or * or /. if want to stop calculator, write there stop):')
                if score2 == '-':
                    score1 = int(input('Write the number:'))
                    cost -= score1
                    score2 = input('Write operator (+ or - or * or /. if want to stop calculator, write there stop):')
                if score2 == '*':
                    score1 = int(input("Write the number:"))
                    cost *= score1
                    score2 = input('Write operator (+ or - or * or /. if want to stop calculator, write there stop):')
                if score2 == '/':
                    score1 = int(input("Write the number:"))
                    cost /= score1
                    score2 = input('Write operator (+ or - or * or /. if want to stop calculator, write there stop):')
                if score2 == 'stop':
                    print("Please, wait...")
                    time.sleep(3)
                    print('Total:',str(cost))
        if vote == 6:
            quest1 = int(input("Before start the command please select number: \n1 - print on java\n2 - input with text on java\n3 - input and print with text on java"))
            if quest1 == 1:
                text = input("Write text for print:")
                javaprint(text)
            if quest1 == 2:
                inputjava = input("Enter a hint for keyboard input:")
                inputjava3 = input("The rename for keyboard input must be int? (Yes/No)")
                if inputjava3 == "Yes":
                    javainput_eng(inputjava, "int")
                if inputjava3 == "No":
                    javainput_eng(inputjava, "String")
            if quest1 == 3:
                inputjava2 = input("Enter a hint for keyboard input:")
                javaprint2 = input("Write text for print:")
                inputjava4 = input("The rename for keyboard input must be int? (Yes/No)")
                if inputjava4 == "Yes":
                    global yes
                    yes = "int"
                    javainputandprint_eng(yes,inputjava2,javaprint2)
                if inputjava4 == "No":
                    global no
                    no = "String"
                    javainputandprint_eng(no,inputjava2,javaprint2)
        if vote == 7:
            print("Goodbye!")
            break
        print("######################################")
        vote = int(input("Select number:\n1 - Generation random number. \n2 - Question. \n3 - Generation random password. \n4 - calculator. \n6 - Java\n7 - Exit"))
def rus():
    welcome()
    print('Приветствую, меня зовут PosReady Бот. Выбери дейстивя:')
    vote = int(input("1 - Генерация рандомного числа. \n2 - Шар судьбы. \n3 - Генерация пароля. \n4 - калькулятор. \n6 - Java\n7 - Выход"))
    while vote != 8:
        if vote == 1:
            print("Подождите идёт генерация...")
            time.sleep(7)
            print("Сгенерированое число:", random.randint(0, 500))
        if vote == 2:
            shar = input("Скажи свой вопрос шару:")
            if shar != '':
                print(f"Шар: {random.choice(answers_ru)}")
            else:
                print("Вы нажали походу на Enter. Напишите цифру 2 в действии..")
        if vote == 3:
            choice = int(input("Перед тем как начать какой будет вид пароля? \n1 - на числах. \n2 - на буквах (английских)"))
            if choice == 1:
                length = int(input('Введите желаемую длину пароля:'))
                password = ''
                for i in range(length):
                    password = password + str(random.randint(0, 500))
                print(password)
                
            if choice == 2:
                length = int(input('Введите желаемую длину пароля:'))
                password = ''
                for i in range(length):
                    password = password + str(random.choice(alpheng))
                print(password)
        if vote == 4:
            score1 = int(input('Введите число:'))
            score2 = input('Введите знак (+ или - или * или /. Если хотите остановить, напишите тут stop):')
            cost = score1
            while score2 != 'stop':
                if score2 == '+':
                    score1 = int(input('Введите число:'))
                    cost += score1
                    score2 = input('Введите знак (+ или - или * или /. Если хотите остановить, напишите тут stop):')
                if score2 == '-':
                    score1 = int(input('Введите число:'))
                    cost -= score1
                    score2 = input('Введите знак (+ или - или * или /. Если хотите остановить, напишите тут stop):')
                if score2 == '*':
                    score1 = int(input("Введите число:"))
                    cost *= score1
                    score2 = input('Введите знак (+ или - или * или /. Если хотите остановить, напишите тут stop):')
                if score2 == '/':
                    score1 = int(input("Введите число:"))
                    cost /= score1
                    score2 = input('Введите знак (+ или - или * или /. Если хотите остановить, напишите тут stop):')
                if score2 == 'stop':
                    print("Пожалуйста, подождите, идёт подсчёт...")
                    time.sleep(3)
                    print('Получилось:',str(cost))
        if vote == 6:
            quest1 = int(input("Для начала выбери цифру: \n1 - просто print на java\n2 - сделать input с текстом, на java\n3 - сделать input и print с текстом, на java (Будет развиваться)"))
            if quest1 == 1:
                text = input("Введите текст для печати:")
                javaprint(text)
            if quest1 == 2:
                inputjava = input("Введите подсказку для ввода с клавиатуры:")
                inputjava3 = input("Переименная для ввода с клавиатуры должна быть численной? (Да/Нет)")
                if inputjava3 == "Да":
                    javainput(inputjava, "int")
                if inputjava3 == "Нет":
                    javainput(inputjava, "String")
            if quest1 == 3:
                inputjava2 = input("Введите подсказку для ввода с клавиатуры:")
                javaprint2 = input("Введите текст для печати:")
                inputjava4 = input("Переименная для ввода с клавиатуры должна быть численной? (Да/Нет)")
                if inputjava4 == "Да":
                    global yes
                    yes = "int"
                    javainputandprint(yes,inputjava2,javaprint2)
                if inputjava4 == "Нет":
                    global no
                    no = "String"
                    javainputandprint(no,inputjava2,javaprint2)
        if vote == 7:
            print("До свидания!")
            break
        print("######################################")
        vote = int(input("Выбери действия: \n1 - Генерация рандомного числа. \n2 - Шар судьбы. \n3 - Генерация пароля. \n4 - Калькулятор. \n5 - Моя история ДО создания этого бота\n6 - Java\n7 - Выход"))

answers_eng = [
    "🎃 Undoubtedly! 🕯️",
    "🎃 You can be sure! 🕯️",
    "🎃 Well this...! 🕯️",
    "🎃 Hard to tell... 🕯️",
    "🎃 Try again... 🕯️"
    "🎃 I doubt it... 🕯️",
    ]

answers_ru = [
    "🎃 Несомненно! 🕯️",
    "🎃 Можете быть уверены! 🕯️",
    "🎃 Ну такое...! 🕯️",
    "🎃 Сложно сказать... 🕯️",
    "🎃 Попробуй ещё раз. 🕯️"
    "🎃 Сомневаюсь в этом... 🕯️",
    ]

alpheng = [
    "A","a","B","b","C","c","D","d","E","e","F","f","G","g","H","h","I","i","J","j","K","k","L","l","M","m","N","n","O","o","P","p","Q","q","R","r","S","s","T","t",
    "U","u","V","v","W","w","X","x","Y","y","Z","z"
]
lang = int(input("Выберите язык бота / Select bot language: 1 - Русский 2 - английский / 1 - Russian 2 - English"))
if lang == 1:
    print("ok")
    rus()
if lang == 2:
    print("ok")
    eng()
