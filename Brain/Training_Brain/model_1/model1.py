import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from jarvis_speak.speak import speak

def load_dataset(file_path):
    with open(file_path, 'r' ,encoding='utf-8') as file:
        lines = file.readlines()
        qna_pairs = [line.strip().split(':') for line in lines if ':' in line]
        dataset = [{'question':q , 'answer':a} for q,a in qna_pairs]
    return dataset

def preprocess_text(query):
    stop_words = set(stopwords.words('english'))
    ps = PorterStemmer()
    tokens = word_tokenize(query.lower())
    tokens = [ps.stem(token) for token in tokens if token.isalnum() and token not in stop_words]
    return ' '.join(tokens)

def train_tfidf_vectorizer(dataset):
    corpus = [preprocess_text(qa['question']) for qa in dataset]
    vectorizer = TfidfVectorizer()
    x = vectorizer.fit_transform(corpus)
    return vectorizer,x

def get_answer(question,vectorizer,x,dataset):
    question = preprocess_text(question)
    question_vector = vectorizer.transform([question])
    similarity_scores = cosine_similarity(question_vector, x)
    best_match_index = similarity_scores.argmax()
    return dataset[best_match_index]['answer']

def mind(query):
    dataset_path = r'/home/hacksmith010/Programming/Personal/Jarvis/data/qna.txt'
    dataset = load_dataset(dataset_path)
    vectorizer,x = train_tfidf_vectorizer(dataset)
    user_question = query
    answer = get_answer(user_question,vectorizer,x,dataset)
    speak(answer)
    
mind("hello")