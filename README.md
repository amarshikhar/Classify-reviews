# Classify-reviews

The goal is to identify the reviews where the semantics of review text does not match rating, that is to identify such ratings where review text is good, but rating is negative- so that the support team can point this to users.

The data used in the project will be in "chrome_review.csv".

"Classify reviews.ipynb" file contains coding for the model to train to get the result.

The model is selected by performing hyper parameter tuning on different algorithms like Logistic regression, random forest classifier. The model which gives best accuracy for both train and test dataset is saved and choosen for our solution.

I have deployed it in Streamlit, code for deployment is written in "review_model.py" where we load the model and deployed it in "Streamlit".

Following link is the live link for the project where we can verify by uploading a csv file.

[Link to app](https://share.streamlit.io/amarshikhar/classify-reviews/main/review_model.py)

I have uploaded a csv file namely "test_data.csv", In which I had made some changes in the review ratings for the positive reviews. It contains 100 records, out of these I have changed arround 15 positive reviews ratings to 1.

So that when we upload this file, the api should display all these 15 values.

Steps in deploying this model.(After all the necessary coding files are ready)
