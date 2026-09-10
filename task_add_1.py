types = {
    1: 'Блокирующий',
    2: 'Критический',
    3: 'Значительный',
    4: 'Незначительный',
    5: 'Тривиальный'
}

tickets = {
    1: ['API_45', 'API_76', 'E2E_4'],
    2: ['UI_19', 'API_65', 'API_76', 'E2E_45'],
    3: ['E2E_45', 'API_45', 'E2E_2'],
    4: ['E2E_9', 'API_76'],
    5: ['E2E_2', 'API_61']
}

# вспомогательная функция работы со списками
def delete_duplicates_in_lst(ticket:str, lst_tickets:list, is_exist:bool):
    count = lst_tickets.count(ticket)
    if count:
        if not is_exist:
            count -= 1
        is_exist = True

        # здесь reverse туда и обратно только для формирования порядка в выводе как в примере
        # функциональной нагрузки для выполнения задания не имеет
        lst_tickets.reverse()
        for val in range(count):
            lst_tickets.remove(ticket)
        lst_tickets.reverse()
    return (lst_tickets, is_exist)

# удаление дублей из списков с тикетами
# в условии задания не указано, что функция принимает аргументы
def delete_duplicates():
    tmp_tickets = []
    for lst in tickets.values():
        tmp_tickets.extend(lst)
    tmp_tickets = set(tmp_tickets)
    for ticket in tmp_tickets:
        first_occurrence = False
        for key, val in tickets.items():
            tickets[key], first_occurrence = delete_duplicates_in_lst(ticket, val, first_occurrence)

# формировани словаря списков уникальных тикетов по типам багов
def unique_tickets(types:dict, tickets:dict):
    return dict(zip(types.values(), tickets.values()))


delete_duplicates()                                 # удаление дублей из списков тикетов
tickets_by_type = unique_tickets(types, tickets)    # формировани словаря списков уникальных тикетов по типам багов
print(tickets_by_type)

# пример итогового словаря из условия задания:
# tickets_by_type = {
#     'Блокирующий': ['API_45', 'API_76', 'E2E_4'],
#     'Критический': ['UI_19', 'API_65', 'E2E_45'],
#     'Значительный': ['E2E_2'],
#     'Незначительный': ['E2E_9'],
#     'Тривиальный': ['API_61']
# }
