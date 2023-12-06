from PIL import Image 
import pandas as pd
from Pil_Image_Class import Image_To_Vector
import numpy as np
IMAGEPATH = "./download.png"
CSVPATH = "pixel.csv"
PIXELCOLUMN = "PixelVector"
BGCOLOUR = (0,0,0)
picture = Image_To_Vector(imagePath=IMAGEPATH)
picture.ToVector(BGCOLOUR,CSVPATH)
print(picture.CurrentPixelVector)
df = pd.read_csv(CSVPATH)
df.loc[PIXELCOLUMN] = picture.NU()
