---
title: "shaneMLproject"
author: "Shane Bateman"
format:
  html:
    toc: true
    toc-location: left
    self-contained: true
engine: python3
---




```{python}
df = pd.read_csv('C:/Users/shane/Downloads/archive (7)/merged.csv')

# df

# df.shape

# df.value_counts()

# df.columns

df = data.rename(columns = { ' Timestamp' : 'Timestamp' })

df['Timestamp'] = pd.to_datetime(df['Timestamp'], dayfirst = True)

```

