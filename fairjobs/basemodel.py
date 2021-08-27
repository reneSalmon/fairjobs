from gensim.models import Word2Vec
import data
from vocabulary import masc_vocab, fem_vocab
from extend import final_fem_vocab, final_masc_vocab

class BaseModel(object):

    def __init__(self, df):
        self.df = df

    def word2vec(self):

        self.word2vec_description = Word2Vec(sentences=self.df['clean_description'],
                                             vector_size=50,
                                             min_count=1)
        return self

    def save_model(self):
        return self.word2vec_description.save("../word2vec.model")

    def load_model(self):
        self.word2vec_description = Word2Vec.load("../word2vec.model")
        return self.word2vec_description

    # def masc_similar_words(self, text):
    #     # simil_masc_vocab = []
    #     # match_masc_vocab = []

    #     n_simil_masc = 0
    #     n_match_masc = 0

    #     for word in text:
    #         for masc_word in masc_vocab:
    #             if masc_word in self.word2vec_description.wv.key_to_index:
    #                 if self.word2vec_description.wv.similarity(word, masc_word) > 0.9 and\
    #                 self.word2vec_description.wv.similarity(word, masc_word) < 0.99:
    #                     n_simil_masc += 1
    #                     # simil_masc_vocab.append((word, masc_word))
    #                     # simil_masc_vocab = list(dict.fromkeys(simil_masc_vocab))
    #             if word.find(masc_word) == 0:
    #                 n_match_masc += 1
    #                 # match_masc_vocab.append((word, masc_word))
    #                 # match_masc_vocab = list(dict.fromkeys(match_masc_vocab))

    #     return (n_simil_masc + n_match_masc)

    # def fem_similar_words(self, text):
    #     # simil_fem_vocab = []
    #     # match_fem_vocab = []

    #     n_simil_fem = 0
    #     n_match_fem = 0

    #     for word in text:
    #         for fem_word in fem_vocab:
    #             if fem_word in self.word2vec_description.wv.key_to_index:
    #                 if self.word2vec_description.wv.similarity(word, fem_word) > 0.9 and\
    #                 self.word2vec_description.wv.similarity(word, fem_word) < 0.99:
    #                     n_simil_fem += 1
    #                     # simil_fem_vocab.append((word, fem_word))
    #                     # simil_fem_vocab = list(dict.fromkeys(simil_fem_vocab))
    #             if word.find(fem_word) == 0:
    #                 n_match_fem += 1
    #                 # match_fem_vocab.append((word, fem_word))
    #                 # match_fem_vocab = list(dict.fromkeys(match_fem_vocab))

    #     return (n_simil_fem + n_match_fem)

    def fem_words(self, text):
        n_fem_words = 0
        for word in text:
            if word in final_fem_vocab:
                n_fem_words += 1
        return n_fem_words

    def masc_words(self, text):
        n_masc_words = 0
        for word in text:
            if word in final_masc_vocab:
                n_masc_words += 1
        return n_masc_words

    def masc_fem_words(self):
        self.df['masc_words'] = self.df['clean_description'].apply(self.masc_words)
        self.df['fem_words'] = self.df['clean_description'].apply(self.fem_words)
        self.df['masc_coded'] = self.df['masc_words']/(self.df['masc_words'] +
                                                       self.df['fem_words'] + 0.001)
        self.df['fem_coded'] = self.df['fem_words']/(self.df['masc_words']
                                                     + self.df['fem_words'] + 0.001)
        self.df = self.df.round(2)*100
        # self.df['gender'] = self.df.apply (lambda row: self.label_gender(row), axis=1)
        return self.df

    def label_gender (row):
        if row['fem_words'] > row['masc_words'] :
            return 'feminine'
        elif row['fem_words'] < row['masc_words']:
            return 'masculine'
        else:
            return 'neutral'

    def df_to_csv(self):
        self.df.to_csv('../basemodel_df_22000.csv', encoding='utf-8')

if __name__ == '__main__':
    df = data.get_data()
    df_clean = data.clean_df(df)
    print(df_clean.columns)
    model = BaseModel(df_clean)
    # model.word2vec()
    # model.save_model()
    # model.load_model()
    model.masc_fem_words()
    model.df_to_csv()
    print(model.df)
