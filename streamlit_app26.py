# import streamlit as st
# import requests

# st.title('🏀 Bored API app')

# st.sidebar.header('Input')
# selected_type = st.sidebar.selectbox('Select an activity type', ["education", "recreational", "social", "diy", "charity", "cooking", "relaxation", "music", "busywork"])

# suggested_activity_url = f'http://www.boredapi.com/api/activity?type={selected_type}'
# json_data = requests.get(suggested_activity_url)
# suggested_activity = json_data.json()

# c1, c2 = st.columns(2)
# with c1:
#   with st.expander('About this app'):
#     st.write('Are you bored? The **Bored API app** provides suggestions on activities that you can do when you are bored. This app is powered by the Bored API.')
# with c2:
#   with st.expander('JSON data'):
#     st.write(suggested_activity)

# st.header('Suggested activity')
# st.info(suggested_activity['activity'])

# col1, col2, col3 = st.columns(3)
# with col1:
#   st.metric(label='Number of Participants', value=suggested_activity['participants'], delta='')
# with col2:
#   st.metric(label='Type of Activity', value=suggested_activity['type'].capitalize(), delta='')
# with col3:
#   st.metric(label='Price', value=suggested_activity['price'], delta='')

import streamlit as st
import requests

st.title('🏀 Bored API app')

st.sidebar.header('Input')
selected_type = st.sidebar.selectbox('Select an activity type', [
    "education", "recreational", "social", "diy", "charity",
    "cooking", "relaxation", "music", "busywork"
])

suggested_activity_url = f'http://www.boredapi.com/api/activity?type={selected_type}'

try:
    response = requests.get(suggested_activity_url)
    response.raise_for_status()  # 检查请求是否成功

    # 打印响应内容以进行调试
    st.write("Response text:", response.text)

    suggested_activity = response.json()  # 尝试解析JSON

    # 显示结果
    c1, c2 = st.columns(2)
    with c1:
        with st.expander('About this app'):
            st.write('Are you bored? The **Bored API app** provides suggestions on activities that you can do when you are bored. This app is powered by the Bored API.')
    with c2:
        with st.expander('JSON data'):
            st.write(suggested_activity)

    st.header('Suggested activity')
    st.info(suggested_activity['activity'])

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(label='Number of Participants', value=suggested_activity['participants'], delta='')
    with col2:
        st.metric(label='Type of Activity', value=suggested_activity['type'].capitalize(), delta='')
    with col3:
        st.metric(label='Price', value=suggested_activity['price'], delta='')

except requests.exceptions.HTTPError as e:
    st.error(f"HTTP error occurred: {e}")
except requests.exceptions.RequestException as e:
    st.error(f"Error occurred while making the request: {e}")
except ValueError as e:
    st.error("JSON parsing error. The response might not be a valid JSON.")
