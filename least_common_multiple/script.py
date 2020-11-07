import random
import sys
import os
import time

# accept the parameter for the n-th number as a command line parameter
n = int(sys.argv[1])
m = int(sys.argv[2])
os.system("python3 gen.py " + str(n) + " " + str(m) + " >input.txt")
# run the model solution
model_start = time.time()
os.system("python3 my_solution_faster_model.py <input.txt")
model_end = time.time()
model_runtime = model_end - model_start
# run the main solution
main_start = time.time()
os.system("python3 lcm.py <input.txt")
main_end = time.time()
main_runtime = main_end - main_start
# Comparing time
if model_runtime != main_runtime:
    print('model: ', model_runtime*1000, ' main: ', main_runtime*1000)