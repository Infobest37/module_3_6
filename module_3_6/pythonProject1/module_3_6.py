def calculate_structure_sum(data_structure):
    sum_1 = 0

    # Если элемент - число, просто добавляем его к сумме
    if isinstance(data_structure, (int, float)):
        sum_1 += data_structure

    # Если элемент - строка, добавляем её длину к сумме
    elif isinstance(data_structure, str):
        sum_1 += len(data_structure)

    # Если элемент - список, кортеж или множество, рекурсивно обрабатываем каждый элемент
    elif isinstance(data_structure, (list, tuple, set)):
        for item in data_structure:
            sum_1 += calculate_structure_sum(item)

    # Если элемент - словарь, обрабатываем его ключ и значение и плюсуем
    elif isinstance(data_structure, dict):
        for key, value in data_structure.items():
            sum_1 += calculate_structure_sum(value)
            sum_1 += calculate_structure_sum(key)
    return sum_1
