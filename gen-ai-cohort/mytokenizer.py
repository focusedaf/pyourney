class Encoder:
    def __init__(self):
        chars = list("abcdefghijklmnopqrstuvwxyz0123456789 .,!?")
        chars.append("[UNK]")
        
        self.token_to_id= {char: idx for idx, char in enumerate(chars)}
        self.id_to_token = {idx: char for char, idx in self.token_to_id.items()}
    
    def encode(self, text):
        text = text.lower()  
        token_ids = []

        for char in text:
            if char in self.token_to_id:
                token_ids.append(self.token_to_id[char])
            else:
                token_ids.append(self.token_to_id["[UNK]"])

        return token_ids

       

    def decode(self, token_ids):
        chars = []

        for token_id in token_ids:
            if token_id in self.id_to_token:
                chars.append(self.id_to_token[token_id])
            else:
                chars.append("[UNK]")

        return "".join(chars)

       



tokenizer = Encoder()

encoded = tokenizer.encode("hello world!")
print("Encoded:", encoded)

decoded = tokenizer.decode(encoded)
print("Decoded:", decoded)

