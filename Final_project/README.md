# Emojify !

Have we ever wanted to make your text messages more expressive? Our emojifier app will help you do that. So rather than writing "Congratulations on the promotion! Lets get coffee and talk. Love you!" the emojifier can automatically turn this into "Congratulations on the promotion! 👍 Lets get coffee and talk. ☕️ Love you! ❤️"

We will implement a model which inputs a sentence (such as "Let's go see the baseball game tonight!") and finds the most appropriate emoji to be used with this sentence (⚾️). In many emoji interfaces, we need to remember that ❤️ is the "heart" symbol rather than the "love" symbol. But using word vectors, you'll see that even if our training set explicitly relates only a few words to a particular emoji, our algorithm will be able to generalize and associate words in the test set to the same emoji even if those words don't even appear in the training set. This allows ous to build an accurate classifier mapping from sentences to emojis, even using a small training set.


# Libary used

  * emoji
  * numpy
  * pandas
  * csv
  * matplotlib
  
# Dataset used
  
  * train_emoji.csv
  * test_emoji.csv
  * glove.6B.50d.txt
  
# Reference

  * Dataset
  
    * https://www.kaggle.com/watts2/glove6b50dtxt
    * https://www.kaggle.com/alvinrindra/emojify
    
  * https://towardsdatascience.com/introduction-to-word-embedding-and-word2vec-652d0c2060fa

  * https://medium.com/data-science-group-iitr/word-embedding-2d05d270b285
  
  * https://www.geeksforgeeks.org/python-program-to-print-emojis/
  
  * https://deeplizard.com/learn/video/v_4KWmkwmsU
  
