class Solution:
	# @param A : tuple of list of integers
	# @return a list of integers
	def spiralOrder(self, A):
	    left = 0
	    right = len(A[0])
	    upper = 0
	    down = len(A)
	    
	    #print (left,right, upper, down)
	    begleft = left
	    begright = right
	    begupper = upper
	    beglower = down
	    
	    currow = 0
	    curcol = 0
	    
	    elementcount = right * down
	    
	    direction = 'R' # can be R,L,U,D in order R->D->L->U->R
	    
	    printlist = []
	    
	    while elementcount != 0:
	        
	        if direction == 'R':
	            for i in range(curcol,right,1):
	                printlist.append(A[currow][i])
                    curcol = i
                    elementcount = elementcount - 1
	            upper = upper + 1
	            currow = currow + 1
	            direction = 'D'
	        
	        elif direction == 'D':
                for i in range(currow,down,1):
                    printlist.append(A[i][curcol])
                    currow = i
                    elementcount = elementcount - 1
                right = right - 1
                curcol = curcol - 1
                direction = 'L'
                    
            elif direction == 'L':
                for i in range(curcol,left-1, -1):
                    printlist.append(A[currow][i])
                    curcol = i
                    elementcount = elementcount - 1
                down = down - 1
                currow = currow - 1
                direction = 'U'
                    
            elif direction == 'U':
                for i in range(currow,upper-1,-1):
                    printlist.append(A[i][curcol])
                    currow = i
                    elementcount = elementcount - 1
                left = left + 1
                curcol = curcol + 1
                direction = 'R'
                
            
            
        return printlist

	            
	            
	        
