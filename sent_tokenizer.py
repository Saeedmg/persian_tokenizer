# Loading Libraries
from nltk.tokenize import PunktSentenceTokenizer
from nltk.corpus import webtext
import pickle

a = open('data.txt', 'r', encoding='utf-8')
text = a.read()
a.close()

# sent_tokenizer = PunktSentenceTokenizer(text) # for traning your model
# sents_1 = sent_tokenizer.tokenize(text)
# print(len(sents_1))


# saving
# with open('tokenizer.pickle', 'wb') as handle:
#     pickle.dump(sent_tokenizer, handle, protocol=pickle.HIGHEST_PROTOCOL)


# loading
with open('tokenizer.pickle', 'rb') as handle:
    sent_tokenizer = pickle.load(handle)

sents_1 = sent_tokenizer.tokenize(text)  
print(len(sents_1))

f = open('finale.txt', 'w', encoding='utf-8')
for sent in sents_1:
	if sent:
		f.write(sent+'\n')
f.close()	
  