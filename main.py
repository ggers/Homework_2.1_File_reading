# cook_book = {
#   'яйчница': [
#     {'ingridient_name': 'яйца', 'quantity': 2, 'measure': 'шт.'},
#     {'ingridient_name': 'помидоры', 'quantity': 100, 'measure': 'гр.'}
#     ],
#   'стейк': [
#     {'ingridient_name': 'говядина', 'quantity': 300, 'measure': 'гр.'},
#     {'ingridient_name': 'специи', 'quantity': 5, 'measure': 'гр.'},
#     {'ingridient_name': 'масло', 'quantity': 10, 'measure': 'мл.'}
#     ],
#   'салат': [
#     {'ingridient_name': 'помидоры', 'quantity': 100, 'measure': 'гр.'},
#     {'ingridient_name': 'огурцы', 'quantity': 100, 'measure': 'гр.'},
#     {'ingridient_name': 'масло', 'quantity': 100, 'measure': 'мл.'},
#     {'ingridient_name': 'лук', 'quantity': 1, 'measure': 'шт.'}
#     ]
#   }

cook_book = {}

def create_cook_book_from_file (filename="data01.txt"):
  with open("data01.txt", encoding= "utf-8") as file:
    for line in file:
      dish_name = line(strip())
      ingridient_count = int(readline())
      for i in range(ingridient_count):
          ingridients = readline().strip()
          ingridients_splitted = ingridients.split(|)
          ingridient_list.append([{'ingridient_name': ingridients_splitted[0]}, {'quantity': ingridients_splitted[1]}, {'measure': ingridients_splitted[2]}]}
          cook_book1.update({dish_name: ingridient_list})
      file.readline()
  return True

def get_shop_list_by_dishes(dishes, person_count):
  shop_list = {}
  for dish in dishes:
    for ingridient in cook_book[dish]:
      new_shop_list_item = dict(ingridient)

      new_shop_list_item['quantity'] *= person_count
      if new_shop_list_item['ingridient_name'] not in shop_list:
        shop_list[new_shop_list_item['ingridient_name']] = new_shop_list_item
      else:
        shop_list[new_shop_list_item['ingridient_name']]['quantity'] += new_shop_list_item['quantity']
  return shop_list

def print_shop_list(shop_list):
  for shop_list_item in shop_list.values():
    print('{} {} {}'.format(shop_list_item['ingridient_name'], shop_list_item['quantity'],
                            shop_list_item['measure']))

def create_shop_list():
  person_count = int(input('Введите количество человек: '))
  dishes = input('Введите блюда в расчете на одного человека (через запятую): ') \
    .lower().split(', ')
  shop_list = get_shop_list_by_dishes(dishes, person_count)
  print_shop_list(shop_list)

create_cook_book_from_file ("data01.txt")
create_shop_list()