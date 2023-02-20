# ztree2python

ztree2python imports a data file created by z-Tree (Fischbacher, 2007) into python as pandas dataframes.
This function inputs the "filename" of a z-Tree data file, and it returns a dictionary, which contains the dataframes of the tables.
The keys are the names of all tables, "globals", "subjects", and so on. The value associated with each key is a pandas dataframe for the table.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install.

```bash
pip install ztree2python
```

Alternatively, simply put ztree2python.py and a z-Tree data file (e.g., 221215_1449.xls) in the current directory or the working directory. 

## Usage
The ztree2python is a simple function that takes the filename of a z-Tree data file as the argument and returns a dictionary that contains all of the tables in the z-Tree data file.
```python
from ztree2python import ztree2python as z2p

# input the file name, and it returns a dictionary.  
tables = z2p('221215_1449.xls')
```
The function returns a dictionary. Each table is stored as a dataframe in the ```tables```. Get the data of a table as follows:
```python
# Extract a table by name, for example, the "subjects" table.
my_table = tables['subjects']
my_table.head()
```
See all of the tables in ```tables``` as follows:
```python
# The dictionary also contains a series of table names. See the list.
tables['list_tables']

# Display all of the tables.
from IPython.display import display
for name, tbl in tables.items():
  display(tbl)
```

## Technical notes

The function reads the data and iterates the following process over the names of the tables. It filters the rows of the main dataframe to only include rows that belong to the current table. Then it processes the data for each treatment within the table and creates a dataframe for each treatment. 
If the period is repeated in the treatment, the data for the treatment has a header row with variable names inserted each period. This function assumes that these header rows are the same within the treatment and reads the top header row as the variable names, then removes all header rows afterwards. All data will be converted to numeric, if possible. Finally, the table for the current treatment is added to the dataframe for the current table. 

After all the tables have been processed, the function returns the dictionary of dataframes.

## License

[MIT](https://choosealicense.com/licenses/mit/). ztree2python is "provided "as is", without warranty of any kind."

## Reference
Fischbacher, U. (2007). z-Tree: Zurich toolbox for ready-made economic experiments. *Experimental Economics*, 10(2), 171-178. 
https://doi.org/10.1007/s10683-006-9159-4.

Takeuchi, Kan. (2022). ztree2python.py, http://github.com/takekan/ztree2python.
(https://sites.google.com/view/takekan/research/ztree2python)

Takeuchi, K. (2022). ztree2stata: A data converter for z-Tree and Stata users. (*Journal of the Economic Science Association*, R&R.)

I would appreciate it if you kindly mention to this code in a footnote or somewhere.



## Acknowledgment 
Takeuchi thanks Zhewei Song for the helpful feedback. 

## A sample data
    
```python
from ztree2python import ztree2python as ztree2python
tables = ztree2python('221215_1449.xls')
```


```python
# Extract the data of a table by its name. For example, 
df = tables['globals']
df
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>session</th>
      <th>treatment</th>
      <th>table</th>
      <th>Period</th>
      <th>NumPeriods</th>
      <th>TreatmentNumber</th>
      <th>TreatmentID</th>
      <th>RepeatTreatment</th>
      <th>Repetition</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>221215_1449</td>
      <td>1</td>
      <td>globals</td>
      <td>1</td>
      <td>5</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>221215_1449</td>
      <td>1</td>
      <td>globals</td>
      <td>2</td>
      <td>5</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>221215_1449</td>
      <td>1</td>
      <td>globals</td>
      <td>3</td>
      <td>5</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>3</th>
      <td>221215_1449</td>
      <td>1</td>
      <td>globals</td>
      <td>4</td>
      <td>5</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>4</th>
      <td>221215_1449</td>
      <td>1</td>
      <td>globals</td>
      <td>5</td>
      <td>5</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>




```python
# To display all the tables and the table name list.
from IPython.display import display
for name, tbl in tables.items():
    display(tbl)
```


<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>session</th>
      <th>treatment</th>
      <th>table</th>
      <th>Period</th>
      <th>NumPeriods</th>
      <th>TreatmentNumber</th>
      <th>TreatmentID</th>
      <th>RepeatTreatment</th>
      <th>Repetition</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>221215_1449</td>
      <td>1</td>
      <td>globals</td>
      <td>1</td>
      <td>5</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>221215_1449</td>
      <td>1</td>
      <td>globals</td>
      <td>2</td>
      <td>5</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>221215_1449</td>
      <td>1</td>
      <td>globals</td>
      <td>3</td>
      <td>5</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>3</th>
      <td>221215_1449</td>
      <td>1</td>
      <td>globals</td>
      <td>4</td>
      <td>5</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>4</th>
      <td>221215_1449</td>
      <td>1</td>
      <td>globals</td>
      <td>5</td>
      <td>5</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>



<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>session</th>
      <th>treatment</th>
      <th>table</th>
      <th>Period</th>
      <th>Subject</th>
      <th>ClientNumber</th>
      <th>LastClientNumber</th>
      <th>Group</th>
      <th>Profit</th>
      <th>TotalProfit</th>
      <th>Participate</th>
      <th>EfficiencyFactor</th>
      <th>Endowment</th>
      <th>Contribution</th>
      <th>TimeOKContributionEntryOK</th>
      <th>SumC</th>
      <th>N</th>
      <th>TimeContinueProfitDisplayOK</th>
      <th>LeaveStage</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>221215_1449</td>
      <td>1</td>
      <td>subjects</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>26.6</td>
      <td>26.6</td>
      <td>1</td>
      <td>1.6</td>
      <td>20</td>
      <td>7</td>
      <td>-41</td>
      <td>17</td>
      <td>2</td>
      <td>30</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>221215_1449</td>
      <td>1</td>
      <td>subjects</td>
      <td>1</td>
      <td>2</td>
      <td>2</td>
      <td>2</td>
      <td>1</td>
      <td>23.6</td>
      <td>23.6</td>
      <td>1</td>
      <td>1.6</td>
      <td>20</td>
      <td>10</td>
      <td>-36</td>
      <td>17</td>
      <td>2</td>
      <td>28</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>221215_1449</td>
      <td>1</td>
      <td>subjects</td>
      <td>1</td>
      <td>3</td>
      <td>3</td>
      <td>3</td>
      <td>2</td>
      <td>31.4</td>
      <td>31.4</td>
      <td>1</td>
      <td>1.6</td>
      <td>20</td>
      <td>15</td>
      <td>-30</td>
      <td>33</td>
      <td>2</td>
      <td>27</td>
      <td>0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>221215_1449</td>
      <td>1</td>
      <td>subjects</td>
      <td>1</td>
      <td>4</td>
      <td>4</td>
      <td>4</td>
      <td>2</td>
      <td>28.4</td>
      <td>28.4</td>
      <td>1</td>
      <td>1.6</td>
      <td>20</td>
      <td>18</td>
      <td>11</td>
      <td>33</td>
      <td>2</td>
      <td>25</td>
      <td>0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>221215_1449</td>
      <td>1</td>
      <td>subjects</td>
      <td>2</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>25.0</td>
      <td>51.6</td>
      <td>1</td>
      <td>1.6</td>
      <td>20</td>
      <td>11</td>
      <td>9</td>
      <td>20</td>
      <td>2</td>
      <td>99999</td>
      <td>0</td>
    </tr>
    <tr>
      <th>5</th>
      <td>221215_1449</td>
      <td>1</td>
      <td>subjects</td>
      <td>2</td>
      <td>2</td>
      <td>2</td>
      <td>2</td>
      <td>1</td>
      <td>27.0</td>
      <td>50.6</td>
      <td>1</td>
      <td>1.6</td>
      <td>20</td>
      <td>9</td>
      <td>13</td>
      <td>20</td>
      <td>2</td>
      <td>29</td>
      <td>0</td>
    </tr>
    <tr>
      <th>6</th>
      <td>221215_1449</td>
      <td>1</td>
      <td>subjects</td>
      <td>2</td>
      <td>3</td>
      <td>3</td>
      <td>3</td>
      <td>2</td>
      <td>30.6</td>
      <td>62.0</td>
      <td>1</td>
      <td>1.6</td>
      <td>20</td>
      <td>15</td>
      <td>22</td>
      <td>32</td>
      <td>2</td>
      <td>26</td>
      <td>0</td>
    </tr>
    <tr>
      <th>7</th>
      <td>221215_1449</td>
      <td>1</td>
      <td>subjects</td>
      <td>2</td>
      <td>4</td>
      <td>4</td>
      <td>4</td>
      <td>2</td>
      <td>28.6</td>
      <td>57.0</td>
      <td>1</td>
      <td>1.6</td>
      <td>20</td>
      <td>17</td>
      <td>17</td>
      <td>32</td>
      <td>2</td>
      <td>28</td>
      <td>0</td>
    </tr>
    <tr>
      <th>8</th>
      <td>221215_1449</td>
      <td>1</td>
      <td>subjects</td>
      <td>3</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>20.4</td>
      <td>72.0</td>
      <td>1</td>
      <td>1.6</td>
      <td>20</td>
      <td>18</td>
      <td>9</td>
      <td>23</td>
      <td>2</td>
      <td>30</td>
      <td>0</td>
    </tr>
    <tr>
      <th>9</th>
      <td>221215_1449</td>
      <td>1</td>
      <td>subjects</td>
      <td>3</td>
      <td>2</td>
      <td>2</td>
      <td>2</td>
      <td>1</td>
      <td>33.4</td>
      <td>84.0</td>
      <td>1</td>
      <td>1.6</td>
      <td>20</td>
      <td>5</td>
      <td>13</td>
      <td>23</td>
      <td>2</td>
      <td>28</td>
      <td>0</td>
    </tr>
    <tr>
      <th>10</th>
      <td>221215_1449</td>
      <td>1</td>
      <td>subjects</td>
      <td>3</td>
      <td>3</td>
      <td>3</td>
      <td>3</td>
      <td>2</td>
      <td>31.4</td>
      <td>93.4</td>
      <td>1</td>
      <td>1.6</td>
      <td>20</td>
      <td>11</td>
      <td>16</td>
      <td>28</td>
      <td>2</td>
      <td>27</td>
      <td>0</td>
    </tr>
    <tr>
      <th>11</th>
      <td>221215_1449</td>
      <td>1</td>
      <td>subjects</td>
      <td>3</td>
      <td>4</td>
      <td>4</td>
      <td>4</td>
      <td>2</td>
      <td>25.4</td>
      <td>82.4</td>
      <td>1</td>
      <td>1.6</td>
      <td>20</td>
      <td>17</td>
      <td>21</td>
      <td>28</td>
      <td>2</td>
      <td>25</td>
      <td>0</td>
    </tr>
    <tr>
      <th>12</th>
      <td>221215_1449</td>
      <td>1</td>
      <td>subjects</td>
      <td>4</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>27.4</td>
      <td>99.4</td>
      <td>1</td>
      <td>1.6</td>
      <td>20</td>
      <td>3</td>
      <td>7</td>
      <td>13</td>
      <td>2</td>
      <td>99999</td>
      <td>0</td>
    </tr>
    <tr>
      <th>13</th>
      <td>221215_1449</td>
      <td>1</td>
      <td>subjects</td>
      <td>4</td>
      <td>2</td>
      <td>2</td>
      <td>2</td>
      <td>1</td>
      <td>20.4</td>
      <td>104.4</td>
      <td>1</td>
      <td>1.6</td>
      <td>20</td>
      <td>10</td>
      <td>13</td>
      <td>13</td>
      <td>2</td>
      <td>25</td>
      <td>0</td>
    </tr>
    <tr>
      <th>14</th>
      <td>221215_1449</td>
      <td>1</td>
      <td>subjects</td>
      <td>4</td>
      <td>3</td>
      <td>3</td>
      <td>3</td>
      <td>2</td>
      <td>21.2</td>
      <td>114.6</td>
      <td>1</td>
      <td>1.6</td>
      <td>20</td>
      <td>10</td>
      <td>19</td>
      <td>14</td>
      <td>2</td>
      <td>27</td>
      <td>0</td>
    </tr>
    <tr>
      <th>15</th>
      <td>221215_1449</td>
      <td>1</td>
      <td>subjects</td>
      <td>4</td>
      <td>4</td>
      <td>4</td>
      <td>4</td>
      <td>2</td>
      <td>27.2</td>
      <td>109.6</td>
      <td>1</td>
      <td>1.6</td>
      <td>20</td>
      <td>4</td>
      <td>10</td>
      <td>14</td>
      <td>2</td>
      <td>29</td>
      <td>0</td>
    </tr>
    <tr>
      <th>16</th>
      <td>221215_1449</td>
      <td>1</td>
      <td>subjects</td>
      <td>5</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>22.0</td>
      <td>121.4</td>
      <td>1</td>
      <td>1.6</td>
      <td>20</td>
      <td>10</td>
      <td>0</td>
      <td>15</td>
      <td>2</td>
      <td>28</td>
      <td>0</td>
    </tr>
    <tr>
      <th>17</th>
      <td>221215_1449</td>
      <td>1</td>
      <td>subjects</td>
      <td>5</td>
      <td>2</td>
      <td>2</td>
      <td>2</td>
      <td>1</td>
      <td>27.0</td>
      <td>131.4</td>
      <td>1</td>
      <td>1.6</td>
      <td>20</td>
      <td>5</td>
      <td>-3</td>
      <td>15</td>
      <td>2</td>
      <td>30</td>
      <td>0</td>
    </tr>
    <tr>
      <th>18</th>
      <td>221215_1449</td>
      <td>1</td>
      <td>subjects</td>
      <td>5</td>
      <td>3</td>
      <td>3</td>
      <td>3</td>
      <td>2</td>
      <td>19.4</td>
      <td>134.0</td>
      <td>1</td>
      <td>1.6</td>
      <td>20</td>
      <td>3</td>
      <td>9</td>
      <td>3</td>
      <td>2</td>
      <td>25</td>
      <td>0</td>
    </tr>
    <tr>
      <th>19</th>
      <td>221215_1449</td>
      <td>1</td>
      <td>subjects</td>
      <td>5</td>
      <td>4</td>
      <td>4</td>
      <td>4</td>
      <td>2</td>
      <td>22.4</td>
      <td>132.0</td>
      <td>1</td>
      <td>1.6</td>
      <td>20</td>
      <td>0</td>
      <td>15</td>
      <td>3</td>
      <td>2</td>
      <td>26</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>



<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>session</th>
      <th>treatment</th>
      <th>table</th>
      <th>Period</th>
    </tr>
  </thead>
  <tbody>
  </tbody>
</table>
</div>



<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>session</th>
      <th>treatment</th>
      <th>table</th>
      <th>Period</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>221215_1449</td>
      <td>1</td>
      <td>summary</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>221215_1449</td>
      <td>1</td>
      <td>summary</td>
      <td>2</td>
    </tr>
    <tr>
      <th>2</th>
      <td>221215_1449</td>
      <td>1</td>
      <td>summary</td>
      <td>3</td>
    </tr>
    <tr>
      <th>3</th>
      <td>221215_1449</td>
      <td>1</td>
      <td>summary</td>
      <td>4</td>
    </tr>
    <tr>
      <th>4</th>
      <td>221215_1449</td>
      <td>1</td>
      <td>summary</td>
      <td>5</td>
    </tr>
  </tbody>
</table>
</div>



<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>session</th>
      <th>treatment</th>
      <th>table</th>
      <th>ClientNumber</th>
      <th>ClientName</th>
      <th>TreatmentNumber</th>
      <th>Subject</th>
      <th>StateString</th>
      <th>RemainingSeconds</th>
      <th>FinalProfit</th>
      <th>MoneyAdded</th>
      <th>ShowUpFee</th>
      <th>ShowUpFeeInvested</th>
      <th>MoneyToPay</th>
      <th>MoneyEarned</th>
      <th>LastClientNumber</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>221215_1449</td>
      <td>1</td>
      <td>clients</td>
      <td>1</td>
      <td>4</td>
      <td>1</td>
      <td>1</td>
      <td>- Profit Display -</td>
      <td>25</td>
      <td>121.4</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>121.4</td>
      <td>121.4</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>221215_1449</td>
      <td>1</td>
      <td>clients</td>
      <td>2</td>
      <td>1</td>
      <td>1</td>
      <td>2</td>
      <td>- Profit Display -</td>
      <td>25</td>
      <td>131.4</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>131.4</td>
      <td>131.4</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>221215_1449</td>
      <td>1</td>
      <td>clients</td>
      <td>3</td>
      <td>2</td>
      <td>1</td>
      <td>3</td>
      <td>- Profit Display -</td>
      <td>25</td>
      <td>134.0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>134.0</td>
      <td>134.0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>221215_1449</td>
      <td>1</td>
      <td>clients</td>
      <td>4</td>
      <td>3</td>
      <td>1</td>
      <td>4</td>
      <td>- Profit Display -</td>
      <td>25</td>
      <td>132.0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>132.0</td>
      <td>132.0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>221215_1449</td>
      <td>-1</td>
      <td>clients</td>
      <td>1</td>
      <td>4</td>
      <td>-1</td>
      <td>-1</td>
      <td>Ready</td>
      <td>25</td>
      <td>121.4</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>121.4</td>
      <td>121.4</td>
      <td>0</td>
    </tr>
    <tr>
      <th>5</th>
      <td>221215_1449</td>
      <td>-1</td>
      <td>clients</td>
      <td>2</td>
      <td>1</td>
      <td>-1</td>
      <td>-1</td>
      <td>Ready</td>
      <td>25</td>
      <td>131.4</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>131.4</td>
      <td>131.4</td>
      <td>0</td>
    </tr>
    <tr>
      <th>6</th>
      <td>221215_1449</td>
      <td>-1</td>
      <td>clients</td>
      <td>3</td>
      <td>2</td>
      <td>-1</td>
      <td>-1</td>
      <td>Ready</td>
      <td>25</td>
      <td>134.0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>134.0</td>
      <td>134.0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>7</th>
      <td>221215_1449</td>
      <td>-1</td>
      <td>clients</td>
      <td>4</td>
      <td>3</td>
      <td>-1</td>
      <td>-1</td>
      <td>Ready</td>
      <td>25</td>
      <td>132.0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>132.0</td>
      <td>132.0</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>



<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>session</th>
      <th>treatment</th>
      <th>table</th>
      <th>TreatmentID</th>
      <th>BaseTreatment</th>
      <th>StartMethod</th>
      <th>FileName</th>
      <th>BackupFileName</th>
      <th>NumberOfSubjects</th>
      <th>TreatmentNumber</th>
      <th>StartTimeString</th>
      <th>EndTimeString</th>
      <th>ErrorString</th>
      <th>MessageString</th>
      <th>EmptyString</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>221215_1449</td>
      <td>1</td>
      <td>treatments</td>
      <td>1</td>
      <td>1</td>
      <td>menu</td>
      <td>pg.ztt</td>
      <td>C:\\ztree-5_1_8\\@221215_1449_pg.ztt</td>
      <td>4</td>
      <td>1</td>
      <td>2022-12-15T14:52:17.368-05:00</td>
      <td>2022-12-15T14:55:46.382-05:00</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>1</th>
      <td>221215_1449</td>
      <td>-1</td>
      <td>treatments</td>
      <td>1</td>
      <td>1</td>
      <td>menu</td>
      <td>pg.ztt</td>
      <td>C:\\ztree-5_1_8\\@221215_1449_pg.ztt</td>
      <td>4</td>
      <td>1</td>
      <td>2022-12-15T14:52:17.368-05:00</td>
      <td>2022-12-15T14:55:46.382-05:00</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>
</div>



<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>session</th>
      <th>treatment</th>
      <th>table</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>221215_1449</td>
      <td>1</td>
      <td>sessionglobals</td>
    </tr>
    <tr>
      <th>1</th>
      <td>221215_1449</td>
      <td>1</td>
      <td>sessionglobals</td>
    </tr>
    <tr>
      <th>2</th>
      <td>221215_1449</td>
      <td>-1</td>
      <td>sessionglobals</td>
    </tr>
    <tr>
      <th>3</th>
      <td>221215_1449</td>
      <td>-1</td>
      <td>sessionglobals</td>
    </tr>
  </tbody>
</table>
</div>



<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>session</th>
      <th>treatment</th>
      <th>table</th>
      <th>ParticipationID</th>
      <th>ClientNumber</th>
      <th>Subject</th>
      <th>TreatmentNumber</th>
      <th>StartInPeriod</th>
      <th>FinishedPeriod</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>221215_1449</td>
      <td>1</td>
      <td>participations</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>5</td>
    </tr>
    <tr>
      <th>1</th>
      <td>221215_1449</td>
      <td>1</td>
      <td>participations</td>
      <td>2</td>
      <td>2</td>
      <td>2</td>
      <td>1</td>
      <td>1</td>
      <td>5</td>
    </tr>
    <tr>
      <th>2</th>
      <td>221215_1449</td>
      <td>1</td>
      <td>participations</td>
      <td>3</td>
      <td>3</td>
      <td>3</td>
      <td>1</td>
      <td>1</td>
      <td>5</td>
    </tr>
    <tr>
      <th>3</th>
      <td>221215_1449</td>
      <td>1</td>
      <td>participations</td>
      <td>4</td>
      <td>4</td>
      <td>4</td>
      <td>1</td>
      <td>1</td>
      <td>5</td>
    </tr>
    <tr>
      <th>4</th>
      <td>221215_1449</td>
      <td>-1</td>
      <td>participations</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>5</td>
    </tr>
    <tr>
      <th>5</th>
      <td>221215_1449</td>
      <td>-1</td>
      <td>participations</td>
      <td>2</td>
      <td>2</td>
      <td>2</td>
      <td>1</td>
      <td>1</td>
      <td>5</td>
    </tr>
    <tr>
      <th>6</th>
      <td>221215_1449</td>
      <td>-1</td>
      <td>participations</td>
      <td>3</td>
      <td>3</td>
      <td>3</td>
      <td>1</td>
      <td>1</td>
      <td>5</td>
    </tr>
    <tr>
      <th>7</th>
      <td>221215_1449</td>
      <td>-1</td>
      <td>participations</td>
      <td>4</td>
      <td>4</td>
      <td>4</td>
      <td>1</td>
      <td>1</td>
      <td>5</td>
    </tr>
  </tbody>
</table>
</div>



<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>session</th>
      <th>treatment</th>
      <th>table</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>221215_1449</td>
      <td>1</td>
      <td>&lt;&lt;  end</td>
    </tr>
  </tbody>
</table>
</div>



    0           globals
    1          subjects
    2         contracts
    3           summary
    4           clients
    5        treatments
    6    sessionglobals
    7    participations
    8           <<  end
    Name: 2, dtype: object



```python
#### 1. Compute the mean contribution to draw a simple graph

# read the data of the subjects table
from ztree2python import ztree2python as ztree2python
tables = ztree2python('221215_1449.xls')
df = tables['subjects']

# extract the unique values from the period column. This is going to be the x.
period_values = df['Period'].unique()
print(period_values)

# get the mean of 'Contribution' by 'Period'. This is going to be the y.
mean_contribution_by_period = df.groupby('Period')['Contribution'].mean()
print(mean_contribution_by_period)

```

    [1 2 3 4 5]
    Period
    1    12.50
    2    13.00
    3    12.75
    4     6.75
    5     4.50
    Name: Contribution, dtype: float64
    


```python
#### 1. Draw a simple graph (continuted from the above)

# set the values.
x = period_values
y = mean_contribution_by_period

# draw a simple graph.
# You need matplotlib
import matplotlib.pyplot as plt
plt.plot(x, y)

# Add labels to the axes
plt.title("Mean contribution")
plt.xlabel("Period")
plt.ylabel("Mean contribution")

# Show the plot
plt.show()
```


    
![png](https://github.com/takekan/ztree2python/blob/main/fig1.png)
    



```python
#### 2. Draw a graph for each Group and add error bar.

# read the data of the subjects table
from ztree2python import ztree2python as ztree2python
tables = ztree2python('221215_1449.xls')
df = tables['subjects']

# extract the unique values from the period column 
period_values = df['Period'].unique()
x = period_values

# Group the data by period and compute the mean and standard error of y for each group
mean_by_period_1 = df[df['Group'] == 1].groupby('Period')['Contribution'].mean()
se_by_period_1   = df[df['Group'] == 1].groupby('Period')['Contribution'].sem()
mean_by_period_2 = df[df['Group'] == 2].groupby('Period')['Contribution'].mean()
se_by_period_2   = df[df['Group'] == 2].groupby('Period')['Contribution'].sem()


# Use the plot function to create a line chart of the mean values
import matplotlib.pyplot as plt
plt.plot(x, mean_by_period_1, linestyle='solid' , marker='o', color='b', label='Group 1')
plt.plot(x, mean_by_period_2, linestyle='dashed', marker='o', color='r', label='Group 2')

# Use the errorbar function to add error bars to the line chart
plt.errorbar(x, mean_by_period_1, yerr=se_by_period_1, fmt='none', ecolor='b')
plt.errorbar(x, mean_by_period_2, yerr=se_by_period_2, fmt='none', ecolor='r')

# Add labels to the axes
plt.title("Mean contribution by Group")
plt.xlabel("Period")
plt.ylabel("Mean contribution")

# Add a legend and title to the plot
plt.legend(loc='upper right')

# Ticks at the data points
plt.xticks(period_values)

# Show the plot
plt.show()
```


    
![png](https://github.com/takekan/ztree2python/blob/main/fig2.png)

Enjoy!
