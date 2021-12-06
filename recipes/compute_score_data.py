# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
import dataiku
from dataiku import pandasutils as pdu
import pandas as pd
import saspy

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# Creates a connection to remote SAS Server. Uses authinfo file to authenticate.
# Modifications are made in /home/dataiku/dss/code-envs/python/sas/lib/python3.6/site-packages/saspy/sascfg_personal.py
sas = saspy.SASsession()

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
sas.assigned_librefs()

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
sas.datasets('CHURN')

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
outdf = sas.sd2df('SCORE_DATA', 'CHURN')
outdf.head(5)

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# Write recipe outputs
modeling_table = dataiku.Dataset("score_data")
modeling_table.write_with_schema(outdf)