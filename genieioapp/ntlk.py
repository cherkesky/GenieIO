import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords, state_union
from nltk.stem import PorterStemmer
from nltk.tokenize import PunktSentenceTokenizer

SENT_WISH = "I wish to finish my capstone on time"
train_text = state_union.raw("2005-GWBush.txt")
filtered_sentence = []
stemmed_sentence = []

stop_words = set(stopwords.words('english'))
word_tokens = word_tokenize(SENT_WISH)

filtered_sentence = [w for w in word_tokens if not w in stop_words]

ps = PorterStemmer()
for w in filtered_sentence:
        stemmed_sentence.append(ps.stem(w))

sample_text=SENT_WISH
custom_sent_tokenizer = PunktSentenceTokenizer(train_text)
tokenized = custom_sent_tokenizer.tokenize(sample_text)
for i in tokenized[:5]:
    words = nltk.word_tokenize(i)
    tagged = nltk.pos_tag(words)

print ("TAGGED:", tagged)

for noun in tagged:
    if noun[1]=="NN" or noun[1]=="NNS" or noun[1]=="VBG" or noun[1]=="NNP":
        print (noun[0])
        












# # Tokenizing and removing stop words
# print ("*************************************************************")
# print ("***********        TOKENIZING / STOP WORDS       ************")
# print ("*************************************************************")
# stop_words = set(stopwords.words('english'))
# word_tokens = word_tokenize(EXAMPLE_TEXT)
# filtered_sentence = [w for w in word_tokens if not w in stop_words]
# filtered_sentence = []
# for w in word_tokens:
#     if w not in stop_words:
#         filtered_sentence.append(w)

# print(word_tokens)
# print(filtered_sentence)

# # Stemming
# print ("*************************************************************")
# print ("*************             STEMMIMG               ************")
# print ("*************************************************************")

# ps = PorterStemmer()
# example_words = ['I', 'want', 'finish', 'capstone', 'successfully', '.', 'On', 'time']
# for w in example_words:
#     print(ps.stem(w))

# #Part Of Speech Tagging
# print ("*************************************************************")
# print ("*************            POS TAGGING             ************")
# print ("*************************************************************")
# train_text = state_union.raw("2005-GWBush.txt")
# sample_text = example_words
# custom_sent_tokenizer = PunktSentenceTokenizer(train_text)
# tokenized = custom_sent_tokenizer.tokenize(EXAMPLE_TEXT)

# def process_content():
#     try:
#         for i in tokenized[:5]:
#             words = nltk.word_tokenize(i)
#             tagged = nltk.pos_tag(words)
#             namedEnt = nltk.ne_chunk(tagged, binary=True)

#             print(tagged)

#             print(namedEnt)

#     except Exception as e:
#         print(str(e))


# process_content()


# print ("*************************************************************")
# print ("*************               CHUNKING             ************")
# print ("*************************************************************")
# for i in tokenized:
#     words = nltk.word_tokenize(i)
#     tagged = nltk.pos_tag(words)
#     chunkGram = r"""Chunk: {<RB.?>*<VB.?>*<NNP>+<NN>?}"""
#     chunkParser = nltk.RegexpParser(chunkGram)
#     chunked = chunkParser.parse(tagged)
#     print(chunked)  



