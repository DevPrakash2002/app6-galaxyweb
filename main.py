import streamlit as st
import requests

st.set_page_config(layout="wide")
apikey = "4JZVqFiNOXNdI9igUAUN69jCJJPgpQt2Lc96dATz"
url = f"https://api.nasa.gov/planetary/apod?api_key={apikey}"

request = requests.get(url)

print(request.content)

content = request.json()

response = requests.get(content['hdurl'])
print(response)

with open("image.jpg", 'wb') as file:
    file.write(response.content)

st.title('Daily Galaxy Knowledge')
st.subheader(f'{content["title"]}')
st.image('image.jpg')
st.write(f'{content["explanation"]}')



