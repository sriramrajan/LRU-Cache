# LRU-Cache

Create and use an LRU cache via unit-tests

## Time Complexity: O(1) using OrderedDict collection which uses DoublyLinkedList to help maintain order

Explanation: I found that the OrderedDict internally implements DoublyLinkedList and used the same for the O(1) lookup
The Time complexity is O(1) for set, add , update operations
Only Exception for getMostRecentKey which uses list splicing to get last key of O(N)
If needed, this could be easily modified via an extra class variable to provide O(1) 

## Space Complexity: O(N) to store all of the nodes till capacity == N. 
Explanation: Post this capacity, least recently used (LRU) items are removed and new items are added to maintain capacity.

Unit-tests borrowed from *https://www.algoexpert.io/questions/LRU%20Cache*
