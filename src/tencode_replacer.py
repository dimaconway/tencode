import json
import pprint

_tencodes_dictionary = json.loads(open('tencodes.json').read())

_lines_delimiter = '\n'
_words_delimiter = ' '


def replace_tencode_in_message(message: str) -> str:
    modified_message = []

    lines = message.split(_lines_delimiter)

    for line in lines:
        words = line.split(_words_delimiter)

        modified_line = []

        for word in words:
            if word == '':
                modified_word = _words_delimiter
            else:
                modified_word = _get_tencode_meaning(word)

            modified_line.append(modified_word)

        modified_message.append(_words_delimiter.join(modified_line))

    return _lines_delimiter.join(modified_message)


def _get_tencode_meaning(word: str) -> str:
    meaning = _tencodes_dictionary.get(word)
    return '[' + meaning + ']' if meaning else word


if __name__ == '__main__':
    pprint.pprint(replace_tencode_in_message(
        '''Произвольный текст     сообщения где есть 

10-13

    10-77    


        10-3

        тенкод например 10-4 или 10-13'''
    ))