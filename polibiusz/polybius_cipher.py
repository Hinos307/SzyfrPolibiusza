# polybius_cipher.py

import math

class PolybiusCipher:
    def __init__(self):
        self.polybius_tables = [

            [
                ['B', 'Q', 'Y', 'a', 'Ć', 'E', 'Z', 'Ó', 'V'],
                ['ą', ' ', 'J', 'I', 'Ł', 'G', 'P', 'M', 'Ś'],
                ['Ź', 'X', 'd', 'T', 'F', 'H', 'Ż', 'f', 'A'],
                ['D', 'N', 'O', 'W', 'K', 'S', 'ę', 'Ć', 'R'],
                ['L', 'U', 'C', 'Ń', 'e', 'Ę', 'o', 'V', 'b']

            ],
            [['d', 'Ą', 'ę', 'E', 'P', 'S', 'B', 'V', 'F'],
             ['I', 'L', 'Q', 'J', 'M', 'T', 'Ń', 'Ź', 'b'],
             ['O', 'o', 'N', 'Ż', 'U', 'y', ' ', 'X', 'c'],
             ['R', 'f', 'Ł', 'Ź', 'ę', 'W', 'Ć', 'ą', 'H'],
             ['D', 'Ś', 'G', 'a', 'Ą', 'ż', 'Y', 'Z', 'O']],

            [['Ż', 'Q', 'Y', 'B', 'O', 'Ę', 'o', 'F', 'd'],
             ['Ć', 'G', 'V', 'K', 'ę', 'L', 'b', 'P', 'Ś'],
             ['Ź', 'c', 'J', 'T', 'R', 'Ń', 'O', 'a', 'N'],
             ['Z', 'f', 'C', 'U', 'W', 'S', 'D', ' ', 'L'],
             ['M', 'Ą', 'I', 'A', 'ć', 'X', 'ą', 'Y', 'Ę']],

            [['M', 'L', 'a', 'Y', 'F', 'ę', 'A', 'P', 'Ż'],
             ['G', 'N', 'K', 'Ź', 'ć', 'U', ' ', 'D', 'V'],
             ['Ę', 'o', 'Ś', 'J', 'T', 'L', 'y', 'Ż', 'B'],
             ['I', 'H', 'b', 'C', 'D', 'ą', 'f', 'S', 'X'],
             ['Q', 'Z', 'O', 'R', 'O', 'Ń', 'Ć', 'Ź', 'E']],

            [['T', 'V', 'C', 'ą', 'E', 'Ż', 'Ę', 'd', 'B'],
             ['Ź', 'F', 'J', 'G', 'a', 'o', 'K', 'L', 'I'],
             [' ', 'Ł', 'Q', 'Ć', 'Y', 'X', 'R', 'Ś', 'D'],
             ['N', 'P', 'f', 'U', 'Ż', 'b', 'Ń', 'S', 'O'],
             ['Ą', 'Ą', 'H', 'A', 'Ź', 'W', 'ć', 'Z', 'e']],

            [['L', 'Ź', 'E', 'Y', 'D', 'T', 'Ą', 'ę', 'X'],
             ['F', 'Ż', 'C', 'V', 'B', 'a', 'P', 'Ś', 'H'],
             ['A', 'o', 'G', 'Ł', ' ', 'Ź', 'Z', 'S', 'Ć'],
             ['Ę', 'N', 'Q', 'R', 'N', 'J', 'M', 'O', 'ą'],
             ['I', 'U', 'b', 'O', 'Ń', 'f', 'K', 'ć', 'd']],

            [['Ź', 'E', 'Z', 'B', 'Y', 'P', 'ą', 'A', 'F'],
             ['V', 'o', 'L', 'G', 'ć', 'S', 'ę', 'T', 'I'],
             ['Ź', ' ', 'a', 'Q', 'Ć', 'Ż', 'M', 'D', 'J'],
             ['K', 'X', 'R', 'd', 'f', 'U', 'b', 'H', 'W'],
             ['O', 'Ń', 'L', 'Ż', 'Ę', 'Ą', 'N', 'c', 'Ś']],

            [['Ż', 'T', 'Ź', 'N', 'C', 'J', 'R', 'd', 'Ą'],
             ['ą', 'Z', 'E', 'V', ' ', 'G', 'o', 'Q', 'P'],
             ['Ś', 'Ć', 'a', 'H', 'U', 'M', 'D', 'Ę', 'f'],
             ['W', 'b', 'I', 'Y', 'A', 'Ź', 'Ł', 'O', 'L'],
             ['Ź', 'ę', 'K', 'S', 'X', 'ć', 'Ó', 'O', 'F']],

            [['P', 'M', 'Ż', 'Ź', 'D', 'ę', 'ą', 'N', 'H'],
             ['o', 'A', 'Ę', 'F', 'V', 'Ź', 'b', 'Y', 'Q'],
             ['C', 'Ź', 'S', 'G', 'Ć', 'R', 'I', 'U', 'X'],
             ['L', 'B', 'd', 'Q', 'f', 'Z', 'T', ' ', 'O'],
             ['Ń', 'ą', 'W', 'E', 'Ć', 'K', 'Y', 'J', 'L']],

            [['Y', 'L', 'a', 'Ę', 'Ć', 'D', 'Ź', 'O', 'G'],
             ['o', 'T', 'A', 'F', 'P', 'B', 'V', 'Ą', 'Z'],
             ['Q', 'S', 'L', 'Ź', 'K', 'ę', 'f', 'X', 'W'],
             ['I', 'J', 'N', 'b', 'Ó', ' ', 'R', 'Ź', 'M'],
             ['d', 'U', 'Ś', 'G', 'C', 'ą', 'H', 'Ć', 'O']],
        ]

    def encrypt(self, text, a, b, table_index):
        text = ''.join(text.split()).upper()
        table = self.polybius_tables[table_index]

        pairs = []
        for char in text:
            for i, row in enumerate(table):
                if char in row:
                    j = row.index(char)
                    pairs.append((i + 1, j + 1))
                    break

        x = int(''.join(f"{i}{j}" for i, j in pairs))
        y = a * (x ** 2) + b
        return y

    def decrypt(self, y, a, b, table_index):
        if a == 0:
            return None

        x = math.isqrt((y - b) // a)
        pairs = [(int(str(x)[i]), int(str(x)[i + 1])) for i in range(0, len(str(x)), 2)]

        decrypted_text = ''
        table = self.polybius_tables[table_index]
        for i, j in pairs:
            if 1 <= i <= 5 and 1 <= j <= 9:
                decrypted_text += table[i - 1][j - 1]

        return decrypted_text
