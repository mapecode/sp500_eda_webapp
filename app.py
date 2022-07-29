import streamlit as st


from utils import load_index_data, file_download, price_plot

st.title('S&P 500 Index App')
st.sidebar.header('User Input Features')

# Web scraping of S&P 500 data
df = load_index_data()

sector = df.groupby('GICS Sector')

# Sidebar - Sector selection
sorted_sector_unique = sorted(df['GICS Sector'].unique())
selected_sector = st.sidebar.multiselect('Sector', sorted_sector_unique, sorted_sector_unique)

# Filtering data
df_selected_sector = df[ (df['GICS Sector'].isin(selected_sector)) ]

st.header('Display Companies in Selected Sector')
st.write('Data Dimension: ' + str(df_selected_sector.shape[0]) + ' rows and ' + str(df_selected_sector.shape[1]) + ' columns.')
st.dataframe(df_selected_sector)

# Download S&P500 data
st.markdown(file_download(df_selected_sector), unsafe_allow_html=True)


# Plot Closing Price of Query Symbol
company = st.sidebar.selectbox("Choose a company to plot it", list(df_selected_sector.Symbol))
st.set_option('deprecation.showPyplotGlobalUse', False)
st.header('Stock Closing Price of {}'.format(company))
price_plot(company)