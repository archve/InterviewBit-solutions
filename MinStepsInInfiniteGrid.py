class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def coverPoints(self, A, B):
        stepcount = 0
        acount = A[0]
        bcount = B[0]
        
        for i in range(len(A)-1):
            cx = A[i]
            cy = B[i]
            nx = A[i+1]
            ny = B[i+1]
            
            xdis = abs(cx - nx)
            ydis = abs(cy - ny)
            
            if xdis > ydis:
                distance = xdis
            else:
                distance = ydis
            stepcount = stepcount + distance
          #  print(stepcount , localstep)
        return stepcount
        
