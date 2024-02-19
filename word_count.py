"""Taller evaluable"""

import glob

import pandas as pd

import string

def load_input(input_directory):
    input_files = glob.glob(input_directory + '/*.txt')
    df = pd.concat((pd.read_csv(f, sep='\t', header=None, names=['text']) for f in input_files), ignore_index=True)
    
    return df


def clean_text(dataframe):
    dataframe['clean_text'] = dataframe['text'].apply(lambda x: x.translate(str.maketrans('', '', string.punctuation)).lower())
    
    return dataframe


def count_words(dataframe):
    words = dataframe['clean_text'].str.split(expand=True).stack()
    word_counts = words.value_counts().reset_index()
    word_counts.columns = ['word', 'count']
    
    return word_counts


def save_output(dataframe, output_filename):
    dataframe.to_csv(output_filename, sep='\t', index=False, header=False)


def run(input_directory, output_filename):
    input_df = load_input(input_directory)

    # Clean text
    clean_df = clean_text(input_df)

    # Count words
    word_count_df = count_words(clean_df)

    # Save output
    save_output(word_count_df, output_filename)



if __name__ == "__main__":
    run(
        "input",
        "output.txt",
    )
