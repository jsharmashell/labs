# creating single instance  and maintaining releasing of resources
class Test:
    def __enter__(self):
        print("starting")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("closing")
    
    def print(self):
        print("HELLO")

def create():
    with Test() as t:
        yield t

def function(instance):
    instance.print()

class C1:
    def __init__(self, instance):
        self.instance = instance

a = create()
instance = next(a)

function(instance)
C1(a)

print("finish")




import pandas as pd

# Sample DataFrame with start date and end date columns
data = {
    'start_date': ['2023-01-01', '2023-02-15', '2023-03-10'],
    'end_date': ['2022-01-10', '2023-02-20', '2023-03-15']
}

df = pd.DataFrame(data)

# Convert the columns to datetime
df['start_date'] = pd.to_datetime(df['start_date'])
df['end_date'] = pd.to_datetime(df['end_date'])

# Find the minimum and maximum dates
min_date = df['start_date'].min()
max_date = df['end_date'].max()

print(f"The minimum date in the DataFrame is: {min_date}")
print(f"The maximum date in the DataFrame is: {max_date}")
