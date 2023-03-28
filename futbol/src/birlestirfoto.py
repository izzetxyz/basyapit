from PIL import Image, ImageDraw
import requests as rq
import io
from bs4 import BeautifulSoup
import dropbox
headers = {
    "user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 123.0.0.21.115 (iPhone11,8; iOS 14_0; en_US; en-US; scale=2.00; 828x1792; 165586599)",
    "content-type": "application/json",
    "cache-control": "private, no-cache, no-store, must-revalidate",
    "access-control-allow-origin": "https://www.instagram.com",
    "access-control-expose-headers": "X-IG-Set-WWW-Claim",
    "alt-svc": '''h3=":443"; ma=86400'''
}
def fotobirlestir(takim1,takim2):
    
    
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
    result.save("./uploads/mac123456789.png")

    # Dropbox API anahtarınızı buraya girin
    API_KEY = "sl.BW7r1QgCZk2s3l5ZQ7E1BrJ5OyEUB5Carc1IexhJ8KA6m7xDVxu3Jm110seoyyWPAurDMmGJW2sAal2k-7ZnxQqzDlbf0XKtBYEq-GUikwwPcTf40P7qw9P94pE78DgQoYlRR39CnJSr"

    # Kimlik bilgilerinizi oluşturun
    dbx = dropbox.Dropbox(API_KEY)
    # Fotoğraf dosyasının yolu
    file_path = "./uploads/mac123456789.png"

    # Fotoğrafı yükleme
    with open(file_path, "rb") as f:
        data = f.read()

    # Fotoğrafı Dropbox'a yükleme
    response = dbx.files_upload(data, '/mac123456789.png', mode=dropbox.files.WriteMode.overwrite)

    # Fotoğrafın dosya yolu
    file_path = response.path_display

    # Fotoğrafın linkini alma
    link_metadata = dbx.files_get_temporary_link(file_path)
    link = link_metadata.link
    # if you want to have the link with previews.dropbox.com
    return link
__all__ = ['fotobirlestir']