from dictionary.base_dictionary import BaseDictionary
from dictionary.word_frequency import WordFrequency
import time

# Class representing a node in the Trie
class TrieNode:

    def __init__(self, letter=None, frequency=None, is_last=False):
        self.letter = letter
        self.frequency = frequency
        self.is_last = is_last
        self.children: dict[str, TrieNode] = {}

class TrieDictionary(BaseDictionary):

    def __init__(self):
        self.root = TrieNode()

    def build_dictionary(self, words_frequencies: [WordFrequency]):
        for word_freq in words_frequencies:
            self.add_word_frequency(word_freq)

    def search(self, word: str) -> int:
        start_time = time.time()
        node = self.root
        for letter in word:
            if letter not in node.children:
                return 0
            node = node.children[letter]
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Search time: {elapsed_time} seconds")
        return node.frequency if node.is_last else 0

    def add_word_frequency(self, word_frequency: WordFrequency) -> bool:
        node = self.root
        word = word_frequency.word
        frequency = word_frequency.frequency

        for letter in word:
            if letter not in node.children:
                node.children[letter] = TrieNode(letter)
            node = node.children[letter]

        if node.is_last:
            return False  # Word already exists
        else:
            node.is_last = True
            node.frequency = frequency
            return True

    def delete_word(self, word: str) -> bool:
        node = self.root
        path = []
        for letter in word:
            if letter not in node.children:
                return False  # Word not found
            path.append((node, letter))
            node = node.children[letter]
        if not node.is_last:
            return False  # Word not found
        node.is_last = False
        node.frequency = None

        # Delete unnecessary nodes
        for parent, letter in reversed(path):
            if node.children:
                break
            del parent.children[letter]
            node = parent

        return True

    def autocomplete(self, prefix_word: str) -> [WordFrequency]:
        node = self.root
        for letter in prefix_word:
            if letter not in node.children:
                return []
            node = node.children[letter]

        def dfs(node, prefix):
            results = []
            if node.is_last:
                results.append((prefix, node.frequency))
            for letter, child in node.children.items():
                results.extend(dfs(child, prefix + letter))
            return results

        completions = dfs(node, prefix_word)
        completions.sort(key=lambda x: x[1], reverse=True)
        return [WordFrequency(word, frequency) for word, frequency in completions[:3]]
