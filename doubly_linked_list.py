class DListNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # =========================
    # INSERT
    # =========================
    def insert(self, value):
        newNode = DListNode(value)

        # LIST KOSONG
        if self.head is None:
            self.head = self.tail = newNode
            return

        # INSERT DEPAN
        if value < self.head.data:
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode
            return

        # INSERT BELAKANG
        if value > self.tail.data:
            newNode.prev = self.tail
            self.tail.next = newNode
            self.tail = newNode
            return

        # INSERT TENGAH
        current = self.head

        while current.data < value:
            current = current.next

        newNode.next = current
        newNode.prev = current.prev

        current.prev.next = newNode
        current.prev = newNode

    # =========================
    # TRAVERSAL FORWARD
    # =========================
    def forwardTraversal(self):
        current = self.head

        while current is not None:
            print(current.data, end=" <-> ")
            current = current.next

        print("NULL")

    # =========================
    # TRAVERSAL REVERSE
    # =========================
    def reverseTraversal(self):
        current = self.tail

        while current is not None:
            print(current.data, end=" <-> ")
            current = current.prev

        print("NULL")

    # =========================
    # SEARCH
    # =========================
    def search(self, target):
        current = self.head

        while current is not None:
            if current.data == target:
                return True

            current = current.next

        return False

    # =========================
    # DELETE
    # =========================
    def delete(self, value):

        if self.head is None:
            return

        current = self.head

        while current is not None:

            if current.data == value:

                # DELETE HEAD
                if current == self.head:
                    self.head = current.next

                    if self.head:
                        self.head.prev = None

                # DELETE TAIL
                elif current == self.tail:
                    self.tail = current.prev
                    self.tail.next = None

                # DELETE TENGAH
                else:
                    current.prev.next = current.next
                    current.next.prev = current.prev

                return

            current = current.next


# =========================
# TEST DLL
# =========================
dll = DoublyLinkedList()

dll.insert(40)
dll.insert(10)
dll.insert(30)
dll.insert(20)
dll.insert(50)

print("FORWARD:")
dll.forwardTraversal()

print("REVERSE:")
dll.reverseTraversal()

print("SEARCH 30:", dll.search(30))

dll.delete(30)

print("SETELAH DELETE 30:")
dll.forwardTraversal()
