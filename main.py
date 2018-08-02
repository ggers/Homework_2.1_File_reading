
def create_cook_book_from_file (filename="data01.txt"):
  cook_book = {}
  with open("data01.txt", encoding= "utf-8") as file:
    for line in file:
       ingridient_list = []
       dish_name = line.strip()
       print(f"\nСчитываем из файла блюдо {dish_name}")
       ingridient_count = int(file.readline())
       print(f"В блюде {dish_name} {ingridient_count} ингридиентов\n")
       for i in range(ingridient_count):
           ingridients = file.readline().strip()
#           print(f"Ингридиент № {i+1} это {ingridients}")
           i_s = ingridients.split("|")
#           print(i_s)
           ingridient_list.append(({'ingridient_name': i_s[0]}, {'quantity': i_s[1]}, {'measure': i_s[2]}))
       cook_book.update({dish_name: ingridient_list})
       file.readline()
  return cook_book

def get_shop_list_by_dishes(dishes, person_count, cook_book):
    shop_list = []
# Эта функция получается названия блюд (список) и количество человек (цифра)
# Цикл перебирает блюда и создает список списков ингридиентов для данного блюда, умноженный на число людей
    for dish in dishes:
        new_shop_list_item = []
        for ingridient in cook_book[dish]:
            new_shop_list_item = [[ingridient[0]['ingridient_name'].strip(), int(ingridient[1]['quantity'])*person_count, ingridient[2]['measure'].strip()]]
#            print("\n", new_shop_list_item)
            shop_list += new_shop_list_item
#Однако в нашем списке могут быть повторяющиеся ингридиенты, для этого придется прикрутить проверку как её сделать, я не могу придумать
    return shop_list


def create_shop_list(database):
    person_count = int(input('Введите количество человек: '))
    dishes = input('Введите блюда в расчете на одного человека (через запятую): ') \
    .split(',')
    shop_list = get_shop_list_by_dishes(dishes, person_count, database)
    print("Ваш итоговый список покупок:\n", shop_list)

c = create_cook_book_from_file ("data01.txt")
create_shop_list(c)