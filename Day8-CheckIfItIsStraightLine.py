class CheckIfItIsStraightLine:
    def checkStraightLine(self, coordinates):
        if len(coordinates) < 2:
            return False
        if len(coordinates) == 2:
            return True

        x_coordinates = [coordinates[i][0] for i in range(len(coordinates))]
        y_coordinates = [coordinates[i][1] for i in range(len(coordinates))]
        if len(set(x_coordinates)) == 1 or len(set(y_coordinates)) == 1:
            return True
        if coordinates[0][0] != coordinates[1][0]:
            slope_m = (coordinates[1][1] - coordinates[0][1]) / (coordinates[1][0] - coordinates[0][0])
            for i in range(2, len(coordinates)):
                temp_slope = (coordinates[i][1] - coordinates[0][1]) / (coordinates[i][0] - coordinates[0][0])
                if temp_slope != slope_m:
                    return False
        else:
            return False
        return True


obj = CheckIfItIsStraightLine()
print(obj.checkStraightLine([[1, 2], [1, 3], [1, 4]]))
print(obj.checkStraightLine([[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]]))
print(obj.checkStraightLine([[1, 1], [2, 2], [3, 4], [4, 5], [5, 6], [7, 7]]))
print(obj.checkStraightLine([[-3, -2], [-1, -2], [2, -2], [-2, -2], [0, -2]]))
print(obj.checkStraightLine([[-7, -3], [-7, -1], [-2, -2], [0, -8], [2, -2], [5, -6], [5, -5], [1, 7]]))
print(obj.checkStraightLine([[0, 1], [1, 3], [-4, -7], [5, 11]]))
