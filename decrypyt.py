class Decrypt:
    """
    Encrypt a simple text

    === Private Attributes ===
    _p_text: Lower case alphabet in a tuple
    _key: Upper case alphabet in a tuple


    """
    _cypher: str
    _key: str

    def __init__(self, cypher: str, key: str):
        self._cypher = cypher
        self._key = key

    def decryption(self) -> str:
        l_alphabet = (
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
            'y', 'z')
        length_text = 0
        final_key = ''
        text = ''

        pos = 0
        word_loop = 0
        while length_text < len(self._cypher):
            if not self._cypher[length_text].isalpha():
                final_key = final_key + self._cypher[length_text]
            else:
                if (word_loop % len(self._key)) == 0:
                    pos = 0
                final_key = final_key + self._key[pos]
                word_loop += 1
                pos += 1

            length_text += 1

        i = 0
        upper = False
        while i < len(self._cypher):
            if not self._cypher[i].isalpha():
                text = text + self._cypher[i]

            else:
                if self._cypher[i].isupper():
                    upper = True
                    self._cypher = (self._cypher[:i] + self._cypher[i].lower()
                                    + self._cypher[i + 1:])
                cypher_pos = (l_alphabet.index(self._cypher[i])
                              - l_alphabet.index(final_key[i]))
                if cypher_pos > 25:
                    cypher_pos -= 26

                if upper:
                    text = text + l_alphabet[cypher_pos].upper()
                    upper = False
                else:
                    text = text + l_alphabet[cypher_pos]
            i += 1

        return text
