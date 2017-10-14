import string

def next_bin_number(n):
    bin_list = list(n)
    for i in range(len(bin_list) - 1, -1, -1):
        if bin_list[i] == "0":
            bin_list[i] = "1"
            break
        else:
            bin_list[i] = "0"
    return ''.join(bin_list)

def G2F_add(a, b):
    if a == '1' and b == '1':
        return '0'
    if a == '0' and b == '0':
        return '0'
    return '1'

def decrypt(encoded_string, key, bin2char):
    decrypted_string = ""
    for i in range(0,55):
        decrypted_string += G2F_add(encoded_string[i], key[i%5])
    readable = ""
    for i in range(0,55,5):
        if decrypted_string[i:i+5] in bin2char:
            readable += bin2char[decrypted_string[i:i+5]]
        else:
            return
    if 'e' in readable and ' ' in readable: #reduce the possibilities by assuming an e and space
        print(readable)


letters  = list(string.ascii_lowercase)
letters.append(' ')
encoded_string = "1010100100101010101111001000110101110101001001100111010"
key = "00000"

char2bin = {}
start = "00000"
for char in letters:
    char2bin[char] = start
    start = next_bin_number(start)

bin2char = {v: k for k, v in char2bin.items()}

decrypt(encoded_string, key, bin2char)
while key != "11111":
    key = next_bin_number(key)
    decrypt(encoded_string, key, bin2char)

