"""
A shoe factory needs an iterable object to keep track of shoes produces by each worker each day.
Each worker has a string name and each shoe has an int serial number.
Object will have an instance variable tha will keep track of workers trying to cheat in the form of a list of names.
Iterating the object will return the serial numbers produced that day by all workers
1) 40p: Definition
    a) 5p: Class with constructor that receives the date in the format you desire
    b) 25p: Method for adding work done by worker
        - 5p: argument: 5p
            - 1 receives worker name as string
            - 2 receives series produced as list of ints
        - 10p: using this method more then once for the same worker allows the worker to add new values but not
            retransmit old values .In case existing value is entered by two workers a specific exception
            (DuplicateDataException - created by you) and inheriting ValueError will be raised.
            (ex name1: 100, 101; name1: 101, 102; results in exception DuplicateDataException) 10p
        - 10p: method validates that series introduced do not already belong to another worker. In case of conflict
            series will be removed from both workers and information will be added to instance variable that tracks
            cheating workers and then ValueError with message: "Conflict series: <series>, Workers: <nume1>, <nume2>"
            will be raised
    c) 10p: Iterating this object will return an instance of an iterator that will have all series produced that day
2) 40p: Execution:
    a) 10p: Create instance of class with date format you selected.
    b) 10p: Add data for the following workers:
        - Joe: 402, 403, 409
        - Ana: 399, 404, 405
        - Tim: 400, 401, 406
        - workerX: 406, 407, 408 - after adding workerX, workerX will have 407, 408 and Tim will have 400, 401
    c) 10p: Add data for Tim: 400, 401 and check that DuplicateDataException is raised
    d) 10p: Iterate the created object and save each value on a new line in a file
3) 20p: Documenting:
   a) 5p: type hints for all arguments (optional for returned values)
   a) 5p: module documentation
   b) 5p: class documentation for all classes
   c) 5p: method documentation for all methods
"""

#
# class DuplicateDataException(ValueError):
#     pass
#
# class ShoeFact():
#     shoes=[]
#     workers=[]
#     work_done={} #dict workers and series evidence
#     def __init__(self,date:str):
#         self.date=date
#     def __iter__(self):
#         return ShoeIter()
#     def add_shoes_series(self,name:str , series:list):
#         try:
#             values=self.work_done[name]
#         except KeyError:
#             values=[]
#         if set(values).intersection(set(series)):#sets
#              raise DuplicateDataException(set(values).intersection(set(series)))
#
#         for worker_name,worker_series in self.work_done.items():
#             if set(series).intersection(set(worker_series)):
#                 for duplicate in set(series).intersection(set(worker_series)):
#                     series.remove(duplicate)
#                     self.work_done[worker_name].remove(duplicate)
#                 raise ValueError('Conflict series:',)
#
#
#
#         self.work_done[name]=series
#
#
# class ShoeIter():
#     def __iter__(self):
#         return self
#     def __next__(self):
#         pass
# shoe1=ShoeFact("04.05.2021")
# shoe1.add_shoes_series("Jerry",[124,125,126])
# shoe1.add_shoes_series("All",[127,128,129])
# # shoe1.add_shoes_series("All",[130,131,129])
# print(shoe1.work_done)
#
# Andrei
# class DuplicateDataException(ValueError):
#     pass
# class ShoeFact():
#     shoes=[]
#     workers=[]
#     work_done={}
#     def __init__(self,date:str):
#         self.date=date
#     def __iter__(self):
#         return ShoeIter()
#     def add_shoes_series(self,name:str , series:list):
#         try:
#             values=self.work_done[name]
#         except KeyError:
#             values=[]
#         if set(values).intersection(set(series)):
#              raise DuplicateDataException(set(values).intersection(set(series)))
#
#         self.work_done[name]=series
#
#
# class ShoeIter():
#     def __iter__(self):
#         return self
#     def __next__(self):
#         pass
# shoe1=ShoeFact("04.05.2021")
# shoe1.add_shoes_series("Jerry",[124,125,126])
# shoe1.add_shoes_series("Pompiliu",[127,128,129])
# # shoe1.add_shoes_series("Pompiliu",[130,131,129])
# print(shoe1.work_done)
#
#

# Mario
class DuplicateDataException(ValueError):
    pass


class ShoeFact(): #-> obiectul iterabil
    """Class to track work progress """# documentatie clase
    shoes = []
    workers = {}
    work_done = {}
    def __init__(self, date:str):
        self.date = date #->instance variable punctul a)
    def __iter_(self): #-> trebuie sa returneze o instanta din obj iterabil
        all_series=[]
        for series in self.work_done.values():
            all_series.extend(series)


        return ShoeIter(all_series)

    def add_shoes_series(self, name:str, series:list): #1b1)
        """Allows user to add work done""" # documentare metode
        conflict=0
        try:
            values = self.work_done[name]
        except KeyError:
            values = []
        if set(values).intersection(set(series)):
            raise DuplicateDataException(set(values).intersection(set(series))) #1b2)
        for worker_name, worker_series in self.work_done.items():
            if set(series).intersection(set(worker_series)):
                for duplicate in set(series).intersection(set(worker_series)):
                    series.remove(duplicate)
                    self.work_done[worker_name].remove(duplicate)#seria care intra in conflict
                    self.workers[duplicate]=(worker_name,name)
                conflict=1
        self.work_done[name] = series
        if conflict:
            raise ValueError(f"Conflict series:, {duplicate}, Workers: {name}, {worker_name}")


class ShoeIter():
    """Class for iterating all series """
    def __init__(self,series:list):
        self.series=series
    def __iter__(self):
        return self               #-> iter returneaza tot timpul self
    def __next__(self):
        if not self.series:
            raise StopIteration
        else:
            return self.series.pop(0)


shoes1 = ShoeFact("07.04.2021")
shoes1.add_shoes_series("Jerry", [124, 125, 126])
shoes1.add_shoes_series("Tom", [224, 225, 226])
shoes1.add_shoes_series("Gigel", [245, 240, 241])

print(shoes1.work_done)

with open('file','w') as file:
    for i in shoes:
        file.write (str(i)+'\n')


# Iulian
#
# class DuplicateDataException(ValueError):
#     pass
# class ShoeFact(): #-> obiectul iterabil
#     shoes = []
#     workers = []
#     work_done = {}
#     def __init__(self, date:str):
#         self.date = date #->instance variable punctul a)
#     def __iter_(self): #-> trebuie sa returneze o instanta din obj iterabil
#         return ShoeIter()
#     def add_shoes_series(self, name:str, series:list): #1b1)
#         try:
#             values = self.work_done[name]
#         except KeyError:
#             values = []
#         if set(values).intersection(set(series)):
#             raise DuplicateDataException(set(values).intersection(set(series))) #1b2)
#         for worker_name, worker_series in self.work_done.items():
#             if set(series).intersection(set(worker_series)):
#                 for duplicate in set(series).intersection(set(worker_series)):
#                     series.remove(duplicate)
#                     self.work_done[worker_name].remove(duplicate)
#                 raise ValueError(f"Conflict series:, {duplicate}, Workers: {name}, {worker_name}")
#         self.work_done[name] = series
# class ShoeIter():
#     def __iter__(self):
#         return self               #-> iter returneaza tot timpul self
#     def __next__(self):
#         pass
# shoes1 = ShoeFact("07.04.2021")
# shoes1.add_shoes_series("Jerry", [124, 125, 126])
# # shoes1.add_shoes_series("Jerry", [124, 129, 130])
# shoes1.add_shoes_series("Tom", [223, 225, 226])
# shoes1.add_shoes_series("Gigel", [224, 240, 241])
# print(shoes1.work_done)