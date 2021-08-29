class Encrypt:
    """
    Encrypt a simple text

    === Private Attributes ===
    _p_text: Lower case alphabet in a tuple
    _key: Upper case alphabet in a tuple


    """
    _text: str
    _key: str

    def __init__(self, text: str, key: str):
        self._text = text
        self._key = key

    def encryption(self) -> str:
        l_alphabet = (
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
            'y', 'z')
        length_text = 0
        final_key = ''
        cypher = ''

        pos = 0
        word_loop = 0
        while length_text < len(self._text):
            if not self._text[length_text].isalpha():
                final_key = final_key + self._text[length_text]
            else:
                if (word_loop % len(self._key)) == 0:
                    pos = 0
                final_key = final_key + self._key[pos]
                word_loop += 1
                pos += 1

            length_text += 1

        i = 0
        upper = False
        while i < len(self._text):
            if not self._text[i].isalpha():
                cypher = cypher + self._text[i]
            else:
                if self._text[i].isupper():
                    upper = True
                    self._text = (self._text[:i] + self._text[i].lower()
                                  + self._text[i + 1:])
                cypher_pos = (l_alphabet.index(self._text[i])
                              + l_alphabet.index(final_key[i]))
                if cypher_pos > 25:
                    cypher_pos -= 26

                if upper:
                    cypher = cypher + l_alphabet[cypher_pos].upper()
                    upper = False
                else:
                    cypher = cypher + l_alphabet[cypher_pos]
            i += 1

        return cypher
