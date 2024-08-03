# install_nltk_data.py

import nltk

def download_nltk_data():
    nltk.download('punkt')
    nltk.download('averaged_perceptron_tagger')

if __name__ == "__main__":
    download_nltk_data()
