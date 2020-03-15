import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords, state_union
from nltk.tokenize import PunktSentenceTokenizer


def harvest(wish_for_harvesting):

    wishnltk=[]

    SENT_WISH = wish_for_harvesting

    train_text = state_union.raw("2005-GWBush.txt")
    filtered_sentence = []
    stemmed_sentence = []

    stop_words = set(stopwords.words('english'))
    word_tokens = word_tokenize(SENT_WISH)

    filtered_sentence = [w for w in word_tokens if not w in stop_words]

    sample_text=SENT_WISH
    custom_sent_tokenizer = PunktSentenceTokenizer(train_text)
    tokenized = custom_sent_tokenizer.tokenize(sample_text)
    for i in tokenized[:5]:
        words = nltk.word_tokenize(i)
        tagged = nltk.pos_tag(words)

    for noun in tagged:
        if noun[1]=="NN" or noun[1]=="NNS" or noun[1]=="VBG" or noun[1]=="NNP":
            wishnltk.append(noun[0])
            
    # print("WISHNLTK", wishnltk)
    return wishnltk

