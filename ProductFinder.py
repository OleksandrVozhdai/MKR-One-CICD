import datetime

def get_price_changes(file_name, target_product):

    current_date = datetime.datetime.now()
    print(f"Поточна дата: {current_date.strftime('%Y-%m-%d')}")

    last_month_date = current_date - datetime.timedelta(days=30)

    price_changes = []

    try:
        with open(file_name, 'r') as file:
            for line in file:

                product, date_str, price = line.strip().split(', ')

                date = datetime.datetime.strptime(date_str, '%Y-%m-%d')
                price = float(price)

                if product == target_product and last_month_date <= date <= current_date:
                    price_changes.append((date, price))

    except FileNotFoundError:
        print(f"Файл {file_name} не знайдено.")
        return []

    return price_changes



target_product = "Product1"
file_name = "Products.txt"

price_changes = get_price_changes(file_name, target_product)

if price_changes:
    print(f"Зміни цін на '{target_product}' за останній місяць:")
    for date, price in price_changes:
        print(f"Дата: {date.strftime('%Y-%m-%d')}, Ціна: {price} грн.")
else:
    print(f"Зміни цін на '{target_product}' за останній місяць не знайдено.")
