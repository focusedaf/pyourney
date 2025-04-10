# create ur tokenizer from scratch for hindi and english
# it should contain class encoder,encode and decode methods

import tiktoken

encoder = tiktoken.encoding_for_model('gpt-4o')

text = 'hello world'
tokens = encoder.encode(text)
print('tokens',tokens)
decoder = encoder.decode(tokens)
print(decoder)
print('vocab size', encoder.n_vocab)