from ortools.sat.python import cp_model



""""


model = cp_model.CpModel()

num_vals = 4
x = model.new_int_var(0, num_vals - 1, "x")
y = model.new_int_var(0, num_vals - 1, "y")
z = model.new_int_var(0, num_vals - 1, "z")

model.add(x != y)
model.add(x != z)

solver = cp_model.CpSolver()
status = solver.solve(model)
if status == cp_model.OPTIMAL or cp_model.FEASIBLE:
    print(f"X: {solver.value(x)}")
    print(f"Y: {solver.value(y)}")
    print(f"Z: {solver.value(z)}")
else:
    print("No solution!")
"""


"""
class VarArraySolutionPrinter(cp_model.CpSolverSolutionCallback):

    def __init__(self, variables):
        cp_model.CpSolverSolutionCallback.__init__(self)
        self.__variables = variables
        self.__solution_count = 0

    def on_solution_callback(self):
        self.__solution_count += 1
        for v in self.__variables:
            print(f"{v}: {self.value(v)}", end = " ")
        print()

    @property
    def solution_count(self):
        return self.__solution_count
    
solver = cp_model.CpSolver()
solution_printer = VarArraySolutionPrinter([x, y ,z])
solver.parameters.enumerate_all_solutions = True
status = solver.solve(model, solution_printer)

print(f"Status: {solver.status_name(status)}")
print(f"Number of solutions: {solution_printer.solution_count}")

"""

model = cp_model.CpModel()

num_vals = 3
A = model.new_int_var(0, num_vals - 1, "A")
B = model.new_int_var(0, num_vals - 1, "B")
C = model.new_int_var(0, num_vals - 1, "C")
D = model.new_int_var(0, num_vals - 1, "D")
E = model.new_int_var(0, num_vals - 1, "E")
model.add(A != B)
model.add(A != E)
model.add(B != C)
model.add(B != D)
model.add(C != D)
model.add(E != D)



"""
if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
    if(solver.value(A) == 0):
        print("A: Red")
    if(solver.value(A) == 1):
        print("A: Blue")
    if(solver.value(A) == 2):
        print("A: Green")
    
    if(solver.value(B) == 0):
        print("B: Red")
    if(solver.value(B) == 1):
        print("B: Blue")
    if(solver.value(B) == 2):
        print("B: Green")

    if(solver.value(C) == 0):
        print("C: Red")
    if(solver.value(C) == 1):
        print("C: Blue")
    if(solver.value(C) == 2):
        print("C: Green")

    if(solver.value(D) == 0):
        print("D: Red")
    if(solver.value(D) == 1):
        print("D: Blue")
    if(solver.value(D) == 2):
        print("D: Green")

    if(solver.value(E) == 0):
        print("E: Red")
    if(solver.value(E) == 1):
        print("E: Blue")
    if(solver.value(E) == 2):
        print("E: Green")  
    
"""

class VarArraySolutionPrinter(cp_model.CpSolverSolutionCallback):

    def __init__(self, variables):
        cp_model.CpSolverSolutionCallback.__init__(self)
        self.__variables = variables
        self.__solution_count = 0

    def on_solution_callback(self):
        self.__solution_count += 1
        for v in self.__variables:
            if(self.value(v) == 0):
                print(f"{v}: Red", end = " ")
            if(self.value(v) == 1):
                print(f"{v}: Blue", end = " ")
            if(self.value(v) == 2):
                print(f"{v}: Green", end = " ")
        print()

    @property
    def solution_count(self):
        return self.__solution_count
    
solver = cp_model.CpSolver()
solution_printer = VarArraySolutionPrinter([A, B, C, D, E])
solver.parameters.enumerate_all_solutions = True
status = solver.solve(model, solution_printer)

print(f"Number of solutions: {solution_printer.solution_count}")


