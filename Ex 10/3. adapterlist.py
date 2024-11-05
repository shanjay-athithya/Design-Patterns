class AdapterList:
    def __init__(self, data, rows, cols):
        self.data = data
        self.rows = rows
        self.cols = cols

    def get_value_at_index(self, row, col):
        flat_index = row * self.cols + col
        if 0 <= flat_index < len(self.data):
            return self.data[flat_index]
        else:
            return None

if __name__ == '__main__':
    adapter_list = AdapterList([5, 2, 8, 1, 3, 7, 4, 6], rows=2, cols=4)

    # Accessing elements in the adapter list
    for row in range(adapter_list.rows):
        for col in range(adapter_list.cols):
            value = adapter_list.get_value_at_index(row, col)
            print(f"Value at ({row}, {col}): {value}")
