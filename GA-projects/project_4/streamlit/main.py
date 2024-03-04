# python -m streamlit run c:/Users/Aspire/Documents/GA/Faaiz-Khan/project_4/streamlit-widget/main.py

from datetime import date, datetime
import pandas as pd
import streamlit as st
import dict

import matplotlib.pyplot as plt


# Remove annoying warning
st.set_option('deprecation.showPyplotGlobalUse', False)

df = pd.DataFrame(dict.dict)
df.index = pd.to_datetime(df.index, format='%Y-%m-%d')


# MAIN CODE

st.header("NUH Bed Availability")
st.markdown("Prediction of bed availability for NUH, modelled using a LSTM network.")
    
# Ask for text or text file
d = st.date_input("Input date (within 3 month period)", date(2024, 1, 1),
                  min_value=date(2024, 1, 1), max_value=date(2024, 5, 22)).strftime('%Y-%m-%d')

# 1219 
# Add a button feature
if st.button("Check"):
        col1, col2 = st.columns(2)
        with col1:
            x = (df.loc[d].iloc[0])
            st.title(str(x) + '%')
            st.subheader('of beds occupied.')
            occ_bed = int(1219*x/100)
            st.subheader('A total of')
            st.title(str(1219 - occ_bed) + ' beds')
            st.subheader('out of 1219 beds will be available.')
        with col2:
            # Pie chart plot
            fig1, ax1 = plt.subplots()
            ax1.pie([x, 100-x], labels=['Occupied', 'Unoccupied'], autopct='%1.1f%%',
                    shadow=True, startangle=90)
            ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
            st.pyplot(fig1)
        
        list = ''
        for x in range(1219 - occ_bed):
             list += '🛏️'
        st.write(list)

        nurse = int(occ_bed/4)
        st.header(str(nurse) + ' nurses will be required to staff')
        st.write('(assuming a ratio of 1 nurse to 4 occupied beds).')
        list = ''
        for x in range(1219 - occ_bed):
            list += '👩‍⚕️'
        st.write(list)


#         st.subheader("URL 1:")
#         df1 = printstats(url1)
#         # st.write(scrape.mostvotes(df1))
#     with col2:
#         st.subheader("URL 2:")
#         df2 = printstats(url2)
#         # st.write(scrape.mostvotes(df2))

#     col1, col2 = st.columns(2)
#     with col1:
#         score1 = printwc(df1)
#     with col2:
#         score2 = printwc(df2)

#     # Compare the 2 scores
#     compare = {'URL 1': score1, 'URL 2': score2}
#     st.subheader('Overall, posts from ' + max(compare, key=compare.get)
#                 + ' favour Generative AI art more than posts from '
#                 + min(compare, key=compare.get) + '.')
        
