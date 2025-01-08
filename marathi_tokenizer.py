# marathi_tokenizer.py
import requests
import os
from tokenizers import Tokenizer, models, trainers, pre_tokenizers
import random
import re


def download_corpus(url, save_path="mr.txt"):
    """
    Downloads a text corpus from the given URL and saves it to the specified path.
    """
    if not os.path.exists(save_path):
        response = requests.get(url)
        if response.status_code == 200:
            with open(save_path, "wb") as f:
                f.write(response.content)
            print(f"Dataset downloaded successfully to {save_path}!")
        else:
            raise Exception("Failed to download the dataset.")
    else:
        print(f"Dataset already exists at {save_path}.")
    return save_path


def clean_chunk(corpus):
    """
    Cleans the corpus by removing unwanted characters, extra spaces, and normalizing text.
    """
    # Remove non-alphanumeric characters except spaces (optional, depending on the corpus)
    corpus = re.sub(r'[^a-zA-Z0-9\u0900-\u097F\s]', '', corpus)  # Marathi Unicode range included
    
    # Remove extra spaces
    corpus = re.sub(r'\s+', ' ', corpus).strip()
    
    return corpus


def load_corpus(file_path,chunk_size=100000):
    """
    Loads the text corpus from the specified file path.
    """
    print(f"Loading corpus from {file_path}...")
    corpus = ""
    with open(file_path, "r", encoding="utf-8") as f:
        while True:
            chunk = f.read(chunk_size)
            #chunk = clean_chunk(chunk)
            if not chunk:
                break
            corpus += chunk
    return corpus


def clean_corpus_incremental(input_path, output_path):
    """
    Cleans the corpus line by line to avoid memory overload.
    """
    with open(input_path, "r", encoding="utf-8") as infile, open(output_path, "w", encoding="utf-8") as outfile:
        for line in infile:
            # Remove non-alphanumeric characters (except spaces) and normalize spaces
            cleaned_line = re.sub(r'[^a-zA-Z0-9\u0900-\u097F\s]', '', line)  # Marathi Unicode range included
            cleaned_line = re.sub(r'\s+', ' ', cleaned_line).strip()
            outfile.write(cleaned_line + "\n")
    print(f"Corpus cleaned and saved to {output_path}.")


def train_bpe_tokenizer(corpus, vocab_size=5000, save_path="marathi_bpe_tokenizer.json"):
    """
    Trains a BPE tokenizer on the given corpus and saves the tokenizer to a file.
    """
    print("Training the BPE tokenizer...")
    # Initialize a BPE tokenizer
    tokenizer = Tokenizer(models.BPE())

    # Use whitespace to split words
    tokenizer.pre_tokenizer = pre_tokenizers.Whitespace()

    # Define the trainer with a specified vocabulary size
    trainer = trainers.BpeTrainer(vocab_size=vocab_size, special_tokens=["<pad>", "<s>", "</s>", "<unk>", "<mask>"])

    # Train the tokenizer
    tokenizer.train_from_iterator(corpus.split("\n"), trainer=trainer)

    # Save the tokenizer
    tokenizer.save(save_path)
    print(f"Tokenizer saved to {save_path}.")
    return tokenizer


def load_tokenizer(tokenizer_path):
    """
    Loads the trained tokenizer from the specified file path.
    """
    tokenizer = Tokenizer.from_file(tokenizer_path)
    print(f"Tokenizer loaded from {tokenizer_path}.")
    return tokenizer


def test_tokenizer(tokenizer, text):
    """
    Tests the tokenizer by encoding a given text and returning the tokens.
    """
    encoding = tokenizer.encode(text)
    print("-" * 50)
    print("Input Text   :", text)
    print("Encoded Ids  :", encoding.ids)
    print("Tokens       :", encoding.tokens)
    print("-" * 50)
    return  encoding.tokens


def calculate_compression_ratio(tokenizer, texts):
    lines = texts.split("\n")
    lines = random.sample(lines, min(10000000, len(lines)))
    original_size = sum(len(text) for text in lines)
    compressed_size = sum(len(tokenizer.encode(text).tokens) for text in lines)
    return original_size / compressed_size


def main():
    # Step 1: Download the dataset
    dataset_url = "https://objectstore.e2enetworks.net/ai4b-public-nlu-nlg/indic-corp-frozen-for-the-paper-oct-2022/mr.txt"
    corpus_path = download_corpus(dataset_url)

    # Step 2: Clean the corpus incrementally
    cleaned_corpus_path = "cleaned_mr.txt"
    clean_corpus_incremental(corpus_path, cleaned_corpus_path)

    # Step 3: Load the corpus
    corpus = load_corpus(cleaned_corpus_path)

    # Step 4: Train the tokenizer
    tokenizer = train_bpe_tokenizer(corpus)

    # Step 5: Test the tokenizer
    test_tokenizer(tokenizer, "महाराष्ट्र हे भारताच्या पश्चिम भागातील एक राज्य आहे.")
    test_tokenizer(tokenizer, "माझे नाव नरेंद्र कालेकर आहे.")
    test_tokenizer(tokenizer, "मुख्यमंत्री देवेंद्र फडणवीसांचा राज्यातील सर्व प्रशासकीय अधिकाऱ्यांसाठी सात कलमी कृती कार्यक्रम.")
    test_tokenizer(tokenizer, "स्टीव्ह जॉब्स यांच्या पत्नी महाकुंभात सहभागी होणार; संन्यासी आयुष्य जगणार.")

    # Step 6: Calculate the compression ratio
    compression_ratio = calculate_compression_ratio(tokenizer, corpus)
    print(f"Compression Ratio: {compression_ratio:.2f}")

if __name__ == "__main__":
    main()