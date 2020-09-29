# Process Scheduler

A Desktop Application to make vizualize the working of Process/Job Scheduling Algorithms.

## Language

Python 3.8.3 (with GUI Library- PyQt5)

## Tools

VS Code, QtDesigner

## How to Use

### Running the python file

1. Make sure you have the python compiler in you system. If not download it from [Python Download](https://www.python.org/downloads/) and install it.
2. Open command prompt and go to the path where you have downloaded the file **ProcessScheduler.py**
3. Type the below command to run the application.
```
py ProcessScheduler.py
```

### Converting QtDesigner file into Python file

1. Make sure you have the PyQt5 installed in your system. If not download it from [PyQt5 Download](https://pypi.org/project/PyQt5/) and install it.
2. Open command prompt and go to the path where you have downloaded the file **ProcessScheduler.ui**
3. Type the below command to convert the QtDesigner file into Python file
```
python -m PyQt5.uic.pyuic -x ProcessScheduler.ui -o ProcessScheduler.py
```
