import os

for object in os.listdir(os.getcwd()):
    if os.path.isfile(object) and object != "run.py":
        path = os.getcwd() + '/' + object
        os.system(f'python -m unittest {path}')
