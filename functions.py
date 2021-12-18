def read_file(path: str):
    cases = []
    with open(path, 'r', encoding='utf-8') as file:
        for item in file:
            parsed_line = item.strip().split()
            for i in range(len(parsed_line)):
                try:
                    parsed_line[i] = int(parsed_line[i])
                except ValueError:
                    continue
            cases.append(parsed_line)
    return cases


def find_min(massive: list):
    try:
        current_min = massive[0]
        for i in massive:
            int(i)
            if i < current_min:
                current_min = i
        return current_min
    except OverflowError:
        return 'Ошибка переполнения!'
    except ValueError:
        return 'Некорректный ввод!'


def find_max(massive: list):
    try:
        current_max = massive[0]
        for i in massive:
            int(i)
            if i > current_max:
                current_max = i
        return current_max
    except OverflowError:
        return 'Ошибка переполнения!'
    except ValueError:
        return 'Некорректный ввод!'


def find_sum(mass: list):
    try:
        total_sum = 0
        for i in mass:
            total_sum = i
        return total_sum
    except OverflowError:
        return 'Ошибка переполнения!'
    except TypeError:
        return 'Некорректный ввод!'


def find_product(mass: list):
    try:
        product = 1
        for i in mass:
            product *= i
        return product
    except OverflowError:
        return 'Ошибка переполнения'
    except TypeError:
        return 'Некорректный ввод!'

