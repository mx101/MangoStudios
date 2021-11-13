import numpy as np

'''
This class retrieves student data from student_data.txt and stores
it as a list using local memory. 

Provides various filtering functionalities, and cleans data
so that we return requested list of (x-axis, y-axis) tuples
'''

class DataStore:
    def __init__(self):
        self.student_data = []
        f = open("student_data.txt", "r")
        for line in f:
            line = line.strip()
            data_point = {}
            parsed_line = line.split(',')
            for i in range(len(parsed_line)):
                kv = parsed_line[i].split(':')
                try:
                    data_point[kv[0]] = int(kv[1])
                except ValueError:
                    data_point[kv[0]] = kv[1]
            self.student_data.append(data_point)
    
    '''
        Call with no arguments for unfitltered list
    '''
    def getFilteredStudentData(self, major = None, year = 0):
        filtered_data = []
        if major is not None and year != 0:
            for data_point in self.student_data:
                if data_point["major"] == major and data_point["year"] == year:
                    filtered_data.append(data_point)
        elif major is not None:
            for data_point in self.student_data:
                if data_point["major"] == major:
                    filtered_data.append(data_point)
        elif year != 0:
            for data_point in self.student_data:
                if data_point["year"] == year:
                    filtered_data.append(data_point)
        else:
            return self.student_data
        return filtered_data
    
    '''
        Primary part of interface. Returns filtered data with
        specified x-axis and y-axis as the x-coordinates and
        y-coordinates as a list of tuples:
        [(x1, y1), (x2, y2)]

        Parameters
        ------
        xaxis : str
        yaxis : str
        major : str, optional
        year  : int, optional


    '''
    def getXYTuples(self, x_axis, y_axis, major=None, year=0):
        filtered_data = self.getFilteredStudentData(major, year)
        res = []
        for data_point in filtered_data:
            x_coordinate = data_point[x_axis]
            y_coordinate = data_point[y_axis]
            res.append((x_coordinate, y_coordinate))
        return res

    
    

