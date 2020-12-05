# in shell linux: time python make_profile.py
# in cmd windows: python make_profile.py

import pandas as pd
import pandas_profiling

df = pd.read_csv('../data/train_data/df_train.csv', index_col=0)
print(df.shape)

# df2 = df.iloc[:10, :10]

profile = df.profile_report(html={'style':{'full_width':True}})
profile.to_file("../data/profiles/df_train_profile.html")

