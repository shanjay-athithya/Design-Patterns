class BasicList:
    def __init__(self, data):
        self.data = data
        
    def get_value(self, index):
        if 0 <= index < len(self.data):
            return self.data[index]
        else:
            raise IndexError("Index out of range")
        
    def sort(self):
        self.data.sort()
        return self.data
    
if __name__ == "__main__":
    my_list = BasicList([5, 2, 8, 1, 3, 7, 4, 6])
    # Get value at index
    try:
        value = my_list.get_value(2)
        print("Value at index 2:", value)
    except IndexError as e:
        print(e)
    sorted_list = my_list.sort()
    print("Sorted List:", sorted_list)

    