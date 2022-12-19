#########################################################################################
### ztree2python imports a data file created by z-Tree into python as pandas dataframes.
### Kan Takeuchi, the University of Michigan and Hitotsubashi University.
### E-mail: <ktakeuch@umich.edu> and <kan@econ.hit-u.ac.jp>
### Ver: Dec 17, 2022. (first release)
###
### This function inputs the "filename" of a z-Tree data file, and
### it returns a dictionary, which contains the dataframes of the tables.
### The keys are the names of all tables, "globals", "subjects", and so on.
### The value associated with each key is a pandas dataframe for the table.
###
### NOTE: This code is provided as it is, without any kind of warranty.
###
### How to use (sample codes):
###   # Put a z-Tree data file (e.g., 221215_1236.xls) and this ztree2python.py
###   # in the current directory or the working directory. Then run;
### 
###   from ztree2python import ztree2python as ztree2python
###   df = ztree2python('221215_1236.xls')
###
###   # If you want to extract the "subjects" table for example, then...
###   my_table = df['subjects']
###   my_table.head()
###
###   # The output dataframe also contains a series of table names. To see it, type;
###   tables['list_tables']
###   
###   # If you want to display all tables, then type:  
###   from IPython.display import display
###   for name, tbl in tables.items():
###       display(tbl)
###   
### Good luck with your research. Enjoy!
###
### Reference:
###  Fischbacher, U. (2007). z-Tree: Zurich toolbox for ready-made economic experiments.
###      Experimental Economics, 10(2), 171-178. https://doi.org/10.1007/s10683-006-9159-4.
###  Takeuchi, K. (2022). ztree2stata: A data converter for z-Tree and Stata users.
###      Journal of the Economic Science Association, R&R.
###
### I would appreciate it if you cite this code in a footnote or acknowledgement
### (or you can even add this to the list of references!
###  Takeuchi, Kan. (2022). ztree2python.py, http://github.com/takekan/ztree2python.)

import pandas as pd
import csv

def ztree2python(filename):

    #### 1. READ THE FILE
 
    # Create an empty list to store the rows
    rows = pd.DataFrame()
    
    # Open the z-Tree data file
    with open(filename, 'r') as f:
        # Create a reader object
        reader = csv.reader(f, delimiter='\t')

        # Iterate through the rows of the CSV file
        for row in reader:
            # Append the row to the list
                row  = pd.DataFrame(row).T
                rows = pd.concat((rows, row), axis = 0)
    # Create a Pandas DataFrame from the rows
    df0 = pd.DataFrame(rows)

    # destring
    df = df0.copy()
    df = df.apply(pd.to_numeric, errors="coerce")
    df.fillna(df0, inplace=True)
    
    #### 2. GET THE LIST OF TABLES

    # get the 3rd column that contains the names of the tables
    list_tables = df.iloc[:,2]
    # drop duplicates and reset the index.
    list_tables = list_tables.drop_duplicates()
    list_tables = list_tables.reset_index(drop=True)

    # create a dictionary to hold the individual dataframes for each table
    tables = {}
    # optional: all_tables = pd.DataFrame()

    
    #### 3.0 CLEAN THE DATA FOR EACH TABLE
    
    # iterate over the names of the tables
    for table_name in list_tables:

        # filter the rows of the main dataframe to only include rows that belong to the current table
        table_df = df.loc[df.iloc[:,2] == table_name]

        # get the 2nd column that contains the treatment (numbers)
        treatments = table_df.iloc[:,1]
    
        # drop duplicates and reset the index.
        treatments = treatments.drop_duplicates()

        
    #### 3.1 CLEAN THE DATA FOR EACH TREATMENT WITHIN THE TABLE
        
    # iterate over the treatments of the selected table
        subtable = pd.DataFrame()
        
        for tr in treatments:

            # slice the table by treatment
            subtable_by_tr = table_df.loc[table_df.iloc[:,1] == tr]
            # reset the index
            subtable_by_tr = subtable_by_tr.reset_index(drop=True)

            
            # Drop all columns that contain only NaN values
            subtable_by_tr = subtable_by_tr.dropna(axis=1, how='all', inplace=False)

            # read the first row of the subtable dataframe and use it for the column names
            subtable_by_tr.columns = subtable_by_tr.iloc[0]

            # drop the (repeated) header row(s), which repeats the same variable names (header row for repeated Period)
            # Here, assume that all the repeated header within this treatment=tr are duplicates. 
            # check first if the subtable_by_tr is large enough to apply this drop.
            num_rows = subtable_by_tr.shape[0]
            num_cols = subtable_by_tr.shape[1]
            if num_rows > 0 and num_cols > 3: # Yes, it is large enough. 
                _header = subtable_by_tr.iloc[0]
                _drop = []
                for i in range(num_rows):
                    # Compare the row data to B
                    if subtable_by_tr.iloc[i].equals(_header):
                        _drop = _drop + [i]

                # Then, drop the rows that duplicates the first row 
                subtable_by_tr.drop(_drop, axis=0, inplace=True)
                # So, all rows duplicating the header will be gone, including the header itself.

                        
            # rename the 1st-3rd columns, they are session, treatment, and table.
            subtable_by_tr.rename(columns={ subtable_by_tr.columns[0]: "session" }, inplace = True)
            subtable_by_tr.rename(columns={ subtable_by_tr.columns[1]: "treatment" }, inplace = True)
            subtable_by_tr.rename(columns={ subtable_by_tr.columns[2]: "table" }, inplace = True)
            
            # Add this sliced small table for this treatment into the current table. 
            subtable = pd.concat((subtable, subtable_by_tr), axis = 0)

            
    #### 3.2 COMBINE ALL TREATMENTS FOR THE TABLE
        
        # reset the index
        subtable = subtable.reset_index(drop=True)

        
    #### 3.3 CONVERT INTO NUMERICS and RECORD

        # Create a copy of the dataframe to store the converted values
        subtable_num = subtable.copy()

        # Use the apply method to apply the pd.to_numeric function to all columns
        subtable_num = subtable_num.apply(pd.to_numeric, errors="coerce")

        # Use the fillna method to fill the missing values with the corresponding values from the original dataframe
        subtable_num.fillna(subtable, inplace=True)

        # Then, store it.
        tables[table_name] = subtable_num

        # optional: all_tables = pd.concat((all_tables, subtables), axis = 0)

        
    #### 4. RETURN THE RESULTS
    # optional: all_tables = all_tables.reset_index(drop=True)
    tables['list_tables'] = list_tables

    return tables