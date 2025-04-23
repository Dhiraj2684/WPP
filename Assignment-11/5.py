import pandas as pd

data = {
    'artist': ['Artist A', 'Artist B', 'Artist A', 'Artist C', 'Artist B'],
    'venue': ['Venue 1', 'Venue 2', 'Venue 1', 'Venue 3', 'Venue 2'],
    'concert_date': ['2025-01-15', '2025-01-20', '2025-02-15', '2025-02-20', '2025-03-15']
}
df = pd.DataFrame(data)
df['concert_date'] = pd.to_datetime(df['concert_date'])

df['year_month'] = df['concert_date'].dt.to_period('M')

pivot_table = df.groupby(['year_month', 'artist', 'venue']).size().unstack(['artist', 'venue'], fill_value=0)

print(pivot_table)
