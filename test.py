# нападающие на растановке 1-центральный 2-правый 3 левый
# защитники 1-левый 2-правый
# Программа помогает подобрать возможный маневр на определнный момент
# игры в хоккей исходя из настоящего положения игроков
# Прим. пункты, в вопросах которые вам не нужны пропускаете нажатием Enter

print('Схема чего вас интерисует?')  # 1. Оборона 2.Атака
b = str.lower(input())
print('Где находятся нападающие?')
a1 = str.lower(input())
print('Где находятся защитники?')
a2 = str.lower(input())
print('Где находиться игрок противника владеющий шайбой?')
a3 = str.lower(input())
print('Может ли команда осществлять активный пресинг?')
a4 = str.lower(input())
if b == 'оборона':
    if a1 == 'усы питак питак' and a2 == 'зона обороны зона обороны':
        print('Форчекинг по схеме 1–2–2')
    elif a1 == 'усы питак слот' and a3 == 'за воротами' and a4 == 'да':
        print('Форчекинг по схеме 2–1–2')
    elif a1 == 'усы усы питак' and a2 == 'зона обороны зона обороны' and a4 == 'да':
        print('Форчекинг по системе 2–3 ( блокировка левого коридора )')
    elif a1 == 'усы усы зона обороны' and a2 == 'слот зона атаки':
        print('Система торпеда')
    else:
        print('Простите, но в нашей базе нет подходящих вам схем!')

elif b == 'атака':
    if a1 == 'зона вбрасывания зона атаки зона обороны':
        print('Растягивание от синей до синей')
    elif a1 == 'усы питак нейтральная зона' and a2 == 'за воротами угол':
        print('Уклон на сильный фланг ')
    elif a1 == 'центральная точка нейтральная зона' and a2 == 'за воротами угол':
        print('Трое высоко')
    else:
        print('Простите, но в нашей базе нет подходящих вам схем!')