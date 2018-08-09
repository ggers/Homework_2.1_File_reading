
def create_cook_book_from_file(filename="data01.txt"):
  cook_book = {}
  with open("data01.txt", encoding="utf-8") as file:
    for line in file:
       ingridient_list = []
       dish_name = line.strip()
       print(f"\nСчитываем из файла блюдо {dish_name}")
       ingridient_count = int(file.readline())
       print(f"\nВ блюде {dish_name} {ingridient_count} ингридиентов")
       for i in range(ingridient_count):
           ingridients = file.readline().strip()
           print(f"Ингридиент № {i+1} это {ingridients}")
           i_s = ingridients.split("|")
#           print(i_s)
           ingridient_list.append({'ingridient_name': i_s[0].strip(), 'quantity': int(i_s[1]), 'measure': i_s[2].strip()})
#           print("список вспомогательный", ingridient_list)
       cook_book.update({dish_name: ingridient_list})
       file.readline()
#       print(cook_book)
  return cook_book

def get_shop_list_by_dishes(dishes, person_count, cook_book):
    shop_list = {}
# Эта функция получается названия блюд (список), количество человек (цифра) и книгу рецептов
# Цикл перебирает блюда и создает список списков ингридиентов для данного блюда, умноженный на число людей
    for dish in dishes:
        for ingridient in cook_book[dish]:
            new_shop_list_item = dict(ingridient)
            new_shop_list_item['quantity'] *= person_count
# Проверка для пересекающихся ингридиентов
            if new_shop_list_item['ingridient_name'] not in shop_list:
                shop_list[new_shop_list_item['ingridient_name']] = new_shop_list_item
            else:
                shop_list[new_shop_list_item['ingridient_name']]['quantity'] += new_shop_list_item['quantity']
# Уродливый цикл для удаления лишнего названия ингридиента
    for i in shop_list.values():
        del i['ingridient_name']
    print("Наш итоговый список покупок в виде словаря\n", shop_list)
    return shop_list

def print_shop_list(shop_list):
    print("\nНаш итоговый список покупок:")
    for key, value in shop_list.items():
        print("{} {} {}".format(key, value['quantity'], value['measure']))

def create_shop_list(database):
    person_count = int(input('Введите количество человек: '))
    dishes = input('Введите блюда в расчете на одного человека (через запятую): ') \
    .split(',')
    shop_list = get_shop_list_by_dishes(dishes, person_count, database)
    print_shop_list(shop_list)


create_shop_list(create_cook_book_from_file ("data01.txt"))