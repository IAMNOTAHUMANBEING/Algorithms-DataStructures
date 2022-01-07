# 리스트 컴프리헨션과 카운터 객체 사용
from typing import Collection

def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
    words = [ word for word in re.sub(r'[^\w]', ' ', paragraph).lower().split() if word not in banned]

    counts = collections.Counter(words)
    # 가장 흔하게 등장하는 단어의 첫 번째 인덱스 리턴 ex. [('ball', 3)]
    return counts.most_common(1)[0][0]
