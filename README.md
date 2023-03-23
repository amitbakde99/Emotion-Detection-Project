# ZAF004_CV_EmotionDetection

### Project Methodology 

We need to validate both Static and dynamic models for different scenarios
- Evaluate classification techniques like Bayersian classifiers, deep belief networks, AUDN (action aware deep
networks)

- For Dynamic models we look at DBM (dynamic bayesian model) such as hidden markov models
- even RNN is used for eg: to predict real valued position of an expression, we need to cluster the data and perform
kernel regression
- More interesting would be to look at DBLSTM (deep bidirectinal LSTM)
- By using CNN with LSTM we can build the model that can track objects (sitting, standing, sleeping, walking)
- Big data frameworks on AWS will be used in deployment - Spark with EMR will be initiated by lambda services - S3
buckets will hold footage data in realtime
- for local environment - we will take the approach of part to whole - each component will be made to
work separately - major integrations to happen only between mid to year end
- Focus on BDLSTM, learn about AlexNet, train on emotion images, train on emotion simple videos
train next on CCTV footage of low quality and high quality. Airport control have promised high quality cameras with
Intellgent zoom.
- Be aware of SVM, YOLO, Autoencoders, VGG, LSTM as a background

Before you commit:

#### As for further methodology, consider stacked neural networks. For emotion set - consider not only basic - sad, happy, inched body language (! For camera input) like fidgeting, twitching.

#### Consider search for specific emotion like intention to do smth, to take an action. Assume, the person is onboard of the airline and he is a terrorist. Which emotion would help to detect his intention and at least consider him with some doubts?

Test sample (four different smiles): https://drive.google.com/drive/folders/1oPJcfAu3tmoSHOaS4dtM4T3k7FRay6u4?usp=share_link
