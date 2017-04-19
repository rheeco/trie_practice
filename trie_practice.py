# practicing trie implementation
# using the implementation provided by Steve Hanov -- just adding
# personal comments

# Trie data structure keeps a set of words, organized with one node
# per letter.  Each node has branch for each letter that may follow
# in set of words.

# e.g., if SET OF WORDS includes
# short, shirt, shorter, shortest, shirts
# Trie would look like... ?
#                       - s - t
# s - h - o - r - t - e - r
#       - i - r - t - s
        
class TrieNode:
    def __init__(self):
        self.word = None
        self.children = {}
        
    def insert(self, word):
        # why create new var node?
        # --> use to traverse to next/child node each time child is
        #     added
        node = self

        for letter in word:
            if letter not in node.children:
                node.children[letter] = TrieNode()
            node = node.children[letter]

        node.word = word

    # Return list of all words less than given max_edit_distance from the
    # target word
    # what if this was a fxn of the TrieNode class...
    def search(self, word, max_edit_distance):
        # build first row
        current_row = range(len(word) + 1)
    
        results_list = []
    
        # recursively search each branch of trie
        for letter in self.children:
            TrieNode._search_helper(
                self.children[letter],
                letter,
                word,
                current_row,
                results_list,
                max_edit_distance)
        
        return results_list
    
    # recursive search helper -- assumes previous_row has been filled in
    # already
    def _search_helper(this_node,
                       letter,
                       word,
                       previous_row,
                       results_list,
                       max_edit_distance):
        columns = len(word) + 1
        # current_row is a list of 1 int?
        current_row = [previous_row[0] + 1]
        
        # build row for letter, write column for each letter in target word,
        # plus one for empty string at column 0
        for column in range(1, columns):
            insert_dist = current_row[column - 1] + 1
            delete_dist = current_row[column - 1]
            
            if word[column - 1] != letter:
                replace_dist = previous_row[column - 1] + 1
            else:
                replace_dist = previous_row[column - 1]
            current_row.append(min(insert_dist, delete_dist, replace_dist))
            
        # if last entry in row indicates optimal cost is less than
        # max_edit_distance, and there is a word in this trie node, then add it
        if current_row[-1] <= max_edit_distance and this_node.word != None:
            results_list.append((this_node.word, current_row[-1]))
        
        # if any entries in row are less than max_edit_distance, then
        # recursively search each branch
        if min(current_row) <= max_edit_distance:
            for letter in this_node.children:
                TrieNode._search_helper(
                    this_node.children[letter],
                    letter,
                    word,
                    current_row,
                    results_list,
                    max_edit_distance)
