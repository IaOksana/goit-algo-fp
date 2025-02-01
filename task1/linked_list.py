'''
Завдання 1. Структури даних. Сортування. Робота з однозв'язним списком

Для реалізації однозв'язного списку (приклад реалізації можна взяти з конспекту) необхідно:
- написати функцію, яка реалізує реверсування однозв'язного списку, змінюючи посилання між вузлами;
- розробити алгоритм сортування для однозв'язного списку, наприклад, сортування вставками або злиттям;
- написати функцію, що об'єднує два відсортовані однозв'язні списки в один відсортований список.
'''

class Node:
    def __init__(self, data: int=None):
        self.data = data  # Зберігає дані вузла
        self.next = None  # Посилання на наступний вузол

class LinkedList:
    def __init__(self):
        self.head = None  # Початок списку, спочатку пустий

    def insert_at_beginning(self, data):
        new_node = Node(data)  # Створює новий вузол з даними
        new_node.next = self.head  # Вказує, що новий вузол має посилатися на поточний головний вузол
        self.head = new_node  # Робить новий вузол головним вузлом списку

    def insert_at_end(self, data):
        new_node = Node(data)  # Створює новий вузол з даними
        if self.head is None:  # Якщо список пустий
            self.head = new_node  # Робить новий вузол головним вузлом
        else:
            cur = self.head  # Починає з головного вузла
            while cur.next:  # Проходить до кінця списку
                cur = cur.next
            cur.next = new_node  # Додає новий вузол в кінці списку

    def insert_after(self, prev_node: Node, data):
        if prev_node is None:  # Перевіряє, чи існує попередній вузол
            print("Попереднього вузла не існує.")
            return
        new_node = Node(data)  # Створює новий вузол з даними
        new_node.next = prev_node.next  # Вказує, що новий вузол має посилатися на вузол після попереднього вузла
        prev_node.next = new_node  # Вставляє новий вузол після попереднього вузла

    def delete_node(self, key: int):
        cur = self.head  # Починає з головного вузла
        if cur and cur.data == key:  # Якщо головний вузол містить потрібні дані
            self.head = cur.next  # Робить наступний вузол головним
            cur = None  # Видаляє вузол
            return
        prev = None  # Змінна для зберігання попереднього вузла
        while cur and cur.data != key:  # Проходить список у пошуках потрібних даних
            prev = cur
            cur = cur.next
        if cur is None:  # Якщо вузол з потрібними даними не знайдено
            return
        prev.next = cur.next  # Видаляє вузол з потрібними даними
        cur = None  # Звільняє пам'ять, видаляючи вузол

    def search_element(self, data: int) -> Node | None:
        cur = self.head  # Починає з головного вузла
        while cur:  # Проходить список у пошуках потрібних даних
            if cur.data == data:  # Якщо знайдено потрібні дані
                return cur  # Повертає вузол з потрібними даними
            cur = cur.next
        return None  # Якщо вузол з потрібними даними не знайдено

    def print_list(self):
        current = self.head  # Починає з головного вузла
        while current:  # Проходить весь список
            print(current.data, end=" -> ")  # Виводить дані вузла
            current = current.next  # Переходить до наступного вузла
        print("None")  # Вказує на кінець списку


    """
    Перше завдання: Реверсує однозв'язний список, змінюючи посилання між вузлами.
    """
    def reverse_list(self):
        prev = None
        curr = self.head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        self.head = prev  # Оновлюємо head на нову голову


    ''' Друге завдання: Сортує однозв'язний список за допомогою алгоритму злиттям.'''
    def merge_sort(self):
        # Сортує список злиттям.
        self.head = self._merge_sort(self.head)

    def _merge_sort(self, head):
        # Рекурсивна функція для сортування злиттям.

        if head is None or head.next is None:
            return head

        middle = self._get_middle(head)
        next_of_middle = middle.next
        middle.next = None

        left = self._merge_sort(head)
        right = self._merge_sort(next_of_middle)

        return self._merge(left, right)

    def _get_middle(self, head):
        # Знаходить середину списку.
        if head is None:
            return head

        slow = head
        fast = head

        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next

        return slow

    def _merge(self, left, right):
        # Зливає два відсортовані списки.
        if left is None:
            return right
        if right is None:
            return left

        if left.data <= right.data:
            result = left
            result.next = self._merge(left.next, right)
        else:
            result = right
            result.next = self._merge(left, right.next)

        return result
    

    """ Завдання 3: Функція, що об'єднує два відсортовані однозв'язні списки в один відсортований список
    (other_list: Інший відсортований список (об'єкт LinkedList).) """
    def merge_sorted_lists(self, other_list):
        # 1. Перевірка на пусті списки
        if self.head is None:
            self.head = other_list.head
            return
        if other_list.head is None:
            return

        # 2. Створення фіктивного вузла для спрощення логіки
        dummy = Node() 
        tail = dummy

        # 3. Порівняння та злиття вузлів
        curr1 = self.head
        curr2 = other_list.head
        while curr1 and curr2:
            if curr1.data <= curr2.data:
                tail.next = curr1
                curr1 = curr1.next
            else:
                tail.next = curr2
                curr2 = curr2.next
            tail = tail.next

        # 4. Додавання решти вузлів, якщо один зі списків закінчився раніше
        if curr1:
            tail.next = curr1
        if curr2:
            tail.next = curr2

        # 5. Оновлення head поточного списку
        self.head = dummy.next