# app.py
import gradio as gr
from marathi_tokenizer import load_tokenizer

# Load the trained tokenizer
tokenizer_path = "marathi_bpe_tokenizer.json"
tokenizer = load_tokenizer(tokenizer_path)

# Define the Gradio interface function
def tokenize_text(text):
    encoding = tokenizer.encode(text)
    tokens = encoding.tokens
    ids = encoding.ids

    # Build a table-like HTML output for better visualization
    formatted_output = "<table style='width: 100%; border-collapse: collapse;'>"
    formatted_output += "<tr><th style='border: 1px solid #ddd; padding: 8px; background-color: #f2f2f2;'>Token</th><th style='border: 1px solid #ddd; padding: 8px; background-color: #f2f2f2;'>ID</th></tr>"

    for token, token_id in zip(tokens, ids):
        formatted_output += f"<tr><td style='border: 1px solid #ddd; padding: 8px;'>{token}</td><td style='border: 1px solid #ddd; padding: 8px; text-align: center;'>{token_id}</td></tr>"

    formatted_output += "</table>"
    return formatted_output

# Create the Gradio app
iface = gr.Interface(
    fn=tokenize_text,
    inputs=gr.Textbox(lines=5, placeholder="Enter Marathi text here..."),
    outputs=gr.HTML(),
    title="Marathi BPE Tokenizer",
    description="A Byte Pair Encoding (BPE) tokenizer for Marathi with a vocabulary of less than 5,000 tokens. The output includes both tokens and their corresponding IDs in a table format for clarity."
)

# Launch the Gradio app
if __name__ == "__main__":
    iface.launch()