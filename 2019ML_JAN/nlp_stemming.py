#!/usr/bin/env python3
import time
from  nltk.tokenize  import  sent_tokenize
from  nltk.tokenize  import  word_tokenize
from nltk.stem import PorterStemmer
from  nltk.stem import WordNetLemmatizer
para='''
i am doing  things intelligently 
this is what the task intelligence is all about
doing thins with big efforts always leads to intelligent works.
mujhe nhi pta mai kya likh rha hu
'''
#  doing  sentence tokenization 
sent_token=sent_tokenize(para)
#word_token=word_tokenize(para)
print(sent_token)
print("@@@@@@@@@@___________________________@@@@@@@@@@@@@")



#  stemming and lemmatization--
stemming=PorterStemmer()
lemma=WordNetLemmatizer()

for  i  in  range(len(sent_token)):
	#print(sent_token[i])
	words=word_tokenize(sent_token[i])
	#print(words)
	#print("____________________")
	stem_words=[stemming.stem(word) for word in words]
	#print("@@@@@@@@@@@@@@@@@@@@@@@@@@@2")
	#print(stem_words)
	sent_token[i]=' '.join(stem_words)


print(sent_token)






'''
intelligently
intelligence---------------->intellign(NO meaning)---stemming{spam email det}
intelligent

goes
going------------------go--(meaning)---lemmatization--chatbot
gone

'''
#  performing  stemming 
stem1=PorterStemmer()
'''
for i  in  range(len(sent_token)):
	words=word_tokenize(sent_token[i])
	print("Stemming----------------------->>")
	newword=[stem1.stem(word)  for  word  in  words]
	print(newword)
	data=" ".join(newword)
	print(data)

'''
