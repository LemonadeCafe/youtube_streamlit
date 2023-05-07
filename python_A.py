
import streamlit as st
from PIL import Image
import time

st.title("Lemonade Cafe's room")

#----- 写真を読み込み、表示する -----
#----- インタラクティブなウィジェット -----

latest_iteration=st.empty()
bar=st.progress(0)
for i in range(100):
    latest_iteration.text(f'読み込み中 {i+1}')
    bar.progress(i+1)
    time.sleep(0.1)



left_column,right_column =st.columns(2)
button=left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラム')

expander=st.expander('問い合わせ')
expander.write('回答1')
expander.write('回答2')
expander.write('回答3')


# option=st.text_input('あなたの趣味を教えてください。')
# condition= st.slider('あなたの今の調子は？',0,10,5)

# 'あなたの趣味：',option
# 'コンディション：', condition

# option=st.selectbox(
#     'あなたが好きな数字を教えてください。',
#     list(range(1,11))
# )
# 'あなたの好きな数字は、',option,'です。'

# if st.checkbox('Show Image'):
#     img=Image.open('IMG_2502.jpeg')
#     st.image(img,caption='keibazyou',use_column_width=True)








