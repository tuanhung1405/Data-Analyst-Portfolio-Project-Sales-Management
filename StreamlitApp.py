import streamlit as st
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import ApiGetData
import ta
from ArimaModel import ArimaModel
from io import StringIO
import sys
import plotly.express as px
from PIL import Image

st.set_page_config(page_title='Data Analyst Portfolio Project – Sales Management
',page_icon="📶",layout="wide")

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
def main():
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
                   
                   
    col1, col2 = st.columns(2)

    with col1:
       with st.expander("Data"): 
            name = "Coin: " + coinname.get(coins)
            st.subheader(name)
            data = ApiGetData.getFinalData(coins, period)
            st.dataframe(data)

    with col2:
       with st.expander("Graph"): 
            data["MA20"] = ta.trend.sma_indicator(data['close'], window=20)
            data["MA50"] = ta.trend.sma_indicator(data['close'], window=50)
            data["MA100"] = ta.trend.sma_indicator(data['close'], window=100)

            fig = make_subplots(rows=2, cols=1, shared_xaxes=True,
                        vertical_spacing=0.03,
                        row_width=[0.2, 0.7])

    # Plot OHLC on 1st row
            fig.add_trace(go.Candlestick(x=data.index,
                                 open=data['open'],
                                 high=data['high'],
                                 low=data['low'],
                                 close=data['close'], name="OHLC"),
                  row=1, col=1)
            fig.add_trace(go.Line(x=data.index, y=data['MA20'], name="MA20", line=dict(
            color="purple",
            width=1)))
            fig.add_trace(go.Line(x=data.index, y=data['MA50'], name="MA50", line=dict(
            color="yellow",
            width=1.5)))
            fig.add_trace(go.Line(x=data.index, y=data['MA100'], name="MA100", line=dict(
            color="orange",
            width=2)))

    # Bar trace for volumes on 2nd row without legend
            fig.add_trace(go.Bar(x=data.index, y=data['volume'], showlegend=False), row=2, col=1)

    # Do not show OHLC's rangeslider plot
            fig.update(layout_xaxis_rangeslider_visible=False)

            fig.update_layout(
            autosize=False,
            width=780,
            height=540,
            margin=dict(
            l=50,
            r=50,
            b=50,
            t=50,
            pad=4))

            st.plotly_chart(fig)

    model = ArimaModel(data, period)
    
    st.write('---')
    st.write("Let's choose the period for the prediction. Please note that the below prediction uses the Arima model as a reference.")
    
    col1, col2 = st.columns(2)

    with col1:
        period = st.slider("Select the period you want to forecast.", 1, 5, 1)
    with col2:
        st.markdown(' ')

 
    st.write("Press the **START PREDICTION** button to show the model and forecast results.")
    
    if st.button("START PREDICTION"):
      st.warning(model.checkData())
      model.createDataReturn()
      st.write("Stationality test")
      warn, ADF, p_value = model.checkStationarity()
      s1 = "ADF Statistic: " + str(ADF)
      s2 = "p-value: " + str(p_value)
      st.text(s1)
      st.text(s2)
      st.warning(warn)

      st.markdown("**_Running the auto_arima can take a while. Please wait!!!_**")
      with st.expander("Summary SARIMAX Results"):
          result = model.displaySummary()

          old_stdout = sys.stdout
          sys.stdout = mystdout = StringIO()
          print(result.summary())
          sys.stdout = old_stdout
          st.text(mystdout.getvalue())

          pre = model.predict(period)
      
      col1, col2 = st.columns(2)

      with col1:
        st.write("Results of prediction:")
        st.dataframe(pre)

      with col2:
        fig2 = px.line(data, y="close", x=data.index)
        fig2.add_trace(
            go.Scatter(x=pre.index, y=pre['Price_mean'], line=dict(color="red"), name="forecast"))
        fig2.add_trace(go.Scatter(x=pre.index, y=pre['Price_upper'], line=dict(color="green", dash='dash'), name="upper", ))
        fig2.add_trace(go.Scatter(x=pre.index, y=pre['Price_lower'], line=dict(color="green", dash='dash'), name="lower", ))
        st.plotly_chart(fig2)
        
        st.markdown('---')
#background = Image.open("Nguyễn Tuấn Hưng_ Ảnh chân dung.png")
#col1, col2, col3 = st.columns([0.7, 1, 0.7])
#col2.image(background, use_column_width=True)
        
if __name__ == '__main__':
    main()
