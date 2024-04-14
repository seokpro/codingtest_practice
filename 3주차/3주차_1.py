def solution(numbers, target):
    def dfs(index, current_sum):
        # base case: 모든 숫자를 다 사용했을 때
        if index == len(numbers):
            # 현재 합이 타겟 넘버와 같다면 1을 반환 (방법을 하나 찾았다는 의미)
            return 1 if current_sum == target else 0
        
        # 현재 숫자를 더하거나 빼는 경우를 모두 탐색
        plus = dfs(index + 1, current_sum + numbers[index])
        minus = dfs(index + 1, current_sum - numbers[index])
        
        # 두 경우의 방법 수를 합산
        return plus + minus
    
    # dfs 탐색 시작
    return dfs(0, 0)

# 예시 데이터로 테스트
numbers = [1, 1, 1, 1, 1]
target = 3
solution(numbers, target)