def count_lines(file_name):
    with open(file_name, encoding='utf-8') as f:
        counter = 0
        for line in f:
            counter += 1
        return counter

def read_lines(file_name, number_of_line):
    with open(file_name, encoding='utf-8') as f:
        data = f.readlines()
        return data[number_of_line]


with open('result.txt', 'a', encoding='utf-8') as f:
    if count_lines('1.txt') < count_lines('2.txt'):
        f.write(f'1.txt\n{count_lines("1.txt")}\n')
        for i in range(count_lines('1.txt')):
            f.write(f'Cтрока номер {i+1} файла номер 1 - {read_lines("1.txt", i)}')

        f.write(f'\n2.txt\n{count_lines("2.txt")}\n')
        for i in range(count_lines('2.txt')):
            f.write(f'Cтрока номер {i+1} файла номер 2 - {read_lines("2.txt", i)}')

    else:
        f.write(f'2.txt\n{count_lines("2.txt")}\n')
        for i in range(count_lines('2.txt')):
            f.write(f'Cтрока номер {i+1} файла номер 2 - {read_lines("2.txt", i)}')

        f.write(f'\n1.txt\n{count_lines("1.txt")}\n')
        for i in range(count_lines('1.txt')):
            f.write(f'Cтрока номер {i+1} файла номер 1 - {read_lines("1.txt", i)}')

print("Файл result.txt записан")