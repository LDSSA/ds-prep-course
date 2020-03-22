## How to install Jupyter Notebook in Ubuntu and Mac

### Set up a virtual environment

To create a virtual environment called `env` (you may use whatever name you like), use the command `python3 -m venv env`.

To activate our virtual environment (in order to install and use the specific libraries we want for our current project - this tutorial) you should type the command below.
Notice that once we do, on the leftmost side of the command line, the name of our virtual environment appears in parenthesis:  
```console
source env/bin/activate
(env) 
```

### Install Jupyter Notebook

Make sure your virtual environment is active, and then use pip to install Jupyter Notebook:
```console
(env) pip install notebook
```

You can then open Jupyter Notebook by using the command `jupyter notebook`. Navigate to the folder of SLU00 and you can click on the Learning and Exercise notebooks to open them.
