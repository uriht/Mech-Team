import pandas as pd
read=pd.read_csv("sample.csv")
remove_dup=read.drop_duplicates(subset="Name")
sort=remove_dup.sort_values(by='CGPA',ascending=False)
top_rankers=sort.head(3)
print(top_rankers)