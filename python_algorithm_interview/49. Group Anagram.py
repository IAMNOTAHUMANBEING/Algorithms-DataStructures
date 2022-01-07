# 정렬하여 딕셔너리에 추가

def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    anagrams = collection.defaultdict(list)

    for word in strs: 
        # 정렬하여 딕셔너리에 추가
        anagrams[''.join(sorted(word))].append(word)
    return anagrams.values()
