from collections import defaultdict

words = ["eat", "tea", "tan", "ate", "nat", "bat"]
anagrams = defaultdict(list)

for word in words:
    key = ''.join(sorted(word))
    anagrams[key].append(word)

result = list(anagrams.values())
print(result)
