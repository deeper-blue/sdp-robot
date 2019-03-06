# QA selection and run script.
#
# Author(s):
#   Filip Smola

from test.qa import *

message = """Available Quantitative Analyses:
    0) Exit
    1) Independent Arch
    2) Independent Platform
    3) Independent Grabber
    4) Grabber In-Place
    5) Integrated One Move
    6) Integrated Continuous Moves"""

separator = "=========="

while True:
    print(message)
    n = input("Select a number:")

    print(separator)
    if n == 1:
        arch_indep.run()
    elif n == 2:
        platform_indep.run()
    elif n == 3:
        grabber_indep.run()
    elif n == 4:
        grabber_in_place.run()
    elif n == 5:
        integrated_one.run()
    elif n == 6:
        integrated_continuous.run()
    else:
        break
    print(separator)

print("Exiting...")
