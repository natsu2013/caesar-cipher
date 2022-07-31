import argparse
from argparse import HelpFormatter
import os


def encrypt(plaintext, shift):
    cipher = bytearray(plaintext.encode('utf-8'))
    for i, c in enumerate(cipher):
        cipher[i] = (c + shift) & 0xff
    return cipher

def decrypt(ciphertext, shift):
    plain = bytearray(len(ciphertext))    
    for i, c in enumerate(ciphertext):
        plain[i] = (c - shift) & 0xff
    return plain.decode('utf-8')

FUNCTION_MAP = { 'e': encrypt, 'd': decrypt }

class MyFormatter(HelpFormatter):
    """
        for matt wilkie on SO
    """
    def _format_action_invocation(self, action):
        if not action.option_strings:
            default = self._get_default_metavar_for_positional(action)
            metavar, = self._metavar_formatter(action, default)(1)
            return metavar

        else:
            parts = []

            # if the Optional doesn't take a value, format is:
            #    -s, --long
            if action.nargs == 0:
                parts.extend(action.option_strings)

            # if the Optional takes a value, format is:
            #    -s ARGS, --long ARGS
            else:
                default = self._get_default_metavar_for_optional(action)
                args_string = self._format_args(action, default)
                for option_string in action.option_strings:
                    parts.append(option_string)

                return '%s %s' % (', '.join(parts), args_string)

            return ', '.join(parts)

    def _get_default_metavar_for_optional(self, action):
        return action.dest.upper()

def parser_argument():
    parser = argparse.ArgumentParser(prog='Caeser Cipher',  usage='%(prog)s [options] ...' ,description='Caeser cipher by N@T54', epilog='Enjoy the moment! :)', formatter_class=MyFormatter)

    parser.add_argument('-k', '--key', metavar='', help='key use for encrypt & decrypt')
    parser.add_argument('-p', '--plaintext', metavar='', help='the plaintext')
    parser.add_argument('-c', '--ciphertext', metavar='', help='the ciphertext')
    parser.add_argument('-e', '--encrypt', help='encrypt the plaintext', action='store_true')
    parser.add_argument('-d', '--decrypt', help='decrypt the ciphertext', action='store_true')
    args = parser.parse_args()
    return args

if __name__ == '__main__':
    args = parser_argument()
    file = './caesar_enc.txt'
    key = int(args.key)
    result = ''
    if args.plaintext is not None and args.encrypt:
        result = encrypt(args.plaintext, key).decode()
    if args.ciphertext is not None and args.decrypt:
        result = decrypt(args.ciphertext, key)

    if os.path.exists(file):
        with open('caesar_enc.txt', 'w') as f:
            f.write(result)
            print(f'[\033[36m!\033[0m] - Save to {file}')
    else:
        print(f'\033[32m[!\033[0m] - Can\'t write to file {file}')
# caesar cipher implement with python 
# Algorithm:
# C = E(p, k) = (p + k) mod 26
# p = D(C, k) = (C - k) mod 26

# if ord(char) > 96 :
#     result += chr((ord(char) + key - 97) % 26 + 97)
# else:
#     result += chr((ord(char)+ key - 65) % 26 +65)