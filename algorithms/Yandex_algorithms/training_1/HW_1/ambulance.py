# Бригада скорой помощи выехала по вызову в один из отделенных районов. К сожалению, когда диспетчер получил вызов, он успел записать только адрес дома и номер квартиры K1, 
# а затем связь прервалась. Однако он вспомнил, что по этому же адресу дома некоторое время назад скорая помощь выезжала в квартиру K2, которая расположена в подъезда P2 на этаже N2. 
# Известно, что в доме M этажей и количество квартир на каждой лестничной площадке одинаково. Напишите программу, которая вычисляет номер подъезда P1 и номер этажа N1 квартиры K1.

import math

k_1, m, k_2, p_2, n_2 = map(int, input().split())
answers = set()

for i in range(1, max(k_1, k_2) + 1):

    if p_2 == math.ceil(k_2 / (i * m)) and n_2 == math.ceil(k_2 / i - m * (p_2 - 1)):
        flats = i
        p_1 = math.ceil(k_1 / (flats * m))
        n_1 = math.ceil(k_1 / flats - m * (p_1 - 1))
        answers.add((p_1, n_1))

if len(answers) == 1:
    print(*list(answers)[0])

elif len({x[0] for x in answers}) > 1 and len({x[1] for x in answers}) > 1:
    print(0, 0)

elif len({x[0] for x in answers}) > 1:
    print(0, list(answers)[0][1])

elif len({x[1] for x in answers}) > 1:
    print(list(answers)[0][0], 0)

else:
    print(-1, -1)
