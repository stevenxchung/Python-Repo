'''
Given an array of strings words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line does not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left-justified, and no extra space is inserted between words.

Note:

- A word is defined as a character sequence consisting of non-space characters only.
- Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
- The input array words contains at least one word.
'''
from collections import defaultdict
from time import time
from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        lines = []  # [[words]]
        spaces_per_line = defaultdict(int)

        # How many words and spaces do I need on each line?
        line_no = 0
        line_size = 0
        curr_words = []
        for w in words:
            if maxWidth - (line_size + len(w) + 1) > 0:
                # Word w/ spaces OK
                curr_words.append(w)
                line_size += len(w) + 1
                spaces_per_line[line_no] += 1
            elif maxWidth - (line_size + len(w)) >= 0:
                # Word w/o space OK
                curr_words.append(w)
                line_size += len(w)
                spaces_per_line[line_no] += maxWidth - line_size
                lines.append(curr_words)
                # New line
                curr_words = []
                line_size = 0
                line_no += 1
            else:
                # Word does not fit, create new line
                # Add leftover spacing
                spaces_per_line[line_no] += maxWidth - line_size
                lines.append(curr_words)

                # New line
                curr_words = [w]
                line_no += 1

                # Any word is always <= max width
                if len(w) + 1 <= maxWidth:
                    line_size = len(w) + 1
                    spaces_per_line[line_no] += 1
                else:
                    line_size = len(w)
                    spaces_per_line[line_no] = 0

        # Double check last row spaces
        lines.append(curr_words)
        spaces_left = maxWidth - (
            len(''.join(lines[-1])) + spaces_per_line[line_no]
        )
        spaces_per_line[line_no] += spaces_left

        # Construct justified text
        for i in range(len(lines)):
            while spaces_per_line[i] > 0:
                if len(lines[i]) == 1:
                    # There is only one character in the line
                    lines[i][-1] = lines[i][-1] + ' ' * spaces_per_line[i]
                    spaces_per_line[i] = 0
                else:
                    for j in range(len(lines[i])):
                        if i == len(lines) - 1 and j == len(lines[i]) - 1:
                            # If last character in text
                            lines[i][j] = lines[i][j] + ' ' * spaces_per_line[i]
                            spaces_per_line[i] = 0
                            break
                        elif spaces_per_line[i] > 0 and j != len(lines[i]) - 1:
                            # Must have spaces left and not be last character
                            lines[i][j] = lines[i][j] + ' '
                            spaces_per_line[i] -= 1

            res.append(''.join(lines[i]))

        return res

    def reference(self, words: List[str], maxWidth: int) -> List[str]:
        result, current_list, num_of_letters = [], [], 0
        # result -> stores final result output
        # current_list -> stores list of words which are traversed but not yet added to result
        # num_of_letters -> stores number of chars corresponding to words in current_list
        for word in words:
            # total no. of chars in current_list + total no. of chars in current word
            # + total no. of words ~= min. number of spaces between words
            if num_of_letters + len(word) + len(current_list) > maxWidth:
                # size will be used for module "magic" for round robin
                # we use max. 1 because atleast one word would be there and to avoid modulo by 0
                size = max(1, len(current_list) - 1)

                for i in range(maxWidth - num_of_letters):
                    # add space to each word in round robin fashion
                    index = i % size
                    current_list[index] += ' '

                # add current line of words to the output
                result.append("".join(current_list))
                current_list, num_of_letters = [], 0

            # add current word to the list and add length to char count
            current_list.append(word)
            num_of_letters += len(word)

        # form last line by join with space and left justify to maxWidth using ljust (python method)
        # that means pad additional spaces to the right to make string length equal to maxWidth
        result.append(" ".join(current_list).ljust(maxWidth))

        return result

    def quantify(self, test_cases, runs=50000):
        sol_start = time()
        for i in range(runs):
            for case in test_cases:
                if i == 0:
                    print(*self.fullJustify(*case), sep='\n')
                    print('\n')
                else:
                    self.fullJustify(*case)
        print(f'Runtime for our solution: {time() - sol_start}\n')

        ref_start = time()
        for i in range(0, runs):
            for case in test_cases:
                if i == 0:
                    print(*self.reference(*case), sep='\n')
                    print('\n')
                else:
                    self.reference(*case)
        print(f'Runtime for reference: {time() - ref_start}')


if __name__ == '__main__':
    test = Solution()
    test_cases = [
        (['This', 'is', 'an', 'example', 'of', 'text', 'justification.'], 16),
        (['What', 'must', 'be', 'acknowledgment', 'shall', 'be'], 16),
        (
            [
                'Science',
                'is',
                'what',
                'we',
                'understand',
                'well',
                'enough',
                'to',
                'explain',
                'to',
                'a',
                'computer.',
                'Art',
                'is',
                'everything',
                'else',
                'we',
                'do',
            ],
            20,
        ),
    ]
    test.quantify(test_cases)
