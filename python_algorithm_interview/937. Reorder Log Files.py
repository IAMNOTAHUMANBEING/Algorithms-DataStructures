# 람다와 + 연산자 이용

def reorderLogFiles(self, logs: List[str]) -> List[str]:
    letters, digits = [], []
    for log in logs:
        if log.split()[1].isdigit():
            digits.append(log)
        else:
            letter.append(log)
    
    # 2개의 키를 람다 표현식으로 정렬
    letters.sort(key=lambda x:(x.split()[1:], x.split()[0]))    
    return letters + digits