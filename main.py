import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('Streamlit超入門')

st.write('プログレスバーの表示')
'Start!!'

latest_iteration = st.empty()
bar= st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration{i+1}')
    bar.progress(i+1)
    time.sleep(0.1)

'Done!!!!'

st.write('Dataaframe')

df=pd.DataFrame({
    '1列目':[1, 2, 3, 4],
    '2列目':[10, 20, 30, 40]
})

st.dataframe(df.style.highlight_max(axis=0), width=100, height=100)
st.table(df.style.highlight_max(axis=0))


"""
# 章
## 節
### 項

```python
import streamlit as st
import numpy as np
import pandas as pd
```

"""

df=pd.DataFrame(
    np.random.rand(20,3),
    columns=['a','b','c']
)

st.area_chart(df)

df=pd.DataFrame(
    np.random.rand(100,2)/[50,50]+[35.69, 139.70],
    columns=['lat','lon']
)

st.map(df)

st.write('Disply Image')

if st.checkbox('Show Image'):
    img=Image.open('large.png')
    st.image(img, caption='夏至', use_column_width=True)

option=st.selectbox(
    'あなたが好きな数字を入れてください、',
    list(range(1, 11))
)

'あなたの好きな数字は、',option,'です。'

left_column, right_column = st.beta_columns(2)
button=left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラム')

expander1= st.beta_expander('問い合わせ1')
expander1.write('問い合わせを書く1')
expander2= st.beta_expander('問い合わせ2')
expander2.write('問い合わせを書く2')
expander3= st.beta_expander('問い合わせ3')
expander3.write('問い合わせを書く3')



st.write('Interactive Widgets')
text=st.text_input('あなたの趣味を教えてください。')
'あなたの趣味：', text

condision=st.slider('あなたの今の調子は？', 0, 100, 50)
'コンディション：', condision
