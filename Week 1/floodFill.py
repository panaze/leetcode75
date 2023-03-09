def floodFill(image, sr, sc, color):
     x = len(image)
     y = len(image[0])
    
     newColor = color
     originalColor = image[sr][sc]

     def dfs(i,j):
        #BASE CASE
        # If index is out of boundaries 
        if i < 0 or i >= x or j < 0 or j >= y:
            return
         #If element is already painted or is not equal to the color of the center
        if  image[i][j] == newColor or image[i][j] != originalColor:
            return

        else:
            #Flood fill the element
            image[i][j] = newColor

            #Call recursevely the 4 directionally connected elements (up,down,    left and right)
            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j+1)
            dfs(i,j-1)
    
     if image[sr][sc] != newColor:
         dfs(sr,sc)
        
     return image

            
          

def main():
    image = [[1,1,1],[1,1,0],[1,0,1]]
    sr = 1
    sc = 1
    color = 2
    floodFill(image, sr, sc, color)
    print(image)  

if __name__ == "__main__":
    main()