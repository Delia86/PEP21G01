"""
A factory needs an iterable object to keep track of employee working hours for each day.
Each employee has a string name and a tuple containing start work and end work time (use format you like).
Iterating the object will return tuple with name and hours worked that day for each employee
1) 40p: Definition
    a) 10p: Class with constructor that receives the date in the format you desire (representing the day)
    b) 10p: Create method to add worker start time
         - if start time has already been added a custom exception inheriting ValueError (exception: WorkStartError)
         exception will be raised with message indicating employee name and existing start time
    c) 10p: Create method to add worker end time
         - if end time has already been added a custom exception inheriting ValueError (exception: WorkEndError)
         exception will be raised with message indicating employee name and existing end time
    c) 10p: Iterating the object will return tuple with name and hours worked that day for each employee
2) 40p: Execution:
    a) 10p: Create instance of class with date format you selected.
    b) 10p: Add start of work for the following employees:
        - Joe: 09:01:20 - start time
        - Ana: 09:03:15 - start time
        - Tim: 09:04:25 - start time
        - Tim: 09:04:30 - start time - treat this exception
    c) 10p: Add end of work for the following employees:
        - Joe: 16:01:20 - end time
        - Ana: 18:04:15 - end time
        - Tim: 18:05:25 - end time
        - Tim: 18:05:30 - end time - treat this exception
    d) 10p: Iterate the created object and save each value on a new line in a file
3) 20p: Documenting:
   a) 5p: type hints for all arguments (optional for returned values)
   a) 5p: module documentation
   b) 5p: class documentation for all classes
   c) 5p: method documentation for all methods
"""

from datetime import datetime

class WorkerStartError(ValueError):
    pass

class Factory():
    """ Class for keeping track of employee working hours"""

    total_work = {}
    total_diff= []

    def __init__(self, date: list):
        self.date = date


    def __iter__(self):

        for name,datetime in self.total_work.items():
            self.total_diff.append((name,datetime[1]-datetime[0]))

        return FactoryIter(self.total_diff)

    def add_worker_start_time(self, name, start_time: list):
        """Allows user to add start time """

        if self.total_work.get(name,False):

            raise WorkerStartError

        self.start_time =datetime(self.date[0], self.date[1], self.date[2], start_time[0], start_time[1],
                                        start_time[2])

        self.total_work[name] = [self.start_time]


    def add_worker_end_time(self, name, end_time:list):
        """Allows user to add work end time """



        self.end_time = datetime(self.date[0], self.date[1], self.date[2], end_time[0], end_time[1], end_time[2])

        self.total_work[name].append(self.end_time)



class FactoryIter():
    """Class for iterating all working hours"""

    def __init__(self, total_diff:list):
        self.total_diff = total_diff
    def __iter__(self):
        return self

    def __next__(self):
        if not self.total_diff:
            raise StopIteration
        else:
            return self.total_diff.pop(0)


employee = Factory([2021, 5, 23])
employee.add_worker_start_time('Joe',[9,1,20])
employee.add_worker_start_time('Ana',[9,3,15])
employee.add_worker_start_time('Tim',[9,4,25])
try:
    employee.add_worker_start_time('Tim',[9,4,30])
except WorkerStartError:
    pass
employee.add_worker_end_time('Joe',[16,1,20])
employee.add_worker_end_time('Ana',[18,4,15])
employee.add_worker_end_time('Tim',[18,5,25])
employee.add_worker_end_time('Tim',[18,5,30])
print(employee.total_diff)

with open('my_file', 'w') as file:
    for x in employee:
        file.write(str(x) + '\n')
