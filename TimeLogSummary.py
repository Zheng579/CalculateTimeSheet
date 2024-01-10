import pandas as pd
import os

df = pd.read_excel('TimeLogSummary.xlsx', sheet_name='Sheet1')

df['Date'] = pd.to_datetime(df['Date'])

# Convert the 'Time' column to timedelta
df['Time'] = pd.to_timedelta(df['Time'].astype(str))

result_dfs = []
# Group the DataFrame by the 'Date' column
grouped_by_date = df.groupby('Date')

#Iterate over the groups
for date, group in grouped_by_date:
    total_time = str(group['Time'].sum()).split()[2]
    
    # Create a new DataFrame with the sum
    sum_df = pd.DataFrame({'Date': [date], 'Time': [total_time]})
    print(f"\nDate: {date} \nTotal Time: {total_time}")
    
    group['Time'] = [ str(deltime).split()[2] for deltime in group['Time']]
    print(group)
    # Append the new DataFrame to the list
    result_dfs.append(sum_df)

# Concatenate the list of DataFrames into the final result
result_df = pd.concat(result_dfs, ignore_index=True)

#region EXIT PROGRAM
#IF USER NOT PRESS THE ENTER TO EXIT, THEN EXIT AUTOMATICALLY
os.system('pause')
#endregion
    

###################################################################################################################
# Write Data Back into the excel
# seattle_restaurants_df = pd.DataFrame(
#     data=seattle_restaurants,
#     columns=['Restaurant', 'Cuisine', 'Rating']
# )

# seattle_restaurants_df.to_excel(
#     'seattle_restaurants.xlsx',
#     # Don't save the auto-generated numeric index
#     index=False
# )

# seattle_restaurants_df

# Add a new sheet to the existing file
# Create an instance of ExcelWriter in append mode
# with pd.ExcelWriter('cities_restaurants.xlsx', mode='a') as writer:
#     # Append new sheet
#     nola_restaurants_df.to_excel(
#         writer,
#         sheet_name='New Orleans',
#         index=False
#     )
###################################################################################################################