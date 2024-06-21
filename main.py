#IT CAN TAKE SOME TIME TO (RECOMMENDED TO RUN IN GOOGLE COLAB)

from transformers import pipeline

summarizer = pipeline('summarization')
# enter text to summarize in article var 
article = ''''''
#you can play with the max length and min length
summarizer(article,max_length=140, min_length=130,do_sample=False)
