#Based on AlgoExpert.io problem
from collections import OrderedDict
import unittest
import warnings

class LRU_Cache(object):
    def __init__(self, capacity):
        # Initialize class variables
        self.myHash = OrderedDict() # Maintain Dict order for keys
        self.capacity = capacity if capacity > 0 else 1
        if (capacity < 1):
            warnings.warn ("Value should be 1 or more!")

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent. 
        if key not in self.myHash.keys():
            return -1
        # Need to remove and re-insert key to update HashTable
        temp = self.myHash[key]
        self.myHash.pop(key)
        self.myHash[key] = temp
        # print (list(self.myHash.keys()))
        return temp

    def update(self, key, value):
        self.myHash[key] = value
        self.get(key) # Update MRU and LRU

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item. 
        if (key in self.myHash.keys()):
            self.update(key, value)
            return

        if (self.capacity > 0):
            self.capacity -= 1
        else:
            self.myHash.popitem(last=False)

        self.myHash[key] = value

    def getValueFromKey(self, key):
        # Write your code here.
        return self.get(key)

    def getMostRecentKey(self):
        # Write your code here.
        if len(self.myHash) == 0:
            return None
        return list(self.myHash.keys())[-1]

    def insertKeyValuePair(self, key, value):
        # Write your code here.
        return self.set(key, value)
        
letterMaps = {
    "a": 0,
    "b": 1,
    "c": 2,
    "d": 3,
    "e": 4,
    "f": 5,
    "g": 6,
    "h": 7,
    "i": 8,
    "j": 9,
}

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]


def testLruOfSize(size, testContext):
    # Instantiate cache and insert first key.
    lru = LRU_Cache(size)
    testContext.assertEqual(lru.getValueFromKey("a"), -1)
    lru.insertKeyValuePair("a", 99)
    testContext.assertEqual(lru.getMostRecentKey(), "a")
    testContext.assertEqual(lru.getValueFromKey("a"), 99)
    # Add existing key when cache isn't full.
    lru.insertKeyValuePair("a", 0)
    testContext.assertEqual(lru.getMostRecentKey(), "a")
    testContext.assertEqual(lru.getValueFromKey("a"), 0)
    # Add keys until cache reaches maximum capacity.
    for i in range(1, size):
        mostRecentLetter = letters[i - 1]
        testContext.assertEqual(lru.getMostRecentKey(), mostRecentLetter)
        # Test key retrieval when cache isn't full.
        for j in range(0, i):
            letter = letters[j]
            testContext.assertEqual(lru.getValueFromKey(letter), letterMaps[letter])
            testContext.assertEqual(lru.getMostRecentKey(), letter)
        currentLetter = letters[i]
        testContext.assertEqual(lru.getValueFromKey(currentLetter), -1)
        lru.insertKeyValuePair(currentLetter, letterMaps[currentLetter])
        testContext.assertEqual(lru.getMostRecentKey(), currentLetter)
        testContext.assertEqual(
            lru.getValueFromKey(currentLetter), letterMaps[currentLetter]
        )
    # Add keys now that cache is at maximum capacity.
    for i in range(size, len(letters)):
        mostRecentLetter = letters[i - 1]
        testContext.assertEqual(lru.getMostRecentKey(), mostRecentLetter)
        # Test key retrieval when cache is full.
        for j in range(i - size, i):
            letter = letters[j]
            testContext.assertEqual(lru.getValueFromKey(letter), letterMaps[letter])
            testContext.assertEqual(lru.getMostRecentKey(), letter)
        leastRecentLetter = letters[i - size]
        currentLetter = letters[i]
        testContext.assertEqual(lru.getValueFromKey(currentLetter), -1)
        lru.insertKeyValuePair(currentLetter, letterMaps[currentLetter])
        testContext.assertEqual(lru.getMostRecentKey(), currentLetter)
        testContext.assertEqual(
            lru.getValueFromKey(currentLetter), letterMaps[currentLetter]
        )
        testContext.assertEqual(lru.getValueFromKey(leastRecentLetter), -1)
    # Add existing keys when cache is full.
    for i in range(len(letters) - size, len(letters)):
        currentLetter = letters[i]
        testContext.assertEqual(
            lru.getValueFromKey(currentLetter), letterMaps[currentLetter]
        )
        lru.insertKeyValuePair(currentLetter, (letterMaps[currentLetter] + 1) * 100)
        testContext.assertEqual(
            lru.getValueFromKey(currentLetter), (letterMaps[currentLetter] + 1) * 100
        )


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        testLruOfSize(1, self)

    def test_case_2(self):
        testLruOfSize(2, self)

    def test_case_3(self):
        testLruOfSize(3, self)

    def test_case_4(self):
        testLruOfSize(4, self)

    def test_case_5(self):
        testLruOfSize(5, self)

    def test_case_6(self):
        testLruOfSize(6, self)

    def test_case_7(self):
        testLruOfSize(7, self)

    def test_case_8(self):
        testLruOfSize(8, self)

    def test_case_9(self):
        testLruOfSize(9, self)

    def test_case_10(self):
        testLruOfSize(10, self)

    def test11(self):
        our_cache = LRU_Cache(5)

        our_cache.set('a', 1);
        our_cache.set('b', 2);
        our_cache.set('c', 3);
        our_cache.set('d', 4);


        our_cache.get('a')      # returns 1
        our_cache.get('b')       # returns 2
        self.assertEqual(our_cache.get('x'),  -1)      # returns -1 because 9 is not present in the cache

        our_cache.set('e', 5) 
        our_cache.set('f', 6)
        # print(our_cache)
        self.assertEqual(our_cache.get('c'),  -1)      # returns -1 because the cache reached it's capacity and 3 was the least recently used entry

        our_cache.set('d', 10)
        self.assertEqual(our_cache.get('d'),  10)   

    def test12(self):
        with self.assertWarns(Warning):
            testEmpty = LRU_Cache(0)
            self.assertEqual(testEmpty.capacity, 1)
            self.assertEqual(testEmpty.get('a'), -1)

    def test13(self):
        with self.assertWarns(Warning):
            testEmpty = LRU_Cache(-2)
            self.assertEqual(testEmpty.capacity, 1)
            self.assertEqual(testEmpty.get('a'), -1)

if __name__ == "__main__":
    unittest.main()

