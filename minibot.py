import random
import time
from time import sleep

print("""
██╗░░██╗███████╗██╗░░░░░██╗░░░░░░█████╗░
██║░░██║██╔════╝██║░░░░░██║░░░░░██╔══██╗
███████║█████╗░░██║░░░░░██║░░░░░██║░░██║
██╔══██║██╔══╝░░██║░░░░░██║░░░░░██║░░██║
██║░░██║███████╗███████╗███████╗╚█████╔╝
╚═╝░░╚═╝╚══════╝╚══════╝╚══════╝░╚════╝░
""")

def info():
    print("Версия Бота")
    print("### 0.9 ####")

def javaprint(x):
    a = """public class Main {
        public static void main(String... a) {
            System.out.print("{0}")
    }
}""".format(x)
    print("######################################")
    print(a)

def javainput(x, y):
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

def javainputandprint(x, y, z):
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

answers = [
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

print('Приветствую, меня зовут PosReady Бот. Выбери дейстивя:')
vote = int(input("1 - Генерация рандомного числа. \n2 - Шар судьбы. \n3 - Генерация пароля. \n4 - калькулятор. \n5 - Моя история ДО создания этого бота\n6 - Java\n7 - Выход"))
while vote != 7:
    if vote == 1:
        print("Подождите идёт генерация...")
        time.sleep(7)
        print("Сгенерированое число:", random.randint(0, 500))
    if vote == 2:
        shar = input("Скажи свой вопрос шару:")
        if shar != '':
            print(f"Шар: {random.choice(answers)}")
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
        calc = int(input("Введите 1 число:"))
        calc2 = int(input("Введите 2 число:"))
        calc3 = int(input("Введите цифру оператора: \n1: +\n2: -\n3: /\n4: *"))
        if calc3 == 1:
            print("Подсчёт...")
            time.sleep(3)
            print("Получилось:", (calc+calc2))
        if calc3 == 2:
            print("Подсчёт...")
            time.sleep(3)
            print("Получилось:", (calc-calc2))
        if calc3 == 3:
            print("Подсчёт...")
            time.sleep(3)
            print("Получилось:", (calc/calc2))
        if calc3 == 4:
            print("Подсчёт...")
            time.sleep(3)
            print("Получилось:", (calc*calc2))
    if vote == 5:
        info()
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
    print("######################################")
    vote = int(input("Выбери действия: \n1 - Генерация рандомного числа. \n2 - Шар судьбы. \n3 - Генерация пароля. \n4 - Калькулятор. \n5 - Моя история ДО создания этого бота\n6 - Java\n7 - Выход"))
