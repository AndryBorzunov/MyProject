from src.data_loader import get_fild_values_unique, load_data_csv, load_data_excel
from src.generators import filter_by_currency
from src.process_bank import process_bank_search
from src.processing import filter_by_state, sort_by_date
from src.utils import load_transactions
from src.widget import get_date, mask_account_card

if __name__ == "__main__":
    """
    # Домашнее задание 9.1
    print(get_mask_card_number(7000792289606361))
    print(get_mask_account(7365410840135874305))

    # Домашнее задание 9.2
    print(mask_account_card("Счет 73654108430135874305"))
    print(mask_account_card("Visa Platinum 8990922113665229"))

    print(get_date("2024-03-11T02:26:18.671407"))

    # Домашнее задание 10.1
    input_data_list = [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]

    print(filter_by_state(input_data_list, "CANCELED"))

    print(sort_by_date(input_data_list, False))

    # Домашнее задание 11.1
    transactions = [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160",
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229",
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657",
        },
    ]

    print("1.\n")
    usd_transactions = filter_by_currency(transactions, "USD")
    for _ in range(2):
        print(next(usd_transactions))

    print("2.\n")
    descriptions = transaction_descriptions(transactions)
    for _ in range(5):
        print(next(descriptions))

    print("3.\n")
    for card_number in card_number_generator(1, 5):
        print(card_number)

    # Домашнее задание 11.2
    @log("mylog.txt")
    def my_function(x: float, y: float) -> Any:
        return x / y

    my_function(6, 4)

    # Домашнее задание 12.1
    print("\n")
    print("Домашнее задание 12.1\n")
    transactions = load_transactions("data/operations.json")
    if len(transactions) > 0:
        print(transactions[4])

    try:
        amount = get_amount_rub(transactions[0])
        print(f"amount = {amount} руб")
    except Exception as e:
        print(e)

    # Домашнее задание 13.1
    print("\n")
    print("Домашнее задание 13.1\n")
    print(load_data_csv("data"))

    print("\n")
    print(load_data_excel("data"))

    transactions = load_data_csv("data", False)

    # Домашнее задание 13.2
    print("\n")
    print("Домашнее задание 13.2\n")
    print(process_bank_search(transactions, "перевод на счет "))

    print("\n")
    name_operations_list = get_descriptions_unique(transactions)
    print(name_operations_list)

    print("\n")
    print(process_bank_operations(transactions, name_operations_list))
    """

    # Выбор источника данных
    print("\n")
    print("Программа: Привет! Добро пожаловать в программу работы с банковскими транзакциями\n")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла\n")
    menu = input("Пользователь: ")
    data_name = {"1": "JSON", "2": "CSV", "3": "XLSX"}
    transactions = []
    if menu in data_name:
        print(f"Для обработки выбран {data_name[menu]}-файл\n")
        if menu == "1":
            transactions = load_transactions("data/operations.json")
        if menu == "2":
            transactions = load_data_csv("data", False)
        if menu == "3":
            transactions = load_data_excel("data", False)
    else:
        print("В меню нет такого пункта")
        exit(0)

    # Фильтрация операций по статусу
    print("Программа: Введите статус, по которому необходимо выполнить фильтрацию.")
    states = get_fild_values_unique(transactions, "state")
    print(f"Доступные для фильтровки статусы: {states}\n")
    state = input("Пользователь: ")
    state = state.upper()

    if state not in states:
        print(f"Программа: Статус операции {state} недоступен)")

    else:
        transactions = filter_by_state(transactions, state)

    # Сортировка по дате
    print("Программа: Отсортировать операции по дате? Да/Нет\n")
    input_user = input("Пользователь: ")
    input_user = input_user.upper()
    if input_user == "ДА":
        print("Программа: Отсортировать по возрастанию или по убыванию?\n")
        input_user = input("Пользователь: ")
        input_user = input_user.upper()
        if input_user in "ПО ВОЗРАСТАНИЮ":
            transactions = sort_by_date(transactions, False)
        else:
            transactions = sort_by_date(transactions)

    # Выборка только рублевых транзакций
    print("Программа: Выводить только рублевые транзакции? Да/Нет\n")
    input_user = input("Пользователь: ")
    input_user = input_user.upper()
    # transactions_currency_filter = []
    if input_user == "ДА":
        transactions = filter_by_currency(transactions, "RUB")

    # Фильтрация по слову в описании
    print("Программа: Отфильтровать список транзакций по определенному слову в описании? Да/Нет\n")
    input_user = input("Пользователь: ")
    input_user = input_user.upper()
    if input_user == "ДА":
        print("Программа: Введите слово:\n")
        input_user = input("Пользователь: ")
        transactions = process_bank_search(transactions, input_user)

    # Вывод результата запроса
    print("Программа: Распечатываю итоговый список транзакций...\n")
    count = 0
    for item in transactions:
        dt = get_date(item["date"])
        print(f"{dt} {item['description']}")

        mask_account_to = mask_account_card(item["to"])
        if "from" in item:
            if type(item["from"]) is str:
                mask_account_from = mask_account_card(item["from"])
                print(f"{mask_account_from} -> {mask_account_to}")
            else:
                print(f"{mask_account_to}")
        else:
            print(f"{mask_account_to}")

        if "amount" in item:
            print(f"Сумма: {item['amount']} {item['currency_code']}\n")
        else:
            print(f"Сумма: {item['operationAmount']['amount']} {item['operationAmount']['currency']['name']}\n")

        count += 1

    if count > 0:
        print("Программа:")
        print(f"Всего банковских операций в выборке: {count}")

    else:
        print("Программа: Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
