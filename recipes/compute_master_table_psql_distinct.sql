SELECT 
    "Account_ID" AS "Account_ID",
    "Acct_Plan_Type" AS "Acct_Plan_Type",
    "Avg_Talk_Hrs" AS "Avg_Talk_Hrs",
    "Acct_Age_Months" AS "Acct_Age_Months",
    "Recent_Complaint" AS "Recent_Complaint",
    "Recent_Complaint_flag" AS "Recent_Complaint_flag",
    "Target_Churn" AS "Target_Churn",
    "Current_Bill_Range" AS "Current_Bill_Range",
    "Percent_Incr_MOM" AS "Percent_Incr_MOM",
    "Avg_Days_Delinquent" AS "Avg_Days_Delinquent",
    "State" AS "State",
    "Headset_Age" AS "Headset_Age",
    "Equipment_Age" AS "Equipment_Age"
  FROM (
    SELECT 
        "Account_ID" AS "Account_ID",
        "Acct_Plan_Type" AS "Acct_Plan_Type",
        "Avg_Talk_Hrs" AS "Avg_Talk_Hrs",
        "Acct_Age_Months" AS "Acct_Age_Months",
        "Recent_Complaint" AS "Recent_Complaint",
        "Recent_Complaint_flag" AS "Recent_Complaint_flag",
        "Target_Churn" AS "Target_Churn",
        "Current_Bill_Range" AS "Current_Bill_Range",
        "Percent_Incr_MOM" AS "Percent_Incr_MOM",
        "Avg_Days_Delinquent" AS "Avg_Days_Delinquent",
        "State" AS "State",
        "Headset_Age" AS "Headset_Age",
        "Equipment_Age" AS "Equipment_Age"
      FROM "dku_demo"."CUSTOMERCHURN_master_table_psql"
    ) "dku__beforegrouping"
  GROUP BY "Account_ID", "Acct_Plan_Type", "Avg_Talk_Hrs", "Acct_Age_Months", "Recent_Complaint", "Recent_Complaint_flag", "Target_Churn", "Current_Bill_Range", "Percent_Incr_MOM", "Avg_Days_Delinquent", "State", "Headset_Age", "Equipment_Age"