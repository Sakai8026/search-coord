import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('vr_coords.csv')
x_ax = df['coord_x'].mean()
y_ax = df['coord_y'].mean()
plt.xlim(-0.145+x_ax,0.145+x_ax)
plt.ylim(-0.145+y_ax,0.145+y_ax)
plt.axvline(x=x_ax, color='k', linewidth=1)
plt.axhline(y=y_ax, color='k', linewidth=1)
# plt.title("分散",fontsize=15)
plt.xlabel('X',fontsize=10)
plt.ylabel('Y',fontsize=10)

def read_json_value(i):
  if i < len(df):
    return df.loc[i]
  else:
    return None

st.title('座標一覧・検索')

# ユーザーから数値を受け取る
i = st.number_input('座標番号を入力:', min_value=0, step=1)

# JSONファイルから値を読み取る
result = read_json_value(int(i))

# 結果を表示する
if result is not None:
  # st.success(result)
  st.write(result['title'])
  st.write(result['url'])
  plt.plot(result["coord_x"], result["coord_y"], marker='.')
  st.pyplot()
else:
  st.error('指定された行は存在しません')
