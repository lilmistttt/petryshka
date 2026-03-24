# TODO Напишите функцию find_common_participants
def find_common_participants(first_group, second_group, separator=','):
    list1 = first_group.split(separator)
    list2 = second_group.split(separator)
    return sorted([name for name in list1 if name in list2])
participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
print(find_common_participants(participants_first_group, participants_second_group, '|'))
# TODO Провеьте работу функции с разделителем отличным от запятой
