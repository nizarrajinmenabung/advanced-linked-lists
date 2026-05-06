class MatrixNode:
    def __init__(self, row, col, value):

        self.row = row
        self.col = col
        self.value = value

        self.nextRow = None
        self.nextCol = None


class SparseMatrix:
    def __init__(self, rows, cols):

        self.rows = rows
        self.cols = cols

        self.rowHeads = [None] * rows
        self.colHeads = [None] * cols

    # =========================
    # INSERT
    # =========================
    def insert(self, row, col, value):

        if value == 0:
            return

        newNode = MatrixNode(row, col, value)

        # INSERT ROW
        newNode.nextRow = self.rowHeads[row]
        self.rowHeads[row] = newNode

        # INSERT COLUMN
        newNode.nextCol = self.colHeads[col]
        self.colHeads[col] = newNode

    # =========================
    # DISPLAY
    # =========================
    def display(self):

        for r in range(self.rows):

            current = self.rowHeads[r]

            while current:
                print(
                    f"Row:{current.row} "
                    f"Col:{current.col} "
                    f"Value:{current.value}"
                )

                current = current.nextRow


# =========================
# TEST SPARSE MATRIX
# =========================
sm = SparseMatrix(4, 4)

sm.insert(0, 1, 5)
sm.insert(2, 3, 9)
sm.insert(3, 0, 7)

sm.display()
