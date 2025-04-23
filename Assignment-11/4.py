import pandas as pd

data = {
    'day': range(1, 11),
    'John': [True, False, True, False, False, True, False, True, False, False],
    'Judy': [False, True, True, False, True, False, True, False, True, False]
}
df = pd.DataFrame(data)

df['party'] = df['John'] & df['Judy']

days_til_party = [0] * len(df)

next_party = None
for i in range(len(df) - 1, -1, -1):
    if df.loc[i, 'party']:
        next_party = i
        days_til_party[i] = 0
    else:
        days_til_party[i] = (next_party - i) if next_party is not None else (len(df) - i)

df['days_til_party'] = days_til_party

print(df)
