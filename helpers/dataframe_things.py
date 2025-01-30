import pandas as pd
from pandas.testing import assert_frame_equal

# Create two DataFrames with the same data but in different orders for TSO
df1 = pd.DataFrame({
    'TSO': ['Amprion', 'Hertz', 'TransnetBW'],
    'Price': [1.1, 1.9, 1.5],
    'Quantity': [3, 1, 2]
})

df2 = pd.DataFrame({
    'TSO': ['TransnetBW', 'Amprion', 'Hertz'],
    'Price': [1.5, 1.1, 1.9],
    'Quantity': [2, 3, 1]
})
print("Record set 1 \n###############################")
print(df1)
print("\n\n")
print("Record set 2 \n###############################")
print(df2)
print(".............................................................................................................................................")

# Sort both DataFrames by column 'TSO'
sorted_df1 = df1.sort_values(by='TSO')
sorted_df2 = df2.sort_values(by='TSO')

# Apply assert_frame_equal to check if the sorted DataFrames are equal
try:
    print("\n\n\n\n Record set 1 after sorting by TSO \n###############################")
    print(sorted_df1)
    print("\n\n")
    print("Record set 2 after sorting by TSO\n###############################")
    print(sorted_df2)
    assert_frame_equal(sorted_df1.reset_index(drop=True), sorted_df2.reset_index(drop=True))

    # assert_frame_equal(df1,df2)
    print("The DataFrames are equal.")
except AssertionError as e:
    print("AssertionError:", e)






