class Tokenizer:
    def __init__(self, vocab):
        self.vocab = vocab
        self.unknown = "UNK"

    def tokenize(self, text):
        tokens = []
        i = 0
        while i < len(text):
            matched = None
            for token in self.vocab:
                if text.startswith(token, i):
                    matched = token
                    break
            if matched is None:
                tokens.append(self.unknown)
                i += 1
            else:
                tokens.append(matched)
                i += len(matched)
        return tokens

    def detokenize(self, tokens):
        return "".join(tokens).replace(self.unknown, "")

