from encrypt import Encrypt
from decrypyt import Decrypt


class Encodify:

    def __init__(self, file: str):
        self.file = file

    def encrypt(self, key: str) -> None:
        r = open(self.file, 'r')
        text = []
        for line in r:
            line = line.strip()
            enc = Encrypt(line, key)
            text.append(enc.encryption())
        r.close()

        w = open('encrypted ' + self.file, 'w')
        for line in text:
            w.write(line + '\n')
        w.close()

    def decrypt(self, key: str):
        r = open(self.file, 'r')
        text = []
        for line in r:
            line = line.strip()
            de = Decrypt(line, key)
            text.append(de.decryption())
        r.close()

        w = open('decrypted ' + self.file, 'w')
        for line in text:
            w.write(line + '\n')
        w.close()


# ENCRYPTYING ONE LINE AT A TIME IS DIF FROM ENCRYPTING THE ENTIRE TEXT



