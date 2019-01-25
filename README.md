# Movie Reviews Classifier

A text classifier of movie reviews as a chatbot on Telegram.

## Dataset

>  Movie reviews collected from [IMDb](https://www.imdb.com/).
>
> http://ai.stanford.edu/~amaas/data/sentiment/

- User reviews of movies on IMDb
- A review is either labelled as positive or negative
- There are a total of 25,000 reviews grouped as a training set, and another 25,000 reviews grouped as a test set.
- There are also some unlabelled data
- Preprocessed data are also available in the compressed file

## Library

> [scikit-learn](https://scikit-learn.org/)
>
> Facebook’s [fastText](https://github.com/facebookresearch/fastText) library

## Model Training

1. **Data Preparation**
   - Randomly split the full dataset into a training set with 70% of the data, and a test set with 30% of the data.
   - The ratio of positive to negative reviews is roughly 1:1 in both the training and test set.

2. **Train**

   1. Using a Naive Bayes Classifier

      - Using `CounterVectorizer` and `TfidfVectorizer` to vectorize the input data.

   2. Using a Logistic Regression Classifier

      - Using `CounterVectorizer` and `TfidfVectorizer` to vectorize the input data.

   3. Adding Bi-grams

   4. Using fastText

3. **Model Persistence**
   - Choose the model that has the higheset score to save.

## Deployment

Whenever the telebot receives a message from a user, it will pass the message into the text classification model and send the result back to user after the prediction. 

User should see the following result:

```
Input  : This is a wonderful movie!
Output : This is a positive review! (0.89)

Input  : I will not recommend this movie to my friends
Output : This is a negative review! (0.23)
```

