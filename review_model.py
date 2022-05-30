# load the model
import streamlit as st
import joblib
import pandas as pd
import numpy as np
import re
import utils
from nltk.corpus import stopwords
# import nltk 
from nltk.stem.porter import PorterStemmer

model=joblib.load('model.mod')
data=pd.read_csv('test_data.csv')
#test_data=pd.DataFrame()
#ref=pd.DataFrame()
# creating object for PorterStemmer
p=PorterStemmer()

def classify(test):
	#test_data=pd.read_csv(filename)
	#ref=pd.read_csv(filename)
	df=words(test)
	X=df['Text'].values
	y_pred=model.predict(X)
	return y_pred

def words(data):
    l=[]
    for i in range(0,len(data)):
        q=re.sub("[^a-zA-Z]"," ",str(data['Text'][i]))
        q=q.lower()
        q=q.split()
        q= [p.stem(word) for word in q if not word in stopwords.words('english')]
        q=' '.join(q)
        l.append(q)
    for i in range(len(l)):
        data['Text'][i]=l[i]
    return data
    
def main():
	st.title('Review classifier using NLP')
	st.write('This app is to identify the reviews where the semantics of review text does not match rating.')
	st.write('We need to upload a "csv" file of following "format" to use the app and click on "classify" button.')
	st.write(data.head())
	
	html_temp="""
    <div style="background-color:tomato;padding:10px;">
    <h2 style="color:white;text-align:center;">Review classifier using NLP</h2>
    </div>
    """
	st.markdown(html_temp,unsafe_allow_html=True)
	
	st.subheader("Input CSV file to classify reviews")
	filename = st.file_uploader("upload a file", type=("csv"))
	if filename is not None:
		try:
			if st.button('classify'):
				test_data=pd.read_csv(filename)
				ref_data=test_data.copy(deep=True)
				y_pred=classify(test_data)
				review_ID=[]
				for i in range(len(y_pred)):
					if ( (y_pred[i]==1) and (ref_data['Star'][i]<2)):
						review_ID.append(ref_data['ID'][i])
				result=ref_data[ref_data['ID'].isin(review_ID)]
				result.reset_index(inplace=True)
				result=result.iloc[:,1:]
				st.subheader('Classified Reviews')
				st.write('Reviews where the semantics of review text does not match rating.')				
				st.write(result)
		except Exception as e:
			st.exception(f'Error: {e}')
			
			
  
if __name__=='__main__':
	main()