import re

def hindi_tokenizer(text):
    patterns = {
        "url": r"https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+",
        "email": r"[\w\.-]+@[\w\.-]+\.[a-zA-Z]{2,6}",
        "date": r"\d{1,2}[-/.]\d{1,2}[-/.]\d{2,4}",
        "number": r"\d{1,3}(?:,\d{2,3})*(?:\.\d+)?|\d+/\d+|[\u0966-\u096F]+",
        "username": r"@[\w_]+",
        "punctuation": r"[.,!?;:\"'()\[\]{}]",
        "hindi_word": r"[\u0900-\u097F]+"
    }
    
    combined_pattern = "|".join(f"(?P<{key}>{pattern})" for key, pattern in patterns.items())
    
    tokens = []
    for match in re.finditer(combined_pattern, text):
        for key, value in match.groupdict().items():
            if value:
                tokens.append((key, value))
    
    return tokens

text = "मेरा नाम धीरज है और मैं एआई स्टूडेंट हूं https://www.google.com"
tokens = hindi_tokenizer(text)
print(tokens)