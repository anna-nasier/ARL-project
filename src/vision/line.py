import math

class Line3D:
    def __init__(self, x1=0, y1=0, z=0, x2=0, y2=0, color = None):
        self.x1 = x1
        self.y1 = y1
        self.z = z
        self.x2 = x2
        self.y2 = y2
        self.color = color

    def set_coordinates(self, x1, y1, z, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.z = z
        self.x2 = x2
        self.y2 = y2

    def get_coordinates(self):
        return (self.x1, self.y1, self.z), (self.x2, self.y2, self.z), self.color

    def calculate_length(self):
        length = math.sqrt((self.x2 - self.x1)**2 + (self.y2 - self.y1)**2)
        return length

    def calculate_world(self, width, height):
        room_width = 4.5
        room_height = 6.3   
        x_factor = room_width/width
        y_factor = room_height/height
        # print(x_factor, y_factor)
        self.x1_w = round(self.x1 * x_factor, 2)
        self.x2_w = round(self.x2 * x_factor, 2)
        self.y1_w = round(self.y1 * y_factor, 2)
        self.y2_w = round(self.y2 * y_factor, 2)


def find_close_points(lines, proximity_threshold):
    close_points = {}
    
    for i, line in enumerate(lines):
        close_points[i] = []
        points1, points2 = line.get_coordinates()

        for j, other_line in enumerate(lines):
            if i != j:
                other_points1, other_points2 = other_line.get_coordinates()
                for point1 in points1:
                    for other_point1 in other_points1:
                        distance = math.sqrt((point1[0] - other_point1[0])**2 + (point1[1] - other_point1[1])**2 + (point1[2] - other_point1[2])**2)
                        if distance < proximity_threshold:
                            close_points[i].append(j)
                            break
                    if close_points[i]:
                        break

                for point2 in points2:
                    for other_point2 in other_points2:
                        distance = math.sqrt((point2[0] - other_point2[0])**2 + (point2[1] - other_point2[1])**2 + (point2[2] - other_point2[2])**2)
                        if distance < proximity_threshold:
                            close_points[i].append(j)
                            break
                    if close_points[i]:
                        break

    return close_points

# Example usage:
# line1 = Line3D(1, 2, 3, 4, 5, 6)
# line2 = Line3D(2, 3, 4, 5, 6, 7)
# line3 = Line3D(7, 8, 9, 10, 11, 12)

# lines = [line1, line2, line3]

# # Find points close to each line within a proximity threshold of 2.0
# close_points = find_close_points(lines, 2.0)
# print(close_points)