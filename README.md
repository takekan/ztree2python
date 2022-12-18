# ztree2python

ztree2python imports a data file created by z-Tree into python as pandas dataframes.
This function inputs the "filename" of a z-Tree data file, and it returns a dictionary, which contains the dataframes of the tables.
The keys are the names of all tables, "globals", "subjects", and so on. The value associated with each key is a pandas dataframe for the table.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
pip install ztree2python
```

Alternatively, simply put ztree2python.py and a z-Tree data file (e.g., 221215_1236.xls) in the current directory or the working directory. 

## Usage

```python
from ztree2python import ztree2python as ztree2python

# input the file name, and it returns a dictionary.  
df = ztree2python('221215_1236.xls')

# Extract a table by name, for example, the "subjects" table.
my_table = (df['subjects'])
my_table.head()

# The output also contains a series of table names. See the list.
tables['list_tables']

# Display all the tables in the df.
for name, tbl in tables.items():
  display(tbl)
```

## A sample data

from ztree2python import ztree2python as ztree2python
tables = ztree2python('221215_1449.xls')

## License

[MIT](https://choosealicense.com/licenses/mit/)

## Reference
Fischbacher, U. (2007). z-Tree: Zurich toolbox for ready-made economic experiments. Experimental Economics, 10(2), 171-178. 
https://doi.org/10.1007/s10683-006-9159-4.

Takeuchi, K. (2023?). ztree2stata: A data converter for z-Tree and Stata users. Journal of the Economic Science Association, R&R.

I would appreciate it if you cite this code in a footnote or acknowledgement (or you can even add this to the list of references!)

Takeuchi, Kan. (2022). ztree2python.py, http://github.com/takekan/ztree2python.)
