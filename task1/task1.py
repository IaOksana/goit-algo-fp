from linked_list import LinkedList

def main():
    llist = LinkedList()

    # Вставляємо вузли в початок
    llist.insert_at_beginning(5)
    llist.insert_at_beginning(10)
    llist.insert_at_beginning(13)
    llist.insert_at_beginning(100)
    llist.insert_at_beginning(-10)
    llist.insert_at_beginning(15)
    # Вставляємо вузли в кінець
    llist.insert_at_end(20)
    llist.insert_at_end(25)

    # Друк зв'язного списку
    print("Зв'язний список:")
    llist.print_list()

    print("\nЗавдання 1: Реверс однозв'язного списку")
    print("Зв'язний список після реверсу:")
    llist.reverse_list()
    llist.print_list()

    print("\nЗавдання 2: Реверс однозв'язного списку. Викуристовуємо метод злиття для сортування однозв'язного списку")
    llist.merge_sort()
    print("Зв'язний список після сортування:")
    llist.print_list()

    print("\nЗавдання 3: Об'єднання двух відсортованих однозв'язних списки в один відсортований список")
    # Другий список створюємо
    llist2 = LinkedList()
    llist2.insert_at_beginning(5)
    llist2.insert_at_beginning(10)
    llist2.insert_at_beginning(-13)
    llist2.insert_at_beginning(150)
    llist2.insert_at_beginning(-10)
    llist2.insert_at_beginning(15)
    llist2.insert_at_end(40)
    llist2.insert_at_end(-35)
    print("Другий зв'язний список:")
    llist2.print_list()
    llist2.merge_sort()
    print("Другий зв'язний список після сортування:")
    llist2.print_list()

    llist.merge_sorted_lists(llist2)
    print("\nЗв'язний список після злиття:")
    llist.print_list()






if __name__ == '__main__':
        main()