class vector:
    def __init__(self, vector1, vector2):
        self.vector1 = vector1
        self.vector2 = vector2

    def vector_distance(self):
        if len(self.vector1) != len(self.vector2):
            raise ValueError("Vectors must have the same dimension")
        
        squared_distance = sum((x - y) ** 2 for x, y in zip(self.vector1, self.vector2))
        return (squared_distance) ** 0.5
    
if __name__ == "__main__":
    vector1 = [1, 2, 3]
    vector2 = [4, 5, 6]

    distance_calculator = vector(vector1, vector2)
    distance = distance_calculator.vector_distance()
    print(f"Euclidean Distance between vectors: {distance}")
