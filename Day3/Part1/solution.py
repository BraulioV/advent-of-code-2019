class Point():
    def __init__(self, x, y):
        self.x, self.y = x, y

    def manhattan_distance(self, point):
        return int(abs(self.x - point.x) + abs(self.y - point.y))

class Segment():

    def __init__(self, start, end):
        self.start = start
        self.end = end

    def intersect(self, segment):
        """https://en.wikipedia.org/wiki/Intersection_(Euclidean_geometry)#Two_line_segments"""
        segment_1 = Point(self.end.x - self.start.x, self.end.y - self.start.y)
        segment_2 = Point(segment.end.x - segment.start.x, segment.end.y - segment.start.y)

        try:
            s = (- segment_1.y * (self.start.x - segment.start.x) + segment_1.x * (self.start.y - segment.start.y)) / (- segment_2.x * segment_1.y + segment_1.x * segment_2.y)
            t = (segment_2.x * (self.start.y - segment.start.y) - segment_2.y * (self.start.x - segment.start.x)) / (- segment_2.x * segment_1.y + segment_1.x * segment_2.y)
        except ZeroDivisionError:
            return None

        if s >= 0 and s <= 1 and t >= 0 and t <= 1:
            # Both segments intersect
            intersection_x = self.start.x + (t * segment_1.x)
            intersection_y = self.start.y + (t * segment_1.y)
            return Point(intersection_x, intersection_y)

    def __repr__(self):
        return "({},{}; {},{})".format(self.start.x, self.start.y, self.end.x, self.end.y)

class Wire():
    def __init__(self, raw_data):
        current_point = Point(0,0)
        self.segments = []

        for movement in raw_data.split(','):
            direction, quantity = movement[0], int(movement[1:])
            aux_point = current_point
            if direction == 'R':
                current_point = Point(current_point.x + quantity, current_point.y)
            elif direction == 'U':
                current_point = Point(current_point.x, current_point.y + quantity)
            elif direction == 'L':
                current_point = Point(current_point.x - quantity, current_point.y)
            elif direction == 'D':
                current_point = Point(current_point.x, current_point.y - quantity)

            self.segments.append(Segment(aux_point, current_point))

    def intersections_with_wire(self, wire):
        intersection_points = []

        # Skip the first point, it isn't needed
        for my_segment in self.segments[1:]:
            for other_segment in wire.segments:
                if (intersection := my_segment.intersect(other_segment)) is not None:
                    intersection_points.append(intersection)

        return intersection_points


with open("../data/input") as f:
    first_wire = Wire(f.readline())
    second_wire = Wire(f.readline())

minimun_distance = sorted([intersection.manhattan_distance(Point(0,0))
                            for intersection in first_wire.intersections_with_wire(second_wire)])[0]

print("Minimun distance is {}".format(minimun_distance))
