 #my brute method before tring trie implemetation
        if not words:
            return []
        words.sort()
        res = ['']
        longest = ''
        for word in words:
            if word[:-1] in res:
                if len(word) > len(longest):
                    longest = word
                res.append(word)
        return longest
