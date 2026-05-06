class StudentNode:
    def __init__(self, student_id, name):

        self.student_id = student_id
        self.name = name

        self.nextById = None
        self.nextByName = None


class MultiLinkedList:
    def __init__(self):

        self.headById = None
        self.headByName = None

    # =========================
    # INSERT BY ID
    # =========================
    def insert(self, student_id, name):

        newNode = StudentNode(student_id, name)

        # ======================
        # INSERT CHAIN ID
        # ======================
        if self.headById is None or student_id < self.headById.student_id:

            newNode.nextById = self.headById
            self.headById = newNode

        else:

            current = self.headById

            while current.nextById and current.nextById.student_id < student_id:
                current = current.nextById

            newNode.nextById = current.nextById
            current.nextById = newNode

        # ======================
        # INSERT CHAIN NAME
        # ======================
        if self.headByName is None or name < self.headByName.name:

            newNode.nextByName = self.headByName
            self.headByName = newNode

        else:

            current = self.headByName

            while current.nextByName and current.nextByName.name < name:
                current = current.nextByName

            newNode.nextByName = current.nextByName
            current.nextByName = newNode

    # =========================
    # DISPLAY BY ID
    # =========================
    def displayById(self):

        current = self.headById

        while current:
            print(current.student_id, current.name)
            current = current.nextById

    # =========================
    # DISPLAY BY NAME
    # =========================
    def displayByName(self):

        current = self.headByName

        while current:
            print(current.student_id, current.name)
            current = current.nextByName


# =========================
# TEST MULTI LIST
# =========================
ml = MultiLinkedList()

ml.insert(103, "Budi")
ml.insert(101, "Andi")
ml.insert(102, "Caca")

print("\nSORT BY ID")
ml.displayById()

print("\nSORT BY NAME")
ml.displayByName()
