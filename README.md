# Gloocel_Pi

Gloocel Raspberry Pi Codebase.

Pi currently has a virtual environment to contain all dependencies

To Start up virtual environment within the my_env directory/folder: source ./bin/activate
To Deactivate the environemnt in venv: Deactivate

Python files/project within a Gloocel_Pi Directory

To install all libraries and modules needed: pip install -r equirements.txt

To run the script/file: Python main.py 

To run the script/file as a 24/7 process: nohup python -u main.py &

NOTE: 
- The command above also outputs logs to a output.txt file within the directory

Lists all python processes: ps aux | grep -i python

To kill the process: kill -9 "PID of the main.py"

## Link to Django Server code
https://github.com/RoyArka/Django_gloocel
