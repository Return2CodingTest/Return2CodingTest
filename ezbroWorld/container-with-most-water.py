class Solution:
    def maxArea(self, height: List[int]) -> int:
        p1,p2 = 0, len(height)-1
        maxWater = (p2 - p1) * min(height[p1], height[p2])
        while p1 < p2 : 
            
            # height(p1) > height(p2)라면 p1이 오른쪽으로 갈 이유가 없음.
            # 오른쪽으로 가더라도, height(p2)가 물넓이의 '높이'가 되므로..
            if height[p1] <= height[p2] : 
                p1+=1
            
            else:
                p2-=1
            
            maxWater = max(maxWater, (p2 - p1) * min(height[p1], height[p2]))
                
        return maxWater
