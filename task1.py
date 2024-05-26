class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    def insert_after(self, prev_node: Node, data):
        if prev_node is None:
            print("Попереднього вузла не існує.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key: int):
        cur = self.head
        if cur and cur.data == key:
            self.head = cur.next
            cur = None
            return
        prev = None
        while cur and cur.data != key:
            prev = cur
            cur = cur.next
        if cur is None:
            return
        prev.next = cur.next
        cur = None

    def search_element(self, data: int) -> Node | None:
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None

    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

    # реверсування списку
    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    # сортування    
    def insertion_sort(self):
        if self.head is None:
            return
        sorted_list = LinkedList()
        current = self.head
        while current:
            next_node = current.next
            self.sorted_insert(sorted_list, current)
            current = next_node
        self.head = sorted_list.head
    
    def sorted_insert(self, llist, new_node):
        if llist.head is None or llist.head.data >= new_node.data:
            new_node.next = llist.head
            llist.head = new_node
            return
        current = llist.head
        while current.next and current.next.data < new_node.data:
            current = current.next
        new_node.next = current.next
        current.next = new_node

    def merge_sorted_lists(self, other_list):
        merged_list = LinkedList()
        cur1, cur2 = self.head, other_list.head
        while cur1 and cur2:
            if cur1.data < cur2.data:
                merged_list.insert_at_end(cur1.data)
                cur1 = cur1.next
            else:
                merged_list.insert_at_end(cur2.data)
                cur2 = cur2.next
        while cur1:
            merged_list.insert_at_end(cur1.data)
            cur1 = cur1.next
        while cur2:
            merged_list.insert_at_end(cur2.data)
            cur2 = cur2.next
        return merged_list


llist = LinkedList()

# Вставляємо вузли в початок
llist.insert_at_beginning(5)
llist.insert_at_beginning(10)
llist.insert_at_beginning(15)

# Вставляємо вузли в кінець
llist.insert_at_end(20)
llist.insert_at_end(25)

# Друк зв'язного списку
print("Зв'язний список:")
llist.print_list()

# Видаляємо вузол
llist.delete_node(10)

print("\nЗв'язний список після видалення вузла з даними 10:")
llist.print_list()

# Пошук елемента у зв'язному списку
print("\nШукаємо елемент 15:")
element = llist.search_element(15)
if element:
    print(element.data)

# Друк зв'язного списку
print("Зв'язний список:")
llist.print_list()

# Реверсування та друк зв'язного списку
print("Реверсований зв'язний список:")
llist.reverse()
llist.print_list()

# Сортування та друк зв'язного списку
print("Відсортований список:")
llist.insertion_sort()
llist.print_list()

llist2 = LinkedList()
llist2.insert_at_beginning(1)
llist2.insert_at_beginning(3)
llist2.insert_at_beginning(17)

# Обєднання та друк зв'язного списку
print("Обєднання списків:")
llist2.insertion_sort()
new_list = llist.merge_sorted_lists(llist2)
new_list.print_list()


