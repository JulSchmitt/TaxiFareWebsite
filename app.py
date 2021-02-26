import streamlit as st

import numpy as np
import pandas as pd

import datetime

'''
# Taxifare Calculator
'''

st.markdown('''
Let's Move it!
''')



st.sidebar.markdown(f"""
    ### Home
    ### Contact
    """)



'''
## Where would you like to go?

**Please insert:**
'''

'## Date input'
#with st.echo():
d = st.date_input(
    "select pickup date", datetime.datetime(2013-7-6))
st.write('pickup_datetime:', d)


'## pickup_longitude'
with st.echo():
    number = st.number_input('Insert pickup longitude', format='%f')
st.write('pickup_longitude', number)

'## pickup_latitude'
with st.echo():
    number = st.number_input('Insert pickup latitude', format='%f')
st.write('pickup_latitude', number)

'## dropoff_latitude'
with st.echo():
    number = st.number_input('Insert dropoff latitude', format='%f')
st.write('dropoff_latitude', number)

'## dropoff_longitude'
with st.echo():
    number = st.number_input('Insert dropoff longitude', format='%f')
st.write('dropoff_longitude', number)

'## passenger_count'
with st.echo():
    number = st.number_input('Insert number of passenger(s)', format='%f')
#st.write('passenger_count', number)
st.slider("passenger_count", 0, 6)

CSS = """
h1 {
    color: purple;
}

markdown {
    color: pink;
}
"""
if st.checkbox('Inject CSS'):
    st.write(f'<style>{CSS}</style>', unsafe_allow_html=True)



'## Map'
@st.cache
def get_map_data():
    print('get_map_data called')
    return pd.DataFrame(
            np.random.randn(1000, 2) / [50, 50] + [40.73, -73.93],
            columns=['lat', 'lon']
        )

if st.checkbox('Show map', False):
    df = get_map_data()

    st.map(df)
else:
    from PIL import Image
    image = Image.open('images/map.png')
    st.image(image, caption='map', use_column_width=False)


'''
## Once we have these, let's call our API in order to retrieve a prediction

See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...

🤔 How could we call our API ? Off course... The `requests` package 💡
'''

url = 'http://taxifare.lewagon.ai/predict_fare/?key=2012-10-06%2012:10:20.0000001&pickup_datetime=2012-10-06%2012:10:20%20UTC&pickup_longitude=40.7614327&pickup_latitude=-73.9798156&dropoff_longitude=40.6513111&dropoff_latitude=-73.8803331&passenger_count=2'

if url == 'http://taxifare.lewagon.ai/predict_fare/?key=2012-10-06%2012:10:20.0000001&pickup_datetime=2012-10-06%2012:10:20%20UTC&pickup_longitude=40.7614327&pickup_latitude=-73.9798156&dropoff_longitude=40.6513111&dropoff_latitude=-73.8803331&passenger_count=2':

    st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')

'''

2. Let's build a dictionary containing the parameters for our API...

3. Let's call our API using the `requests` package...

4. Let's retrieve the prediction from the **JSON** returned by the API...

## Finally, we can display the prediction to the user
'''
