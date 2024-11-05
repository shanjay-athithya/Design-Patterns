from vector import vector

class Centroid:
    def __init__(self, obj1, obj2):
        self.obj1 = obj1
        self.obj2 = obj2

    def centroid_distance(self):
        centroid1 = self.obj1.calculate_centroid()
        centroid2 = self.obj2.calculate_centroid()

        if centroid1 is None or centroid2 is None:
            raise ValueError("One or both objects do not have valid centroids.")
        
        # Assuming centroid is represented as a tuple or list of coordinates
        return vector(centroid1, centroid2).vector_distance()

class ObjectWithCentroid:
    def __init__(self, points):
        self.points = points

    def calculate_centroid(self):
        if not self.points:
            return None
        centroid_x = sum(point[0] for point in self.points) / len(self.points)
        centroid_y = sum(point[1] for point in self.points) / len(self.points)
        return (centroid_x, centroid_y)

if __name__ == "__main__":
    object1 = ObjectWithCentroid([(1, 2), (3, 4), (5, 6)])
    object2 = ObjectWithCentroid([(0, 0), (1, 1), (2, 2)])

    distance_calculator = Centroid(object1, object2)
    distance = distance_calculator.centroid_distance()
    print(f"Centroid Distance between objects: {distance}")