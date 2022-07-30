# EDA-and-Deep-Learning-CNN-Fruit-Classification-Predictions

URL Heroku : https://ilmi-fruit-classification.herokuapp.com/

Dasboard Heroku

![Screenshot (112)](https://user-images.githubusercontent.com/105533908/181878984-b9692af9-fa35-4e61-b25b-1be71a56c140.png)

## Assignment Problems
The demand for fruits is always there at any time whether people choose to buy fruit in traditional markets, in supermarkets, buy online and even export abroad. But the problem is that sometimes there are long queues in sorting the types of fruit to be sent abroad or there are long queues to pay at the cashier. Some cases of problems, among others:

- Why are some fruits delivered late so the fruit is not in good condition?

- Why do you have to wait in long queues to pay for fruit at the cashier?

Tried to use an artificial network of image processing that can classify the types of fruit, so that what will be sent can arrive on time without sorting the fruit manually and customers waiting in long lines to buy fruit because the cashier detects the type of fruit to be made purchased by the customer.

## Dataset Information
URL Dataset : https://www.kaggle.com/datasets/sshikamaru/fruit-recognition

- Total number of images: 22495.
- Training set size: 16854 images (one fruit or vegetable per image).
- Test set size: 5641 images (one fruit or vegetable per image).
- Number of classes: 33 (fruits and vegetables).
- Image size: 100x100 pixels.
- Training data filename format: [fruit/vegetable name][id].jpg (e.g. Apple Braeburn100.jpg). Many images are also rotated, to help training.
- Testing data filename format: [4 digit id].jpg (e.g. 0001.jpg)

## Convolutional Neural Network (CNN)
![1_XbuW8WuRrAY5pC4t-9DZAQ](https://user-images.githubusercontent.com/105533908/181879042-195c3dd0-99e2-4556-b5b3-09162e7f113b.jpeg)

In deep learning, a convolutional neural network (CNN, or ConvNet) is a class of artificial neural network (ANN), most commonly applied to analyze visual imagery. CNNs are also known as Shift Invariant or Space Invariant Artificial Neural Networks (SIANN), based on the shared-weight architecture of the convolution kernels or filters that slide along input features and provide translation-equivariant responses known as feature maps. Counter-intuitively, most convolutional neural networks are not invariant to translation, due to the downsampling operation they apply to the input. They have applications in image and video recognition, recommender systems, image classification, image segmentation, medical image analysis, natural language processing, brain–computer interfaces and financial time series.

## Process Concept Completion
- Data Preprocessing : This section contains the process of preparing data for the model training process, such as dividing the data into train-val-test, data transformation (normalization, encoding, etc.), and other necessary processes.
- Modeling : Able to make a model to solve the problem of Computer Vision CNN fruit classification and Do the training process several times with different hyperparameters to see the results obtained.
- Model Evaluation : Able to do Model Evaluation with matrix curve, classification report, Precision, Recall and Confusion Matrix.
- Model Improvement: Able to do Model Improvement with transfer learning
- Model Inference: Trying out a model that has been created with new data
- Model deployment using Docker and Streamlit.

## Reference
- Anggriawan, dan Toti Indrawati. 2013. Peran Komoditi Gambir Terhadap Perekonomian Kabupaten Lima Puluh Kota Provinsi Sumatera Barat. Jurnal Ekonomi. Volume 21. Nomor 2 Juni 2013. Jurusan Ekonomi Pembangunan. Fakultas Ekonomi. Universitas Riau.
- Asrianti. 2013. Strategi Pengembangan Usaha Pepaya California Pada Mitra Alam Kabupaten Bogor Jawa Barat. Bogor : Fakultas Ekonomi Manajemen, Institut Pertanian Bogor.
- https://medium.com/@samuelsena/pengenalan-deep-learning-part-7-convolutional-neural-network-cnn-b003b477dc94
- http://repository.unmuhjember.ac.id/2334/3/3.%20ISI%20BAB%201.pdf
- https://www.pertanian.go.id/home/?show=news&act=view&id=1838
- https://en.wikipedia.org/wiki/Convolutional_neural_network
- https://www.kaggle.com/code/muhamadrialdy/fruit-classification
