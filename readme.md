# Marathi BPE Tokenizer

## Project Overview
The **Marathi BPE Tokenizer** is a custom-built tokenizer for the Marathi language using Byte Pair Encoding (BPE). The project includes a tokenizer training script (`marathi_tokenizer.py`) and a user-friendly web interface built with Gradio (`app.py`). The interface allows users to input Marathi text and see the tokenized output, as well as encoded IDs.

---

## Features
- Downloads and cleans a Marathi text corpus
- Trains a Byte Pair Encoding (BPE) tokenizer with a vocabulary size of 5,000 tokens
- Saves the tokenizer in a JSON format
- Provides a Gradio-based web interface to test the tokenizer
- Calculates the compression ratio of the tokenizer

---

## File Structure
```
.
├── marathi_tokenizer.py  # Script to download, clean, and train the tokenizer
├── app.py                # Gradio app for interacting with the tokenizer
├── marathi_bpe_tokenizer.json  # Trained tokenizer model (generated after training)
├── requirements.txt      # Dependencies
└── README.md             # Project documentation
```

---

## Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd marathi-tokenizer
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## How to Use

### 1. Training the Tokenizer
Run the `marathi_tokenizer.py` script to download the dataset, clean it, train the tokenizer, and save the trained model.
```bash
python marathi_tokenizer.py
```
The trained tokenizer will be saved as `marathi_bpe_tokenizer.json`.

### 2. Launching the Gradio App
Once the tokenizer is trained, run the Gradio app to use the web interface.
```bash
python app.py
```
The app will launch in your default web browser. You can enter Marathi text to see the tokenized output and encoded IDs.

---

## Sample Logs

```

(venv) narendra.kalekar@MAC-KJF4T0J3JR marathi-tokenizer-bpe % python3 marathi_tokenizer.py
Dataset already exists at mr.txt.
Corpus cleaned and saved to cleaned_mr.txt.
Loading corpus from cleaned_mr.txt...
Training the BPE tokenizer...
[00:01:28] Pre-processing sequences       ████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████ 0        /        0[00:00:06] Tokenize words                 ████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████ 8382991  /  8382991
[00:00:54] Count pairs                    ████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████ 8382991  /  8382991
[00:00:20] Compute merges                 ████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████ 4813     /     4813
Tokenizer saved to marathi_bpe_tokenizer.json.
--------------------------------------------------
Input Text   : महाराष्ट्र हे भारताच्या पश्चिम भागातील एक राज्य आहे.
Encoded Ids  : [708, 193, 2766, 2449, 2928, 303, 627, 199]
Tokens       : ['महाराष्ट्र', 'हे', 'भारताच्या', 'पश्चिम', 'भागातील', 'एक', 'राज्य', 'आहे']
--------------------------------------------------
--------------------------------------------------
Input Text   : माझे नाव नरेंद्र कालेकर आहे.
Encoded Ids  : [2913, 701, 1631, 194, 198, 203, 199]
Tokens       : ['माझे', 'नाव', 'नरेंद्र', 'का', 'ले', 'कर', 'आहे']
--------------------------------------------------
--------------------------------------------------
Input Text   : मुख्यमंत्री देवेंद्र फडणवीसांचा राज्यातील सर्व प्रशासकीय अधिकाऱ्यांसाठी सात कलमी कृती कार्यक्रम.
Encoded Ids  : [860, 2151, 1563, 279, 202, 342, 1325, 406, 217, 2312, 1731, 722, 710, 1057, 277, 1496, 2381]
Tokens       : ['मुख्यमंत्री', 'देवेंद्र', 'फडण', 'वी', 'सा', 'ंचा', 'राज्यातील', 'सर्व', 'प्र', 'शासकीय', 'अधिकाऱ्या', 'ंसाठी', 'सात', 'कल', 'मी', 'कृती', 'कार्यक्रम']
--------------------------------------------------
--------------------------------------------------
Input Text   : स्टीव्ह जॉब्स यांच्या पत्नी महाकुंभात सहभागी होणार; संन्यासी आयुष्य जगणार.
Encoded Ids  : [206, 313, 484, 3104, 497, 123, 403, 1783, 421, 365, 2604, 196, 2253, 647, 236, 405, 351, 3606, 755, 275]
Tokens       : ['स्', 'टी', 'व्ह', 'जॉ', 'ब्', 'स', 'यांच्या', 'पत्नी', 'महा', 'कु', 'ंभ', 'ात', 'सहभागी', 'होणार', 'सं', 'न्या', 'सी', 'आयुष्य', 'जग', 'णार']
--------------------------------------------------
Compression Ratio: 4.06
(venv) narendra.kalekar@MAC-KJF4T0J3JR marathi-tokenizer-bpe % 

```


---

## Compression Ratio
The script also calculates the compression ratio to evaluate the efficiency of the tokenizer.
```bash
Compression Ratio: 4.06
```
This indicates that the original text size is 4.06 times larger than the tokenized version.

---

## Future Enhancements
- Support for additional Marathi datasets
- Customizable vocabulary size
- Enhanced text normalization for better tokenization

---

## Contributing
Contributions are welcome! Feel free to submit a pull request or open an issue to suggest improvements.

---

## License
This project is licensed under the MIT License.

---

## Acknowledgments
- Inspired by the [Hugging Face Tokenizers](https://huggingface.co/docs/tokenizers/) library.
- Marathi text corpus provided by [AI4Bharat](https://ai4bharat.org/).
