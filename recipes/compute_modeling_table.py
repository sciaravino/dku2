# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# -*- coding: utf-8 -*-
import dataiku
import pulp
import pandas as pd
from dataiku import pandasutils as pdu

# Read recipe inputs
master_Table = dataiku.Dataset("master_table_psql")
master_Table_df = master_Table.get_dataframe()

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# Prep Steps
master_Table_df.info()

sample_df = master_Table_df.sample(frac=.1)
sample_df.info()

# Complaints
sample_df.loc[sample_df['Recent_Complaint_flag'].isnull(), 'Recent_Complaint_flag'] = 0
print("Count total missing values for each column:\n", sample_df.isnull().sum().sum())

# State
sample_df["State"] = sample_df["State"].str.title()

# Account Plan
sample_df["Plan_Full"] = sample_df["Acct_Plan_Type"] + "_" + sample_df["Recent_Complaint"]
sample_df.info()

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE

# Pulp Test
pulp.pulpTestAll()

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# Write recipe outputs
modeling_table_df=master_Table_df.dropna()
modeling_table = dataiku.Dataset("modeling_table")
modeling_table.write_with_schema(modeling_table_df)