# Research on Social Recommenders

### Table of Contents
1. [Introduction](#introduction)
2. [Files](#files)
3. [References](#references)

## Introduction<a name="introduction"></a>
This project tries to evaluate the performance of SocialMF [1] and SocialFD [2]. More accurately, the contributions of this project are:
• Create a new large dataset, extending a prior dataset called TwitterEgo [3], with high quality social circle information extracted from Twitter
• Perform extensive experiments on the SocialMF and SocialFD algorithms with the datasets that these algorithms were tested on and our new dataset
• Compare the results of these experiments based on the evaluation metrics including Root Mean Squared Error (RMSE) and Mean Absolute Error (MAE)
• Investigate the performance of these two models when there is no trust between any users i.e., the number of trust statements is 0

This folder contains codes used in experimentation apart from the source code taken from https://github.com/Coder-Yu/RecQ

## Files<a name="files"></a>
**Data Generation** : This folder contains the code used to generated TwitterEgo social rating network dataset from [Twitter](https://snap.stanford.edu/data/egonets-Twitter.html) data

**HyperParameterTuning**: Contains sample code used for tuning hyperparameters discussed in the paper

**TwitterEgo**: This folder contains the social rating network dataset
 - ratings_data.txt: contains the ratings expressed by users. Here the ratings are binary.   '1' indicates that user liked the tweet and '0' indicates that user did not react to it
 - trust_data.txt: contains trust data of ussers 

### References<a name="references"></a>
1. M. Jamali and M. Ester. A Matrix Factorization Technique with Trust Propagation for Recommendation in Social Networks, RecSys 2010, pages 135-142
2. J. Yu, M. Gao, W. Rong, Y. Song and Q. Xiong, "A Social Recommender Based on Factorization and Distance Metric Learning," in IEEE Access, vol. 5, pp. 21557-21566, 2017.
3. J. McAuley and J. Leskovec. Learning to Discover Social Circles in Ego Networks. NIPS, 2012
