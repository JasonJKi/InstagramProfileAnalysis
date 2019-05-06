#### Understanding You through your Social Media

Social media today, for many, is the predominant way of interaction, and receiving and sharing of information with others. People are uploading their most personal, and intimate moments via photos, and videos, and it has become the go-to medium for communicating and documenting apsects of one's life. According to a survey by Global Web Index, in 2018, internet users were spending an average of 2 hours and 22 minutes per day on social networking and messaging platforms. This is an increase of 57% from 2012, when the average usage rate was at 1 hour and 30 minutes. One major social media platform is Instagram; it is the largest photo sharing site in the world. It’s estimated that 35 percent of American adults have an account with over a billion active users globally. Every post consists of photo(s) or video(s) along with some caption and keywords which documents a particular sentiment or event. Individuals lean to posting contents that are generally associated with personal interests, values or specific industries such as fashion, fitness, travel, food, music, politics, etc.  Thus, every post gives a purview of the person. With its popularity along with the advance of digital technology and production, average person can now produce high quality media at high frequencies. The aim of this work is to analyze individual’s characteristic and behavior from the collection of their media data.

There is a deep rich information in images and videos, but the data is high dimensional. And most of posts on social networks hardily contain high-level descriptions. Hence, contextualization of every posts needs to be made, defining specific feature that is relevant to defining individual characters. First, we need to define feature space that is sensible for characterizing individual posts. For this, an image labeling framework will be built using pretrained convolutional neural networks (CNN) for extracting wide array of categorical, and sentiment characteristic of the image. Complementary and similar to visual content analysis, high-level features are to be extracted from the word captions of each post using pretrained recurrent network models. All output features will undergo domain specific fine tuning to ensure sensibility and accuracy of the label and the features are weighted by the output probability of each model and combined. This process will require some handpicked parameter tuning but it will be mainly based on the data. With these feature set, we can categorize user characteristics using unsupervised grouping or clustering models. The model will be analyzed to test the validity of generated feature set. Finally, we will create a data analysis tool for characterization of individual Instagram user and a web app for visualizing the analysis along with features which will summarize the characterization of individuals circle of followers and followings. 

#### Data Collection
To obtain data, first I needed a data miner for Instagram. For this, I’ve used a combination of third-party API for Instagram data scraping, one was InstagramAPI and the other was InstagramScraper. These two APIs individually were not sufficient for me to accomplish my goals which was one, to get the following and follower information of my account and two, download images, captions, comments and number of likes for every single post that a user posted.  Two address this, I wrote a python package called InstaScraper which combined the two APIs that allowed me to quickly download data from any user which were public or that I was following. This part was the most challenging and most time consuming
