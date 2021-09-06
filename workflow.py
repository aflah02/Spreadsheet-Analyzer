import pandas as pd
import io
path = 'test.csv'
df = pd.read_csv(path)
buffer = io.StringIO()
df.info(buf=buffer)
s = buffer.getvalue()
with open("df_info.txt", "w", encoding="utf-8") as f:
    f.write(s)