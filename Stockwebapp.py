#description : this is the stock market dash orad  to show the chat and data on same stock

# import some liraries
import streamlit as st
import pandas as pd
from PIL import Image

#add a title on this project
st.write(""" 
# Stock Market we Application  
**visually** show data on a stock ! data range from  3 jan 2000 - 30 april 2020 
""")


image=Image.open("C:/Users/Intel/Documents/python/stock_market_analyzer/stock_image.jpg")
st.image(image,use_column_width=True)

#create a side header
st.sidebar.header('User input')

#create a function to get the user input
def get_input():
    start_date=st.sidebar.text_input("Start date","03-01-2000")
    end_date = st.sidebar.text_input("End date", "30-04-2021")
    stock_symol= st.sidebar.text_input("Stock symol", "ASIANPAINT")
    return start_date,end_date,stock_symol

#create a function to get the company name
def get_company_name(symol):
    if symol=='ASIANPAINT':
        return 'Asianpaint'
    elif symol=='HDFCBANK':
        return 'Hdfcbank'
    elif symol=='RELIANCE':
        return 'Reliance'
    elif symol=='TCS':
        return 'Tcs'
    else:
        'None'

# 3this function to get the proper company data and the proper time frame from the start date and end date
def get_data(symol,start,end):
    # load the data
    if symol.upper()=='ASIANPAINT':
        df= pd.read_csv("C:/Users/Intel/Documents/python/stock_market_analyzer/Stocks/ASIANPAINT.csv")
    elif symol.upper()=='HDFCBANK':
        df = pd.read_csv("C:/Users/Intel/Documents/python/stock_market_analyzer/Stocks/HDFCBANK.csv")
    elif symol.upper()=='RELIANCE':
        df = pd.read_csv("C:/Users/Intel/Documents/python/stock_market_analyzer/Stocks/RELIANCE.csv")
    elif symol.upper()=='TCS':
        df = pd.read_csv("C:/Users/Intel/Documents/python/stock_market_analyzer/Stocks/TCS.csv")
    else:
        df= pd.DataFrame(Columns=['Date','Prev Close','Open','High','Low','Last,Close','VWAP','Volume'])

    # get the data range
    start =pd.to_datetime(start)
    end   =pd.to_datetime(end)

    #set the start and end index row  to 0
    start_row=0
    end_row=0

    # start the data from the top of the data set and go down to see
    for i in range(0,len(df)):
        if start <= pd.to_datetime(df['Date'][i]):
            start_row=i
            break

    # start  from the ottom of the data set and go up to the see
    for j in range(0,len(df)):
        if end>=pd.to_datetime(df['Date'][len(df)-1-j]):
            end_row=len(df)-1-j
            break

    # set the index to e the date
    df = df.set_index(pd.DatetimeIndex(df['Date'].values))
    return df.iloc[start_row:end_row+1,:]

# get the user input
start,end,symol=get_input()

#get the company name
company_name =get_company_name(symol.upper())

# get the data
df = get_data(symol,start,end)

# display the line chart
st.header(company_name + " Open \n")
st.line_chart(df['Open'])

st.header(company_name + " High\n")
st.line_chart(df['High'])

st.header(company_name + " Low\n")
st.line_chart(df['Low'])

st.header(company_name + " Close Price\n")
st.line_chart(df['Close'])

st.header(company_name + "Average  volume per year\n")
st.line_chart(df['VWAP'])

st.header(company_name + " Volume\n")
st.line_chart(df['Volume'])

st.header('Data statistics')
st.write(df.describe())


# run  - streamlit run Stockwebapp.py