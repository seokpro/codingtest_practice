def solution(cards1, cards2, goal):
    idx1, idx2 = 0, 0  # cards1과 cards2의 현재 인덱스를 추적
    for word in goal:
        if idx1 < len(cards1) and cards1[idx1] == word:  # cards1에서 단어를 찾음
            idx1 += 1
        elif idx2 < len(cards2) and cards2[idx2] == word:  # cards2에서 단어를 찾음
            idx2 += 1
        else:
            return "No"  # goal의 현재 단어가 두 카드 뭉치에 없으면 "No" 반환
    return "Yes"  # 모든 단어를 찾으면 "Yes" 반환
