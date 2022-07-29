# Author: Dennis Lam
# GitHub username: dennislam4
# Date: 7/28/2022
# Description: Two classes, one is named Point which takes two arguments, x_coordinate and y_coordinate and returns the
# distance between two different Point objects. The other named LineSegment, takes two data members, endpoint_1 and
# endpoint_2 and returns the distance between the two end points.

class Point:
    """A class that represents two coordinates of a point."""
    def __init__(self, x_coordinate, y_coordinate):
        """Initializes x and y coordinates."""
        self._x_coord = x_coordinate
        self._y_coord = y_coordinate

    def get_x_coord(self):
        """Returns x-coordinate."""
        return self._x_coord

    def get_y_coord(self):
        """Returns y_coordinate."""
        return self._y_coord

    def distance_to(self, point):
        """Returns distance between two different points."""
        x_coordinate = (self._x_coord - point.get_x_coord()) * (self._x_coord - point.get_x_coord())
        y_coordinate = (self._y_coord - point.get_y_coord()) * (self._y_coord - point.get_y_coord())
        return (x_coordinate + y_coordinate) ** 0.5


class LineSegment:
    """A class that represents the endpoints of a line segment."""
    def __init__(self, endpoint_1, endpoint_2):
        """Initializes both endpoints."""
        self._endpoint_1 = endpoint_1
        self._endpoint_2 = endpoint_2

    def get_endpoint_1(self):
        """Returns the first endpoint."""
        return self._endpoint_1

    def get_endpoint_2(self):
        """Returns the second endpoint."""
        return self._endpoint_2

    def length(self):
        """Returns the distance between both endpoints."""
        return self._endpoint_1.distance_to(self._endpoint_2)

    def slope(self):
        """Returns the slope of LineSegment."""
        x_coordinate = self._endpoint_2.get_x_coord() - self._endpoint_1.get_x_coord()
        y_coordinate = self._endpoint_2.get_y_coord() - self._endpoint_1.get_y_coord()
        return y_coordinate / x_coordinate

    def is_parallel_to(self, line_seg_2):
        """
        Returns True if the LineSegment method is being called on is parallel to the one being passed as the argument.
        If not, False is returned.
        """
        if self.slope() == line_seg_2.slope():
            return True
        else:
            return False
