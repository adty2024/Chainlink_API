text=[]
textstr=''
for i in range(1):
    with open(f'/content/p2.pdf', 'rb') as f:
        reader = PyPDF2.PdfReader(f)
        pages = [reader.pages[j].extract_text() for j in range(len(reader.pages))]
        text.append(' '.join(pages))
        textstr+=(' '.join(pages))

textstr = textstr.lower()

substring1 = "abs"
substring2 = "introduction"

index = textstr.find(substring1)
if(index == -1):
  index = textstr.find(substring2)

result = textstr[index:index+500]
ind = index+500

while result[-1] != '.':
    result += textstr[ind]
    ind=ind+1

result = re.sub(r'\s+', ' ', result)

from gensim.parsing.preprocessing import remove_stopwords

for i in range(len(text)):
    words = text[i].split()
    words = [remove_stopwords(word) for word in words]
    text.append(' '.join(words))

    lemmatizer = WordNetLemmatizer()

# Define a function to get the WordNet POS tag from the NLTK POS tag
def get_wordnet_pos(nltk_tag):
    if nltk_tag.startswith('J'):
        return wordnet.ADJ
    elif nltk_tag.startswith('V'):
        return wordnet.VERB
    elif nltk_tag.startswith('N'):
        return wordnet.NOUN
    elif nltk_tag.startswith('R'):
        return wordnet.ADV
    else:
        return None

lemmatized = []

# Iterate over each sentence in the text array
for sentence in text:
    # Tokenize the sentence into words
    words = nltk.word_tokenize(sentence)
    # Get the NLTK POS tags for the words
    pos_tags = nltk.pos_tag(words)
    # Map the NLTK POS tags to WordNet POS tags
    wordnet_tags = [(word, get_wordnet_pos(tag)) for word, tag in pos_tags]
    # Lemmatize each word using its WordNet POS tag (if available)
    lemmatized_words = [lemmatizer.lemmatize(word, tag) if tag else word for word, tag in wordnet_tags]
    # Join the lemmatized words back into a sentence
    lemmatized_sentence = ' '.join(lemmatized_words)
    # Add the lemmatized sentence to the lemmatized array
    lemmatized.append(lemmatized_sentence)

texts=[]
for el in lemmatized:
  texts.append(el)

# define the number of topics to extract
num_topics = 70

# define the number of words in each topic
num_words = 70

lda_models = []
for text in texts:
    # tokenize the text and remove stopwords
    tokens = [token for token in simple_preprocess(text) if token not in STOPWORDS]

    # create a dictionary from the tokens
    dictionary = Dictionary([tokens])

    # convert the tokens to a bag-of-words representation
    bow_corpus = [dictionary.doc2bow(tokens)]

    # define the LDA model
    lda_model = LdaModel(bow_corpus, num_topics=num_topics, id2word=dictionary)
    lda_models.append(lda_model)

    topics_dict = {}
for i in range(1):
    topics_dict[i+1] = {}
    for idx, topic in lda_models[i].print_topics(-1, num_words=num_words):
        # extract the words and their weights
        words_weights = topic.split("+")
        # loop over each word and its weight
        for word_weight in words_weights:
            # extract the word and its weight
            word = word_weight.split("*")[1].replace('"', '').strip()
            weight = float(word_weight.split("*")[0])
            # store the word and its weight in the dictionary
            if word in topics_dict[i+1]:
                topics_dict[i+1][word] += weight
            else:
                topics_dict[i+1][word] = weight

sorted_dict = dict(sorted(topics_dict[1].items(), key=lambda x: x[1], reverse=True))

keys = list(sorted_dict.keys())[:5]
{'heat': 2.124999999999998, 'pump': 2.062999999999998, 'model': 2.062999999999998, 'ground': 2.062999999999998, 'element': 2.062999999999998, 'exchanger': 2.042999999999998, 'additional': 2.0219999999999976, 'unsteady': 2.0219999999999976, 'tube': 2.0219999999999976, 'space': 2.0219999999999976, 'source': 2.0219999999999976, 'shortly': 2.0219999999999976, 'second': 2.0219999999999976, 'process': 2.0219999999999976, 'present': 2.0219999999999976, 'place': 2.0219999999999976, 'investigate': 2.0219999999999976, 'general': 2.0219999999999976, 'form': 2.0219999999999976, 'adjoin': 2.0219999999999976, 'analyzed': 2.0219999999999976, 'apart': 2.0219999999999976, 'area': 2.0219999999999976, 'calculation': 2.0219999999999976, 'character': 2.0219999999999976, 'vapour': 2.0219999999999976, 'compressor': 2.0219999999999976, 'consist': 2.0219999999999976, 'contain': 2.0219999999999976, 'conventional': 2.0219999999999976, 'equation': 2.0219999999999976, 'equip': 2.0219999999999976, 'compressorheat': 2.0219999999999976, 'vertical': 2.0219999999999976}


# Append the keys to the string, separated by commas
result+=("The research paper highlights the significance of the following words: ")
appended_string = result + ", ".join(keys)

from gtts import gTTS
import os
import pyttsx3

# Set the output file path
output_path = "/content/e5.mp3"

tts = gTTS(text=appended_string, lang='en')
tts.save(output_path)

engine = pyttsx3.init()

engine.setProperty('rate', 150)

# Set the speech volume (0.0 to 1.0)
engine.setProperty('volume', 1.0)

# Play the audio file using pyttsx3
engine.say(appended_string)
engine.runAndWait()

from googletrans import Translator

def generate_audio(text, target_language):
    translator = Translator()
    translation = translator.translate(text, dest=target_language)
    tts = gTTS(text=translation.text, lang=target_language)
    tts.save("h2.mp3")  # Save the audio to a file named "output.mp3"

# Example usage
text = appended_string
target_language = "hi"  # Language code for Hindi

generate_audio(text, target_language)