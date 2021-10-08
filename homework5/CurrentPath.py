import os
import pathlib

print(os.path.abspath(__file__))  # directory of the script being run

print(pathlib.Path(__file__).parent.resolve())  # current working directory
