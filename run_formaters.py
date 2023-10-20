import os

print('run autopep8')
os.system("autopep8 ./src --recursive --in-place -a")

print('run autoflake')
os.system("autoflake --in-place --remove-all-unused-imports --remove-unused-variables -r ./src")

print('run unify')
os.system("unify --in-place -r ./src/")

