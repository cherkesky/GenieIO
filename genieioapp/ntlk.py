import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords, state_union
from nltk.stem import PorterStemmer
from nltk.tokenize import PunktSentenceTokenizer

EXAMPLE_TEXT = "I want to finish my capstone successfully. On time."

# Tokenizing and removing stop words
print ("*************************************************************")
print ("***********        TOKENIZING / STOP WORDS       ************")
print ("*************************************************************")
stop_words = set(stopwords.words('english'))
word_tokens = word_tokenize(EXAMPLE_TEXT)
filtered_sentence = [w for w in word_tokens if not w in stop_words]
filtered_sentence = []
for w in word_tokens:
    if w not in stop_words:
        filtered_sentence.append(w)

print(word_tokens)
print(filtered_sentence)

# Stemming
print ("*************************************************************")
print ("*************             STRMMIMG               ************")
print ("*************************************************************")

ps = PorterStemmer()
example_words = ['I', 'want', 'finish', 'capstone', 'successfully', '.', 'On', 'time']
for w in example_words:
    print(ps.stem(w))

#Part Of Speech Tagging
print ("*************************************************************")
print ("*************            POS TAGGING             ************")
print ("*************************************************************")
train_text = state_union.raw("2005-GWBush.txt")
sample_text = example_words
custom_sent_tokenizer = PunktSentenceTokenizer(train_text)
tokenized = custom_sent_tokenizer.tokenize(EXAMPLE_TEXT)

def process_content():
    try:
        for i in tokenized[:5]:
            words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)
            print(tagged)

    except Exception as e:
        print(str(e))


process_content()