# Classify-reviews

The goal is to identify the reviews where the semantics of review text does not match rating, that is to identify such ratings where review text is good, but rating is negative- so that the support team can point this to users.

The data used in the project will be in "chrome_review.csv".

"Classify reviews.ipynb" file contains coding for the model to train to get the result.

The model is selected by performing hyper parameter tuning on different algorithms like Logistic regression and Naive Bayes. The model which gives best accuracy for both train and test dataset is saved and choosen for our solution.

I have deployed it in Streamlit, code for deployment is written in "review_model.py" where we load the model and deployed it in "Streamlit".

Following link is the live link for the project where we can verify by uploading a csv file.

[Link to app](https://share.streamlit.io/amarshikhar/classify-reviews/main/review_model.py)

I have uploaded a csv file namely "test_data.csv", In which I had made some changes in the review ratings for the positive reviews. It contains 100 records, out of these I have changed arround 15 positive reviews ratings to 1.

So that when we upload this file, the api should display all these 15 values.

Steps in deploying this model.(After all the necessary coding files are ready)

To deploy on streamlit:

>Goto stramlit, signup using github

>Put code in your github repository

>Enter the required fields

Grammar checker:

Using pretrained model we labeled the grammer as correct or incorrect.

>ipynb file is grammar_reviews

>review_output is the outpul file

Regex pattern:

{"orders":[{"id":1},{"id":2},{"id":3},{"id":4},{"id":5},{"id":6},{"id":7},{"id":8},{"id":9},{"id":10},{"id":11},{"id":648},{"id":649},{"id":650},{"id":651},{"id":652},{"id":653}],"errors":[{"code":3,"message":"[PHP Warning #2] count(): Parameter must be an array or an object that implements Countable (153)"}]}

\d.*\d.*\d.*\d.*\d.*\d.*\d.*\d.*\d.*10.*11.*648.*649.*650.*651.*652.*653.*\d
