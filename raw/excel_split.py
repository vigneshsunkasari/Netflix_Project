import pandas as pd
excel_sheets=pd.ExcelFile('netflix_titles.xlsx')
for sheet_name in excel_sheets.sheet_names:
     df=pd.read_excel('/workspaces/Netflix_Project/raw/netflix_titles.xlsx',sheet_name=f'{sheet_name}')
     df.to_csv(f'/workspaces/Netflix_Project/splitted_files/{sheet_name}.csv',index=False)