from PIL import Image, ImageDraw
import requests as rq
def fotobirlestir(takim1,cizgi,takim2):
    
    
   # URLs of the images
    url1 = takim1
    url3 = takim2
    # Open the first image
    image1 = Image.open(rq.get(url1, stream=True).raw)
    # Open the third image
    image2 = Image.open(rq.get(url3, stream=True).raw)
    (width1, height1) = image1.size

    # Get the width and height of the second image
    (width2, height2) = image2.size

    # Create a new image with black background
    result = Image.new("RGB", (width1 + width2, max(height1, height2)), (0, 0, 0))

    # Paste the first image onto the new image
    result.paste(image1, (0,0))

    # Paste the second image onto the new image
    result.paste(image2, (width1, 0))

    # Save the final image
    result.save("./uploads/final.png")
    
    return result
__all__ = ['fotobirlestir']