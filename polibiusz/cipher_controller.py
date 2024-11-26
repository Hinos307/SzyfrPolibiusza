# cipher_controller.py

from polybius_cipher import PolybiusCipher

class CipherController:
    def __init__(self):
        self.cipher = PolybiusCipher()

    def encrypt_text(self, text, a, b, table_index):
        return self.cipher.encrypt(text, a, b, table_index)

    def decrypt_text(self, y, a, b, table_index):
        return self.cipher.decrypt(y, a, b, table_index)
