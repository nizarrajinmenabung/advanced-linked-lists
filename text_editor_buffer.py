class LineNode:
    def __init__(self, text):

        self.text = list(text)

        self.next = None
        self.prev = None


class TextEditorBuffer:
    def __init__(self):

        firstLine = LineNode("\n")

        self.head = firstLine
        self.tail = firstLine

        self.current = firstLine

    # =========================
    # ADD LINE
    # =========================
    def addLine(self, text):

        newNode = LineNode(text + "\n")

        self.tail.next = newNode
        newNode.prev = self.tail

        self.tail = newNode

    # =========================
    # DISPLAY
    # =========================
    def display(self):

        current = self.head

        lineNumber = 1

        while current:

            print(f"{lineNumber}: ", end="")

            for ch in current.text:
                print(ch, end="")

            current = current.next
            lineNumber += 1

    # =========================
    # DELETE LAST LINE
    # =========================
    def deleteLastLine(self):

        if self.tail == self.head:
            return

        self.tail = self.tail.prev
        self.tail.next = None


# =========================
# TEST TEXT EDITOR
# =========================
editor = TextEditorBuffer()

editor.addLine("Hello World")
editor.addLine("Advanced Linked List")
editor.addLine("Python Programming")

print("\nISI TEXT EDITOR:")
editor.display()

editor.deleteLastLine()

print("\nSETELAH DELETE:")
editor.display()
