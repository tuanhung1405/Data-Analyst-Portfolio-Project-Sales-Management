import streamlit as st
from io import StringIO
import sys
from PIL import Image

st.set_page_config(page_title='Data Analyst Portfolio Project – Sales Management',page_icon="📶",layout="wide")

st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #3498DB;">
  <a class="navbar-brand" href="https://online.flippingbook.com/link/654193/" target="_blank">My Resume</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link" href=https://github.com/hunter1405?tab=repositories" target="_blank">Portfolio</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="https://www.facebook.com/hunter.dasick/" target="_blank">Facebook</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="www.linkedin.com/in/hung-tuan-nguyenf" target="_blank">Linkedin</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)

h = st.markdown("""
<style>
div.fullScreenFrame > div {
    display: flex;
    justify-content: center;
}
</style>""", unsafe_allow_html=True)

#Title
original_title='<p style="text-align: center; color:#3498DB; text-shadow: 2px 2px 4px #000000; font-size: 60px;">Data Analyst Portfolio Project – Sales Management</p>'
st.markdown(original_title, unsafe_allow_html=True)


st.markdown("This is a project of **Nguyen Tuan Hung** from **UEL** that aims to build a web application to forecast the trend of coin prices using the ARIMA model. The data was crawled from API of Coinbase. You can use the model however you want, but you carry the risk for your actions.")

st.write('---')
    #st.sidebar.write("Choose your coin and the period")
    #coins = st.sidebar.selectbox("Which coin", (tup))
    #period = st.sidebar.selectbox("Choose the period", ("DAY", "1WEEK", "2WEEK", "MONTH"))
    
    # Store the initial value of widgets in session state
st.header('Business Request & User Stories')
st.write("The business request for this data analyst project was an executive sales report for sales managers. Based on the request that was made from the business we following user stories were defined to fulfill delivery and ensure that acceptance criteria’s were maintained throughout the project.")
data = {'As a (role)': ['Sales Manager', 'Sales Representative', 'Sales Representative', 'Sales Manager'],
         'I want (request / demand)': ['To get a dashboard overview of internet sales', 'A detailed overview of Internet Sales per Customer', 'A detailed overview of Internet Sales per Products', 'A dashboard overview of internet salesr'],
         'So that I (user value)': ['Can follow better which customers and products sells the best', 'Can follow up my customers that buys the most and who we can sell more to', 'Can follow up my Products that sells the most', 'Follow sales over time against budgetr'],
         'Acceptance Criteria': ['A Power BI dashboard which updates data once a day', 'A Power BI dashboard which allows me to filter data for each customer', 'A Power BI dashboard which allows me to filter data for each Product', 'A Power Bi dashboard with graphs and KPIs comparing against budget.']}

df = pd.DataFrame(data)
st.dataframe(df)
                   

    
