# EDA-and-Deep-Learning-CNN-Fruit-Classification-Predictions

URL Heroku : https://ilmi-fruit-classification.herokuapp.com/

## Dataset Information
URL Dataset : https://www.kaggle.com/datasets/sshikamaru/fruit-recognition

- Total number of images: 22495.
- Training set size: 16854 images (one fruit or vegetable per image).
- Test set size: 5641 images (one fruit or vegetable per image).
- Number of classes: 33 (fruits and vegetables).
- Image size: 100x100 pixels.
- Training data filename format: [fruit/vegetable name][id].jpg (e.g. Apple Braeburn100.jpg). Many images are also rotated, to help training.
- Testing data filename format: [4 digit id].jpg (e.g. 0001.jpg)

## Assignment Problems
The demand for fruits is always there at any time whether people choose to buy fruit in traditional markets, in supermarkets, buy online and even export abroad. But the problem is that sometimes there are long queues in sorting the types of fruit to be sent abroad or there are long queues to pay at the cashier. Some cases of problems, among others:

- Why are some fruits delivered late so the fruit is not in good condition?

- Why do you have to wait in long queues to pay for fruit at the cashier?

Tried to use an artificial network of image processing that can classify the types of fruit, so that what will be sent can arrive on time without sorting the fruit manually and customers waiting in long lines to buy fruit because the cashier detects the type of fruit to be made purchased by the customer.

## Computer Vision model working concept
- Data Preprocessing : This section contains the process of preparing data for the model training process, such as dividing the data into train-val-test, data transformation (normalization, encoding, etc.), and other necessary processes.
- Modeling : Able to make a model to solve the problem of Computer Vision CNN fruit classification and Do the training process several times with different hyperparameters to see the results obtained.
- Model Evaluation : Able to do Model Evaluation with matrix curve, classification report, Precision, Recall and Confusion Matrix.
- Model Improvement: Able to do Model Improvement with transfer learning
- Model Inference: Trying out a model that has been created with new data
- Model deployment using Docker and Streamlit.
