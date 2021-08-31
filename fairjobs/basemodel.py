import data
import pickle
import ast

class BaseModel(object):

    def __init__(self, df):
        self.df = df

    def fem_words(self, text):
        fh = open("../vocab_fem.pkl", 'rb')
        final_fem_vocab = pickle.load(fh)
        fh.close()

        self.fem_words_list = []

        n_fem_words = 0
        for word in text:
            if word in final_fem_vocab:
                self.fem_words_list.append(word)
                n_fem_words += 1
        self.fem_words_list = [n.strip() for n in self.fem_words_list]
        return self.fem_words_list

    def masc_words(self, text):
        fh = open("../vocab_masc.pkl", 'rb')
        final_masc_vocab = pickle.load(fh)
        fh.close()

        self.masc_words_list = []

        n_masc_words = 0
        for word in text:
            if word in final_masc_vocab:
                self.masc_words_list.append(word)
                n_masc_words += 1

        return self.masc_words_list

    def label_gender(self, row):
        if row['fem_coded'] > 52 :
            return 'feminine'
        elif row['fem_coded'] < 48:
            return 'masculine'
        else:
            return 'neutral'

    def text_for_annotation(self, text):

        self.neut_words_list = []
        self.List_for_annotation = []
        for word in text.split():
            if word in self.df['fem_words_list']:
                if word in self.df['masc_words_list']:
                    self.List_for_annotation.append((word + ' ', "neutral", "#fea"))
                self.List_for_annotation.append((word + ' ', "female", "#faa"))
            elif word in self.df['masc_words_list']:
                self.List_for_annotation.append((word + ' ', "male", "#8ef"))
            else:
                self.List_for_annotation.append(word + ' ')
        return self.List_for_annotation

    def masc_fem_words(self):
        self.df['masc_words_list'] = self.df['clean_description'].apply(self.masc_words)
        self.df['fem_words_list'] = self.df['clean_description'].apply(self.fem_words)
        self.df['masc_words'] = self.df['masc_words_list'].apply(len)
        self.df['fem_words'] = self.df['fem_words_list'].apply(len)

        self.df['list_for_annotation'] = self.df['job_description'].apply(self.text_for_annotation)

        self.df['masc_coded'] = self.df['masc_words']/(self.df['masc_words'] +
                                                       self.df['fem_words'] + 0.001)
        self.df['fem_coded'] = self.df['fem_words']/(self.df['masc_words']
                                                     + self.df['fem_words'] + 0.001)

        self.df.masc_coded = self.df.masc_coded.round(2)*100
        self.df.fem_coded = self.df.fem_coded.round(2)*100
        self.df['gender'] = self.df.apply(lambda row: self.label_gender(row), axis=1)
        return self.df

    def df_to_csv(self):
        self.df.to_csv('../raw_data/data_2021-31-08-cleaned_newds_gd.csv', encoding='utf-8')

if __name__ == '__main__':
    df = data.get_data()
    df_clean = data.clean_df(df)
    print(df_clean.columns)
    model = BaseModel(df_clean)
    model.masc_fem_words()
    model.df_to_csv()
    print(model.df)
