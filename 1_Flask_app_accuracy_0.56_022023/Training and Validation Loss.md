## Training Loss
The training loss is a metric used to assess how a deep learning model fits the training data. That is to say, it assesses the error of the model on the training set. Note that, the training set is a portion of a dataset used to initially train the model. Computationally, the training loss is calculated by taking the sum of errors for each example in the training set.

It is also important to note that the training loss is measured after each batch. This is usually visualized by plotting a curve of the training loss.

## Validation Loss
On the contrary, validation loss is a metric used to assess the performance of a deep learning model on the validation set. The validation set is a portion of the dataset set aside to validate the performance of the model. The validation loss is similar to the training loss and is calculated from a sum of the errors for each example in the validation set.

Additionally, the validation loss is measured after each epoch. This informs us as to whether the model needs further tuning or adjustments or not. To do this, we usually plot a learning curve for the validation loss.

## Implications of Training and Validation Loss
In most deep learning projects, the training and validation loss is usually visualized together on a graph. The purpose of this is to diagnose the model’s performance and identify which aspects need tuning. To explain this section, we’ll use three different scenarios

Underfitting
Let’s consider scenario 1, the image illustrates that the training loss and validation loss are both high:

![image](https://user-images.githubusercontent.com/113517699/208231828-3d0bb672-676a-48c7-b791-1538fcb3a62b.png)

At times, the validation loss is greater than the training loss. This may indicate that the model is underfitting. Underfitting occurs when the model is unable to accurately model the training data, and hence generates large errors.

Furthermore, the results in scenario 1 indicate that further training is needed to reduce the loss incurred during training. Alternatively, we can also increase the training data either by obtaining more samples or augmenting the data.

5.2. Overfitting
In scenario 2, the validation loss is greater than the training loss, as seen in the image:

![image](https://user-images.githubusercontent.com/113517699/208231823-2d763875-df43-4572-83db-5ac901378d9b.png)

This usually indicates that the model is overfitting, and cannot generalize on new data. In particular, the model performs well on training data but poorly on the new data in the validation set. At a point, the validation loss decreases but starts to increase again.

A notable reason for this occurrence is that the model may be too complex for the data or that, the model was trained for a long period. In this case, training can be halted when the loss is low and stable, this is usually known as early stopping. Early stopping is one of the many approaches used to prevent overfitting.

5.3. Good Fit
In scenario 3, in the image below, the training loss and validation loss both decrease and stabilize at a specific point

![image](https://user-images.githubusercontent.com/113517699/208231816-287ea7c0-f43c-4e33-85fd-c44cabf6d403.png)

This indicates an optimal fit, i.e a model that does not overfit or underfit.

Reference - https://www.baeldung.com/cs/training-validation-loss-deep-learning#:~:text=A%20high%20loss%20value%20usually,the%20error%20in%20different%20ways.

