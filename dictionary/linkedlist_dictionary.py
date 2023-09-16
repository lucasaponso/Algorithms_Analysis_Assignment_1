from dictionary.base_dictionary import BaseDictionary
from dictionary.word_frequency import WordFrequency
import time


class ListNode:
    '''
    Define a node in the linked list
    '''
    def __init__(self, word_frequency: WordFrequency):
        self.word_frequency = word_frequency
        self.next = None

class LinkedListDictionary(BaseDictionary):

    def __init__(self):
        self.head = ListNode(None)  # Dummy head node
        self.word_set = {}  # Hash table to store added words

    def build_dictionary(self, words_frequencies: [WordFrequency]):
        """
        Construct the data structure to store nodes
        @param words_frequencies: list of (word, frequency) to be stored
        """
        for word_freq in words_frequencies:
            self.add_word_frequency(word_freq)

    def search(self, word: str) -> int:
        start_time = time.time()
        """
        Search for a word
        @param word: the word to be searched
        @return: frequency > 0 if found and 0 if NOT found
        """
        current = self.head.next
        while current is not None:
            if current.word_frequency.word == word:
                return current.word_frequency.frequency
            current = current.next
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Search time: {elapsed_time} seconds")
        return 0

    def add_word_frequency(self, word_frequency: WordFrequency) -> bool:
        """
        Add a word and its frequency to the dictionary
        @param word_frequency: (word, frequency) to be added
        :return: True whether succeeded, False when word is already in the dictionary
        """
        word = word_frequency.word
        if word in self.word_set:
            return False  # Word already exists

        current = self.head
        while current.next is not None:
            current = current.next

        new_node = ListNode(word_frequency)
        new_node.next = current.next
        current.next = new_node

        self.word_set[word] = True  # Add word to the hash table
        return True

    def delete_word(self, word: str) -> bool:
        """
        Delete a word from the dictionary
        @param word: word to be deleted
        @return: whether succeeded, e.g. return False when word not found
        """
        current = self.head
        while current.next is not None:
            if current.next.word_frequency.word == word:
                current.next = current.next.next
                if word in self.word_set:
                    del self.word_set[word]
                return True
            current = current.next
        return False

    def autocomplete(self, word: str) -> [WordFrequency]:
        """
        Return a list of 3 most-frequent words in the dictionary that have 'word' as a prefix
        @param word: word to be autocompleted
        @return: a list (could be empty) of (at most) 3 most-frequent words with prefix 'word'
        """
        completions = []
        current = self.head.next

        while current is not None:
            if current.word_frequency.word.startswith(word):
                completions.append(current.word_frequency)
            current = current.next

        completions.sort(key=lambda x: x.frequency, reverse=True)
        return completions[:3]
