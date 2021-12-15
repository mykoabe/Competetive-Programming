def sorting(s):
    mixedSenetence = s.split()
    dictionaryWord ={}
    sortedSentence = ''
    for word in mixedSenetence:
        dictionaryWord[word[-1]]= word[:-1]
    for word in sorted(dictionaryWord):
        sortedSentence= sortedSentence+''.join(dictionaryWord[word])+' '
    sortedSentence=sortedSentence[:-1]
    return sortedSentence
s = "is2 sentence4 This1 a3"
print(sorting(s))