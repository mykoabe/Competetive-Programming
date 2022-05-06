 words = sorted(word[::-1] for word in set(words))
        words = words + ['']
        res = 0
        curr = ''
        for word in words:
            if not word.startswith(curr):
                res += len(curr) + 1
            curr = word  
        return res
        
