# TwitteEgo Dataset

This dataset is extension of the [Social Circles: Twitter](https://snap.stanford.edu/data/egonets-Twitter.html) dataset[1].

## Data Format

**`ratings_data.txt`** - This file contains the ratings given by users to items. Here ratings are nothing but if the user has reacted to a tweet, i.e. if a user likes/retweets a tweet, it is considered as user's reaction to that tweet.

Every line has the following format:

      user_id item_id rating_value

      For example,
     
      53870594 185015205342883840 1
      
      represents the fact "user 53870594 has reacted to tweet 185015205342883840 "


**`trust_data.txt`** -  This file contains the trust statements issued by users.

Every line has the following format:

      source_user_id target_user_id trust_statement_value
      
      For example, the line
      
      59804598 7860742 1
      
      represents the fact "user 59804598 has expressed a positive trust statement on user 7860742"

***Note:***
- *trust_statement_value is always 1 (since in the dataset there are only positive trust statements and not negative ones (distrust)).*
- *There are no distrust statements in the dataset (block list) but only trust statements (web of trust), because the block list is kept private and not shown on the site.*

### References:
1. J. McAuley and J. Leskovec. [Learning to Discover Social Circles in Ego Networks](http://i.stanford.edu/~julian/pdfs/nips2012.pdf). NIPS, 2012.
2. SNAP [Social Circles: Twitter](https://snap.stanford.edu/data/egonets-Twitter.html) dataset
