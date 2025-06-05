from collections import defaultdict
import os
import re
import csv

UTF = 'utf-8'
PATH = os.path.dirname(os.path.realpath(__file__))
MIN_WORD_FREQ_LIMIT = 5
MIN_WORD_LENGTH = 5
MAX_WORD_LENGTH = 26


class Analyzer:
    def __init__(
        self, filename='test.txt', output='test.csv', top_n=25, debug=False
    ) -> None:
        self.debug = debug
        self.filepath = f'{PATH}\{filename}'
        self.output_path = f'{PATH}\{output}'
        self.top_n = top_n
        self.word_freq_map = defaultdict(int)

    def scan(self) -> None:
        print(f'[INFO]: loading file from {self.filepath}...')
        doc_text = open(self.filepath, 'r', encoding=UTF)
        text_string = doc_text.read().lower()

        # Ref: https://code.tutsplus.com/tutorials/counting-word-frequency-in-a-file-using-python--cms-25965
        # Starting from 3 will help in avoiding words whose frequency we may not be interested in counting, like if, of, in, etc.
        regex = r'\b[a-z]{' + f'{MIN_WORD_LENGTH},{MAX_WORD_LENGTH}' + '}\\b'
        match_pattern = re.findall(regex, text_string)

        for word in match_pattern:
            self.word_freq_map[word] += 1

        sorted_output = sorted(
            self.word_freq_map.items(), key=lambda x: x[-1], reverse=True
        )
        if self.debug:
            print(f'[DEBUG]: top {self.top_n} results...')
            for i, pair in enumerate(sorted_output):
                if i + 1 == self.top_n:
                    break
                print(pair[0], pair[-1])

        print(f'[INFO]: writing output to file at: {self.output_path}...')
        rows_written = 0
        with open(self.output_path, 'w', newline='') as f:
            csv_writer = csv.writer(f)
            for word, freq in sorted_output:
                if freq >= MIN_WORD_FREQ_LIMIT:
                    rows_written += 1
                    csv_writer.writerow((word, freq))
        print(f'[INFO]: successfully wrote {rows_written} rows!')


if __name__ == '__main__':
    test = Analyzer(debug=True)
    test.scan()
