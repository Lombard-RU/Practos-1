import random
from colorama import init
from colorama import Fore, Back, Style

init()

print(
    Fore.GREEN + "*Вы очутились посередине поляны в лесу. Перед вами стоит седобородый старик*\n"
    + Fore.CYAN + "(Седой старик): Приветствую тебя, странник ты не просто так сюда забрёл, тебя запутал Леший! \n"
    + Fore.YELLOW + "(Герой): Что же мне делать? \n"
    + Fore.CYAN + "(Седой старик): Найди перо жарптицы, кулон с коловратом, и щит с руной Алатырь."
    + Style.RESET_ALL
)
klichka = ""
enemies_lvl_1 = ["гоблин", "лох"]
inventory = []
heal = 10
proshol_1 = False
proshol_2 = False
proshol_3 = False
level_1 = 0
result = ""


def choose_direction(number, k):
    while True:
        if number in k:
            return number
            break
        else:
            print(Fore.RED + "Вы ошиблись в цифре, введите ещё раз\n" + Style.RESET_ALL)


def dead():
    if heal <= 0:
        print(Fore.RED + "Ваше здоровье меньше 0\n" "Вы погибли" + Style.RESET_ALL)
        exit()


def vopr():
    global level_1
    level_1 = int(input(Fore.CYAN + "Куда вы отправитесь? 1.Юг 2.Север 3.Восток (Введите цифру): " + Style.RESET_ALL))


vopr()


def lvl1():
    global result
    if level_1 == 1:
        result = "Вы пошли на юг"
    elif level_1 == 2:
        result = "Вы пошли на север"
    elif level_1 == 3:
        result = "Вы пошли на восток"
    return result


result = lvl1()
print(Fore.GREEN + result + Style.RESET_ALL)

def pobeda():
    if proshol_3 and proshol_2 and proshol_1 == True:
            print(
                Fore.CYAN + "Вы возвращаетесь на поляну и отдаёте все собранные артефакты Седобородому старику и он выводит вас из леса\n"
                + Fore.GREEN
                + "Вы победили"
                + Style.RESET_ALL
            )
            exit()

def igra():
    global result, heal, klichka, proshol_1, proshol_2, proshol_3
    if result == "Вы пошли на юг" and proshol_1 == False:
        youg = int(
            input(
                Fore.GREEN + "*На юг ведёт тропинка в лесу. Вы идёте по тропинке и натыкаетесь на волка🐺 попавшего в капкан. Ему защемило ногу. Он смотрит на вас с молящими о помоще глазами*\n"
                "Что вы сделаете? 1.Помочь волку🙌 2. Пройти мимо😠 : " + Style.RESET_ALL
            )
        )
        d = [1, 2]
        f = choose_direction(youg, d)
        if f == 1:
            print(
                Fore.CYAN + "*Как только вы подоходите волк начинает вилять хвостом и вы понимаете что это пёс. Вы раздвигаете капкан руками и пёс начинает вас облизывать.*\n"
                + Fore.GREEN + "((Теперь вол ваш питомец он следует за вами и поможет в случае драки😊))\n"
                + Fore.YELLOW + "(Герой):Хмммм, как бы тебя назвать?\n"
                + Style.RESET_ALL
            )
            klichka = input(Fore.CYAN + "Введети имя пса : " + Style.RESET_ALL)
            inventory.append(klichka)
            print(Fore.GREEN + "В вашем инвенторе теперь есть: " + str(inventory) + Style.RESET_ALL)
        else:
            print(Fore.RED + "*Вы прокрадываетесь мимо*\n" "(Герой): Фух, пронесло!" + Style.RESET_ALL)
        spavn = random.randint(0, 1)
        if spavn == 1:
            k = enemies_lvl_1[random.randint(0, 1)]
            print(Fore.RED + "Вы встречаете " + k)
            print("На вас нападает " + k + Style.RESET_ALL)
            if klichka != "":
                print(Fore.GREEN + "Пёс спасает вас и загрызает врага :" + k + Style.RESET_ALL)
            else:
                print(Fore.RED + "Вас ранит враг " + k)
                heal -= 3
                print(
                    "*Вы потеряли 3 здоровья и победили*"
                    + k
                    + "ваше здоровье"
                    + str(heal)
                    + Style.RESET_ALL
                )
                dead()
        b = int(
            input(
                Fore.YELLOW + "Вы проходите дальше и попадаете на поляну залитую огнём. Посередине на камне лежит нужное вам перо жарптицы\n"
                "Что вы хотите сделать? 1. схватить перо 2. обернуть перо с кусок рубахи " + Style.RESET_ALL
            )
        )
        k = [1, 2]
        f = choose_direction(b, k)
        if f == 1:
            print(Fore.RED + " Вы обожглись пером, вы потеряли 2 здоровья" + Style.RESET_ALL)
            heal -= 2
            dead()
        inventory.append("Перо жар птицы")
        print(Fore.GREEN + "Вы собрали первый артефакт")
        print("*Пёс оставляет вас, а вы возвращаетесь на поляну*" + Style.RESET_ALL)
        proshol_1 = True
        pobeda()
        vopr()
        result = lvl1()
        print(Fore.GREEN + result + Style.RESET_ALL)
        igra()

    if result == "Вы пошли на север" and proshol_2 == False:
        sever = int(
            input(
                Fore.CYAN + "*Вы идёте и видете ловушку на которой что-то написано\n"
                "(Ловушка): Пароль это ответ на этот пример: x^2 - 6x + 9 = 0. Ответ: " + Style.RESET_ALL
            )
        )
        if sever != 3:
            heal -= 2
            print(Fore.RED + "*Ловушка срабатывает и вы теряете 2 здоровья*" + Style.RESET_ALL)
            dead()
        print(
            Fore.GREEN + "*Вы проходите и оказываетесь перед пнём на котором лежит щит с руной Алатыр. Вы берёте его и возвращаетесь на поляну.*" + Style.RESET_ALL
        )
        inventory.append("щит с руной Алатырь")
        proshol_2 = True
        pobeda()
        vopr()
        result = lvl1()
        print(Fore.GREEN + result + Style.RESET_ALL)
        igra()

    ogni = ["огонь", "пламя"]
    if result == "Вы пошли на восток" and proshol_3 == False:
        vostok = input(
            Fore.CYAN + "*Вы идёте по поленя и упираетесь в каменную стену на которой написанна загадка:\n"
            "Я не живое существо, но я расту; У меня нет лёгких, но мне нужен воздух; У меня нет рта, но вода убивает меня. Что я?*" + Style.RESET_ALL
        ).lower()

        if vostok not in ogni:
            print(Fore.RED + "*На вас падает стела и вы теряете 7 здоровья*" + Style.RESET_ALL)
            heal -= 7
            dead()
        print(
            Fore.GREEN + "*Стена отодвигается и вы берёте кулон с коловратом, который лежал на полу пещеры за стеной*" + Style.RESET_ALL
        )
        proshol_3 = True
        pobeda()
        vopr()
        result = lvl1()
        print(Fore.GREEN + result + Style.RESET_ALL)
        igra()


igra()
