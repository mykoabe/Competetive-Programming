class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digitLogs, letterLogs = [], []
        for log in logs:
            if log.split()[1].isdigit():
                digitLogs.append(log)
            else:
                letterLogs.append(log)
        letterLogs.sort(key = lambda x: (x.split()[1:], x.split()[0]))
        return letterLogs + digitLogs