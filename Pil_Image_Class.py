from PIL import Image
import pandas as pd
import numpy as np
class Image_To_Vector:
    width : float
    height : float
    CurrentPixelVector : [float]
    IsVector = False
    def __init__(self, imagePath) -> None:
        self.loaded_Image = Image.open(imagePath)
        self.pixel_map = self.loaded_Image.load()
        self.width, self.height = self.loaded_Image.size
        print(f"This is the height: {self.height}. This is the width: {self.width}")
    def ToVector(self, bgColour : tuple, csvPath : str, pixel_column : str = "PixelVector"):
        self.IsVector = True
        self.CurrentPixelVector = [0] * self.loaded_Image.size[0]*self.loaded_Image.size[1] # Create an arary with the size of the amount of pixels in a 4k image
        PixelCsv = pd.read_csv(csvPath)
        for i in range(self.width):
            for j in range(self.height):
                if self.loaded_Image.getpixel((i,j)) != (bgColour):
                    self.CurrentPixelVector[i] = 1
    def NU(self):
        return np.asvector(self.loaded_Image)
    def __str__(self):
        if self.IsVector:
            return str(self.CurrentPixelVector)
        else:
            return 'Must convert to vector'
    
        
Image_To_Vector("./download.png")
Image_To_Vector("./download.png").ToVector(bgColour=(0,0,0), csvPath="pixel.csv")

        
        
