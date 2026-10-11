class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # sonuna əlavə etmə
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node

    # əvvəlinə əlavə etmə
    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # verilmiş elementdən sonra əlavə etmə
    def insert_after(self, target, data):
        current = self.head
        while current is not None and current.data != target:
            current = current.next
        if current is None:
            print(f"{target} siyahıda tapılmadı, əlavə edilmədi.")
            return
        new_node = Node(data)
        new_node.next = current.next
        current.next = new_node

    # element silmə
    def delete(self, value):
        if self.head is None:
            print("Siyahı boşdur.")
            return
        # silinən element birinci düyündürsə
        if self.head.data == value:
            self.head = self.head.next
            return
        prev = self.head
        current = self.head.next
        while current is not None:
            if current.data == value:
                prev.next = current.next
                return
            prev = current
            current = current.next
        print(f"{value} siyahıda tapılmadı, silinmədi.")

    # axtarış
    def search(self, value):
        current = self.head
        while current is not None:
            if current.data == value:
                print("Element tapıldı.")
                return True
            current = current.next
        print("Element tapılmadı.")
        return False

    # uzunluq
    def length(self):
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.next
        return count

    # maksimum və minimum
    def find_max_min(self):
        if self.head is None:
            return None, None
        maximum = minimum = self.head.data
        current = self.head.next
        while current is not None:
            if current.data > maximum:
                maximum = current.data
            if current.data < minimum:
                minimum = current.data
            current = current.next
        return maximum, minimum

    # siyahını tərs çevirmək (yeni siyahı yaratmadan, yalnız göstəriciləri dəyişərək)
    def reverse(self):
        prev = None
        current = self.head
        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def display(self):
        current = self.head
        result = ""
        while current is not None:
            result += str(current.data) + " -> "
            current = current.next
        print(result + "None")


# ---------------- Tapşırıq 10 ----------------
class StudentNode:
    def __init__(self, student_id, student_name, gpa):
        self.student_id = student_id
        self.student_name = student_name
        self.gpa = gpa
        self.next = None


class StudentList:
    def __init__(self):
        self.head = None

    def add_student(self, student_id, student_name, gpa):
        # eyni ID ilə ikinci tələbə əlavə olunmasın
        current = self.head
        while current is not None:
            if current.student_id == student_id:
                print(f"ID {student_id} artıq mövcuddur, əlavə edilmədi.")
                return
            current = current.next
        new_node = StudentNode(student_id, student_name, gpa)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node

    def remove_student(self, student_id):
        if self.head is None:
            print("Siyahı boşdur.")
            return
        if self.head.student_id == student_id:
            self.head = self.head.next
            print(f"ID {student_id} olan tələbə silindi.")
            return
        prev = self.head
        current = self.head.next
        while current is not None:
            if current.student_id == student_id:
                prev.next = current.next
                print(f"ID {student_id} olan tələbə silindi.")
                return
            prev = current
            current = current.next
        print(f"ID {student_id} olan tələbə tapılmadı.")

    def show_all(self):
        if self.head is None:
            print("Siyahıda tələbə yoxdur.")
            return
        print(f"{'ID':<6}{'Ad':<20}{'GPA':<6}")
        print("-" * 32)
        current = self.head
        while current is not None:
            print(f"{current.student_id:<6}{current.student_name:<20}{current.gpa:<6}")
            current = current.next

    def show_high_gpa(self, limit=80):
        found = False
        current = self.head
        while current is not None:
            if current.gpa > limit:
                print(f"{current.student_id:<6}{current.student_name:<20}{current.gpa:<6}")
                found = True
            current = current.next
        if not found:
            print(f"GPA > {limit} olan tələbə yoxdur.")

    def search_by_name(self, name):
        current = self.head
        while current is not None:
            if current.student_name.lower() == name.lower():
                print(f"Tapıldı: ID={current.student_id}, Ad={current.student_name}, GPA={current.gpa}")
                return current
            current = current.next
        print(f"'{name}' adlı tələbə tapılmadı.")
        return None

    def count(self):
        total = 0
        current = self.head
        while current is not None:
            total += 1
            current = current.next
        return total
