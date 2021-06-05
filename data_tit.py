# 1)choose any dataset from given websites(dataset_repo.txt) and use NumPy,Pandas,Seaborn Libraries and deploy using Streamlit
# in Heroku?
#
# * There must Complete Analaysis Using NumPy,Pandas,Seaborn Libraries.
# *Share the github& heroku link in  a text file

#import required libraries
import numpy as np
import pandas as pd
import seaborn as sns
import streamlit as st

st.set_option('deprecation.showPyplotGlobalUse', False)

st.title('TITANIC - FOR FIRST AND LAST')
data_set = pd.read_csv('titanic.csv')

st.subheader('Sample data of titanic - first 5 rows')
ship = data_set.head(5)
st.table(ship)

st.sidebar.header("DASHBOARD")
st.sidebar.subheader('Number of Male and Female passengers')
passengers_sex = data_set.groupby('Sex')
st.sidebar.table(passengers_sex.size())

passengers_class = data_set.groupby('Pclass')
st.sidebar.subheader('Passenger Class')
st.sidebar.table(passengers_class.size())

st.sidebar.subheader('Total Passengers')
st.sidebar.markdown(len(data_set.PassengerId))

total_survived = data_set['Survived'].sum()
st.sidebar.subheader("Total Survived")
st.sidebar.markdown(total_survived)

sets = data_set[['Survived','Age']].fillna(1)
average_age_survived = round(sets['Age'].mean())
st.sidebar.subheader('Average age survived')
st.sidebar.markdown(average_age_survived)

st.subheader("Correlation between age and survived")
sns.heatmap(sets.corr())
st.pyplot()

st.subheader("Gender Survived")
sns.barplot(x='Sex',y = 'Survived',data = data_set)
st.pyplot()

s = data_set[['Pclass','Fare','Cabin']].fillna(0)

cab = s.groupby('Cabin')
st.text(cab.size()['B22'])

cab_list = []
for i in s['Cabin']:
    if (i not in cab_list) and (i != 0):
        cab_list.append(i)
st.subheader("Heads in a cabin")
cabin_selected = st.selectbox("Select Cabin",cab_list)
st.table(s.loc[(s.Cabin == cabin_selected)])


def check_survived(ss):
    if ss == 1:
        return 'Survived'
    elif ss == 0:
        return 'Not Survived'


# sirvived_list = data_set.applymap(check_survived)
data_set = data_set.fillna(0)
tick_det = data_set[['Ticket','PassengerId','Pclass','Name','Sex','Age','Cabin']]
st.subheader("Ticket Details")
ticket = st.text_input("Enter Ticket number...")
s_data =  tick_det.loc[(tick_det.Ticket == ticket)]
st.table(s_data.iloc[:,1:])


st.subheader("Check SUrvived or Not")
st.markdown("Use the ticket number to get the passenger id of the person you searching from above box")
pass_id = st.selectbox("Select id ",data_set.PassengerId)
if data_set.Survived[pass_id-1] == 1:
    st.success('Survived')
else:
    st.error('Not Survived')
