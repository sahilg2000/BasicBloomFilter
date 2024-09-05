# Sahil Gaikwad
# 07/24/2024

import hashlib
import math


class BloomFilter:
    def __init__(self, size, hash_count):
        """
        :param size:        size of bloom filter bit array
        :param hash_count:  number of times to hash
        """
        self.size = size
        self.hash_count = hash_count
        self.bit_array = [0] * size
        self._dict = {}

    def _hashes(self, item):
        """
        Hashes at indexes based on hash_count repetition and returns expected hash indexes
        :param item:    item to hash
        :return:        indexes that should be (made) positive for hash item
        """
        result = []
        for i in range(self.hash_count):
            hash_result = int(hashlib.sha256(item.encode('ISO-8859-1') + str(i).encode('ISO-8859-1')).hexdigest(), 16)
            result.append(hash_result % self.size)
        return result

    def add(self, item):
        """
        Adds an item to the bloom filter bit array and its checking dictionary
        :param item:    item to add
        :return:        None
        """
        for hash_result in self._hashes(item):
            self.bit_array[hash_result] = 1
        self._dict[item] = 1

    def check(self, item):
        """
        Checks if item is in the bloom filter bit array
        :param item:    item to check for
        :return:        False if bloom filter indexes are not all 1, True otherwise
        """
        for hash_result in self._hashes(item):
            if self.bit_array[hash_result] == 0:
                return False
        return True

    def check_non_hash(self, item):
        """
        Checks if the item is present in the dict
        :param item:    item to check for
        :return:        True if present, False otherwise
        """
        try:
            if self._dict[item] == 1:
                return True
        except KeyError:
            return False


def bloom_load(bloom_filter_obj: BloomFilter, filepath: str):
    """
    Loads a text file into a bloom filter object
    :param bloom_filter_obj:    bloom filter to load into
    :param filepath:            filepath for text file
    :return:                    None
    """
    with open(filepath, 'r', encoding='ISO-8859-1') as file:
        for line in file:
            bloom_filter_obj.add(line.strip())


def test_dictionary(bloom_filter_obj, filepath):
    """
    Checks for false/true positives and false/true negatives
    :param bloom_filter_obj:    bloom filter object to check against
    :param filepath:            text file to check with (dictionary)
    :return:                    true positives, true negatives, false positives, false negatives (in that order)
    """
    true_pos = true_neg = false_pos = false_neg = 0
    with open(filepath, 'r', encoding='ISO-8859-1') as file:
        for line in file:
            check_word = line.strip()

            in_bloom = bloom_filter_obj.check(check_word)
            is_in_dict = bloom_filter_obj.check_non_hash(check_word)

            if in_bloom and is_in_dict:
                true_pos += 1
            elif not in_bloom and not is_in_dict:
                true_neg += 1
            elif in_bloom and not is_in_dict:
                false_pos += 1
            elif not in_bloom and is_in_dict:
                false_neg += 1
    return true_pos, true_neg, false_pos, false_neg


# Citation for the following function:
# Date: 07/24/2024
# Adapted from :
# Source URL: https://techtonics.medium.com/implementing-bloom-filters-in-python-and-understanding-its-error-probability-a-step-by-step-guide-13c6cb2e05b7
def calc_bit_count(capacity: int, error_rate: float):
    """
    Gives an approximate optimal number of bits needed for a bloom filter with 'capacity' number of elements
    :param capacity:    number of elements expected
    :param error_rate:  required error rate
    :return:            number of bits by calculation
    """
    num_bits = - (capacity * math.log(error_rate)) / (math.log(2) ** 2)
    return math.ceil(num_bits)


def main():
    """
    Adds a text file to bloom filter line by line
    and checks 'dictionary.txt' for true positives, true negatives, false positives, false negatives.
    """
    n_items = 100000000

    # false positive rate
    f_pos_rate = 0.01

    # calculations for bloom filter
    bit_count = calc_bit_count(n_items, f_pos_rate)
    hash_count = round((bit_count / n_items) * math.log(2))

    # create and load bloom filter
    b_filter = BloomFilter(bit_count, hash_count)
    bloom_load(b_filter, 'text_files/loader.txt')

    # get stats
    true_pos, true_neg, false_pos, false_neg = test_dictionary(b_filter, 'text_files/dictionary.txt')

    # displays statistics
    print(f"True Positives:     {true_pos}")
    print(f"True Negatives:     {true_neg}")
    print(f"False Positives:    {false_pos}")
    print(f"False Negatives:    {false_neg}")
    print("\n")


if __name__ == "__main__":
    main()
