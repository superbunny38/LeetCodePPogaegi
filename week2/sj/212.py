class Node:
    def __init__(self):
        self.children = {}
        self.end = ""

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        '''
        use trie and backtracking
        '''

        '''
        create a trie using all words, basically a word trie
        for iterating through each cell, if there is a node node in trie, 
        start backtracking and see if the word is there
        '''

        '''
        creating trie
        '''

        trie = Node()
        for word in words:
            node = trie
            for c in word:
                if c not in node.children:
                    node.children[c] = Node()
                node = node.children[c]
            node.end = word
        
        m, n = len(board), len(board[0])
        dx = [-1, 0, 1, 0]
        dy = [0, 1, 0, -1]
        result = []

        '''
        what should be the parameters for the backtrack?
        the things that "CHANGE" during the backtrack
        '''
        def backtrack(row, col, node):
            if node.end:
                result.append(node.end)
                node.end = ""
            
            temp = board[row][col]
            board[row][col] = '#'
            for i in range(4):
                nx, ny = row + dx[i], col + dy[i]
                if nx < 0 or nx >= m or ny < 0 or ny >= n:
                    continue
                if board[nx][ny] not in node.children:
                    continue
                backtrack(nx, ny, node.children[board[nx][ny]])
            board[row][col] = temp

        for i in range(m):
            for j in range(n):
                if board[i][j] in trie.children:
                    backtrack(i, j, trie.children[board[i][j]])
        
        return result
        
        '''
        TC: Very complicated
        SC: O(L) where L is the maximum length of a word in words
        => because trie will have k * L storage
            maximum recursive stack will have recusion of maximum L
        '''
