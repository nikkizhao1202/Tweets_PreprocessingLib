# Tweets Preprocessing Library 

<ul>
  <li> Contributors: Yongyi(Nikki)Zhao</li>
</ul>

## Overview
<p> 
  Writing a Python library to perform preprocessing for a sentiment analysis tasktask with a CNN + Embedding model
</p >


## Details
<ul>
  <li> clean_text </li>
    <p> cleaning the raw text to remove URLs and any other tokens that deem unnecessary
   </p >
  <li> tokenize_text </li>
    <p>
    converting a string into an array of tokens by using the TweetTokenizer from nltk 
    </p >
  <li> replace_token_with_index </li>
   <p>
    replacing each token in a list of tokens by their corresponding index in an embedding dictionary and producing a list of indexes by using the twitter GloVe embedding dictionary
    </p >
  <li> pad_sequence </li>
    <p>
     padding a list of indices with 0 until a maximum length (max_length_tweet)
    </p >

## Requirements
<ul>
  <li> Python (3.6, 3.7) </li>
</ul>

## Reference Matrial
- [Twitter GloVe](https://nlp.stanford.edu/projects/glove/) 


## Discussion and Development

<p> Most development discussion is taking place on github in this repo.</p >

## Contributing to Tweets Preprocessing Library
<p>
Any contributions, bug reports, bug fixes, documentation improvements, enhancements to make this project better are warmly welcomed.
</p >
