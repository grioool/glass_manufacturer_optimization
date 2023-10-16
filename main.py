from pulp import *

# 1 Initialize model
glass_manufacturer = LpProblem("Maximize_Manufacturer_Profit", LpMaximize)

# 2 Define the decision variables
A = LpVariable("Wine_glasses", lowBound=0, upBound=6)
B = LpVariable("Beer_glasses", lowBound=0)

# 3 Define Objective function
glass_manufacturer += 5 * A + 4.5 * B

# 4 Define Constraints
glass_manufacturer += 6 * A + 5 * B <= 60
glass_manufacturer += 10 * A + 20 * B <= 150

# 5 Solve model
glass_manufacturer.solve()

# 6 Print
print(glass_manufacturer.status)

print("Produce {} wine glasses".format(A.varValue))
print("Produce {} beer glasses".format(B.varValue))

profit = 5 * A.varValue + 4.5 * B.varValue
print("Glass manufacturer maximum profit is : {}".format(profit))