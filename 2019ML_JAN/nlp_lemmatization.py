#!/usr/bin/env python3
import time
from  nltk.tokenize  import  sent_tokenize
from  nltk.tokenize  import  word_tokenize
from  nltk.stem import WordNetLemmatizer
from  nltk.corpus   import  stopwords
para='''
i am doing  things intelligently 
this is what the task intelligence is all about
doing thins with big efforts always leads to intelligent works.
mujhe nhi pta mai kya likh rha hu
'''
#  doing  sentence tokenization 
sent_token=sent_tokenize(para)
sent_token1=sent_tokenize(para)
#word_token=word_tokenize(para)
print("@@@@@@@@@@___________________________@@@@@@@@@@@@@")


#  stemming and lemmatization--
lemma=WordNetLemmatizer()
print(dir(lemma))

for  i  in  range(len(sent_token)):
	words=word_tokenize(sent_token[i])
	newword=[lemma.lemmatize(word) for word in words]
	sent_token[i]=' '.join(newword)

lem_sent=sent_token
lem_sent1=sent_token
print(lem_sent)

# removing  stopwords
for  j  in  range(len(lem_sent)):
	words=word_tokenize(lem_sent[j])
	newword1=[word for word  in  words if word not in stopwords.words('english') ]
	lem_sent1[j]=' '.join(newword1)

print("())))))))))))))))))))))(((((((((((((((((((")
print(lem_sent1)



'''
intelligently
intelligence---------------->intellign(NO meaning)---stemming{spam email det}
intelligent

goes
going------------------go--(meaning)---lemmatization--chatbot
gone

'''
