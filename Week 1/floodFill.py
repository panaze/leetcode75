def floodFill( image, sr, sc, color):
        if image[sr][sc] == color:
          return image
        else:
            image[sr][sc] = color
            
            image[sr-1][sc-1] = color
            image[sr-1][sc] = color

            image[sr][sc-1] = color
            image[sr+1][sc-1] = color
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