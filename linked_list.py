"""
BCP 210 - Assignment 2: Linked Lists
University Helpdesk Ticket Queue (Singly Linked List)
"""


class Ticket:
    def __init__(self, ticket_id, student_name, issue):
        self.ticket_id = ticket_id
        self.student_name = student_name
        self.issue = issue
        self.next = None


class TicketQueue:
    def __init__(self):
        self.head = None

    def enqueue(self, ticket_id, student_name, issue):
        """Add a new ticket to the end of the queue. Time: O(n)"""
        new_node = Ticket(ticket_id, student_name, issue)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def priority_insert(self, after_ticket_id, ticket_id, student_name, issue):
        """Insert a new ticket immediately after the given ticket ID.
        Time: O(n)
        """
        current = self.head
        while current:
            if current.ticket_id == after_ticket_id:
                new_node = Ticket(ticket_id, student_name, issue)
                new_node.next = current.next
                current.next = new_node
                return True
            current = current.next
        return False  # after_ticket_id not found

    def resolve(self, ticket_id):
        """Delete the ticket with the given ID. Time: O(n)"""
        current = self.head
        prev = None
        while current:
            if current.ticket_id == ticket_id:
                if prev is None:
                    self.head = current.next
                else:
                    prev.next = current.next
                return True
            prev = current
            current = current.next
        return False  # ticket not found

    def find_middle(self):
        """Find the middle ticket using fast/slow pointers. Time: O(n)"""
        if self.head is None:
            return None
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def reverse(self):
        """Reverse the queue in-place. Time: O(n)"""
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def display(self):
        """Print all tickets. Time: O(n)"""
        current = self.head
        if not current:
            print("Queue is empty.")
            return
        while current:
            print(f"[{current.ticket_id}] {current.student_name} - {current.issue}")
            current = current.next


def run_demo():
    queue = TicketQueue()
    queue.enqueue(101, "Ama", "Cannot login")
    queue.enqueue(102, "Kojo", "Printer not working")
    queue.enqueue(103, "Yaw", "Wi-Fi issue")
    queue.enqueue(104, "Esi", "Slow laptop")

    print("Initial queue:")
    queue.display()

    queue.priority_insert(102, 999, "Abena", "URGENT: server down")
    print("\nAfter priority insert after ticket 102:")
    queue.display()

    queue.resolve(103)
    print("\nAfter resolving ticket 103:")
    queue.display()

    middle = queue.find_middle()
    print(f"\nMiddle ticket: {middle.ticket_id if middle else None}")

    queue.reverse()
    print("\nAfter reversing queue:")
    queue.display()


def run_tests():
    """Edge-case and typical-case tests."""
    q = TicketQueue()
    assert q.find_middle() is None
    q.display()  # empty queue, should not crash

    q.enqueue(1, "A", "issue1")
    assert q.find_middle().ticket_id == 1
    assert q.resolve(99) is False  # not found
    assert q.resolve(1) is True
    assert q.head is None

    q.enqueue(1, "A", "i1")
    q.enqueue(2, "B", "i2")
    q.enqueue(3, "C", "i3")
    assert q.priority_insert(2, 99, "Z", "urgent") is True
    ids = []
    node = q.head
    while node:
        ids.append(node.ticket_id)
        node = node.next
    assert ids == [1, 2, 99, 3]

    assert q.find_middle().ticket_id == 99

    q.reverse()
    ids = []
    node = q.head
    while node:
        ids.append(node.ticket_id)
        node = node.next
    assert ids == [3, 99, 2, 1]

    print("All tests passed.")


if __name__ == "__main__":
    run_demo()
    print()
    run_tests()